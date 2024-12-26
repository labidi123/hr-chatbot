# hr-chatbot
# HR Chatbot - CV Helper

## Overview
HR Chatbot is an AI-powered assistant designed to help job seekers improve their CVs to match job descriptions. By analyzing the provided CV and job description, the chatbot provides a score (out of 10) and suggestions to enhance the CV for better alignment with the job requirements.

## Features
- **Job Description Input**: The user provides a job description.
- **CV Input**: The user provides their CV text.
- **Match Scoring**: The chatbot analyzes the match between the CV and job description, providing a score out of 10.
- **Suggestions for Improvement**: Based on the analysis, the chatbot gives actionable suggestions to improve the CV.

## How It Works

1. **User**: Provides the job description.
2. **Bot**: Acknowledges the description and asks for the CV.
3. **User**: Pastes the CV text.
4. **Bot**: Analyzes the CV, compares it to the job description, and provides a match score along with suggestions for improvement.

## Example Interaction

### Step 1: Job Description
**User**: "Here's my job description: Data Scientist with strong experience in Python, Machine Learning, SQL, and Data Visualization"

### Step 2: CV Input
**Bot**: "Got it! Please share your CV so I can help."

**User**: (Pastes CV)

### Step 3: Result
Your CV has been analyzed. Here are the results:
Your CV scored 6/10. Here’s how you can improve:
- Suggestions to Improve the CV:**
- Here are specific ways to improve the CV, focusing on the weaknesses:
- 1.  **Quantify Achievements:** Instead of just saying "worked with", use action verbs and numbers:
- *   **Instead of:** "Worked with regression models."
- *   **Try:** "Developed and deployed regression models that improved prediction accuracy by 15%."
- *   **Instead of:** "Performed data extraction using SQL."
## Requirements

- Python 3.8 or higher
- `google` library for Gemini API integration
- `re` for regular expression matching
- Internet connection for API calls

## Installation

1. pip install google-generativeai
2. pip install crewai
3. pip install 'crewai[tools]'
4. pip install gemini-api
