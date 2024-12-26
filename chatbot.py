from crewai import Agent
from google import genai
import re

# Initialize the Gemini client (Gemini API)
client = genai.Client(api_key="AIzaSyDT7Zz6bie-nA4BZOlCd0ZAE4n5wbqZNoc")

def match_cv_to_job(cv_text, job_description):
    """
    Analyzes the CV's match with the job description using the API.
    """
    data = f"Job Description: {job_description}\nCV: {cv_text}\nPlease give a match score (out of 10) and suggestions to improve the CV."

    try:
        # Generate a response via the API
        response = client.models.generate_content(model='gemini-2.0-flash-exp', contents=data)
        
        # Clean the raw response
        result = response.text.strip()

        # If no valid response, return an error message
        if not result or "Not found" in result:
            return "No result generated. Check the inputs provided."

        # Extract the match score
        score = "No score found"  # Default value
        score_match = re.search(r"(\d{1,2})/10", result)
        if score_match:
            score = score_match.group(1)

        # Extract the suggestions section from "Suggestions to improve the CV"
        suggestions = []
        suggestions_start = result.lower().find("suggestions to improve the cv:")
        if suggestions_start != -1:
            suggestions_text = result[suggestions_start:]
            suggestions_end = suggestions_text.find("in summary")
            if suggestions_end != -1:
                suggestions_text = suggestions_text[:suggestions_end]

            # Split and clean the suggestions text
            suggestions = [s.strip() for s in suggestions_text.split("\n") if s.strip()]

        # Limit to 3 suggestions, if necessary
        suggestions = suggestions[:6]

        # If no suggestions are found, provide a generic one
        if not suggestions:
            suggestions = ["Try to include more relevant details for the job offer."]

        # Return match score and suggestions in the desired format
        return f"Your CV scored {score}/10. Here’s how you can improve:\n" + "\n".join([f"- {s}" for s in suggestions])

    except Exception as e:
        return f"Error while analyzing the CV: {str(e)}"


class HRChatbotAgent(Agent):
    def __init__(self, **kwargs):
        kwargs.setdefault('role', "HR assistant") 
        kwargs.setdefault('goal', "Help users improve their CV to match job descriptions.")
        kwargs.setdefault('backstory', "I am an AI assistant trained to analyze CVs and provide feedback.")
        super().__init__(**kwargs)
        
    def receive_message(self, message, memory):
        if "job_description" not in memory:
            memory["job_description"] = message
            return "Got it! Please share your CV so I can help."
        
        elif "cv_text" not in memory:
            memory["cv_text"] = message
            job_description = memory["job_description"]
            cv_text = memory["cv_text"]
            result = match_cv_to_job(cv_text, job_description)
            memory.clear()  # Clear the memory after analysis
            return f"Your CV has been analyzed. Here are the results:\n{result}"

def chatbot():
    print("Welcome to HR Chatbot: CV Helper!")
    
    # Create a CrewAI agent for interaction
    agent = HRChatbotAgent(
        role="HR assistant",
        goal="Help users improve their CV to match job descriptions.",
        backstory="I am an AI assistant trained to analyze CVs and provide feedback.",
        llm="gpt-4",
        verbose=True,
    )
    
    memory = {}  # Manually manage memory with a dictionary

    # Ask for the job description once
    job_description = input("Please enter the job description:\n")
    print(agent.receive_message(job_description, memory))
    
    # Ask for the CV text once
    cv_text = input("\nPlease enter the text of your CV:\n")
    print(agent.receive_message(cv_text, memory))

# Start the chatbot
if __name__ == "__main__":
    chatbot()
