AI-Powered Quotes Assistant

A high-performance conversational AI assistant designed to deliver curated wisdom and motivational content. Built using the Rasa Open Source framework, this project features a modern glassmorphism-based web interface and a custom Python backend for managing a diverse library of quotes across multiple thematic topics.

The assistant provides users with inspirational and motivational quotes through natural language conversations, creating an engaging and interactive experience.

Key Features:

Multi-Topic Quote Engine

Provides quotes across more than 15 thematic categories including:

-Success
-Discipline
-Leadership
-Hard Work
-Life
-Motivation
-Inspiration
-Love
-Humor

Natural Language Understanding (NLU)

Uses Rasa’s DIETClassifier to understand natural user queries and classify intents accurately, enabling users to interact with the assistant using normal conversational language.

Interactive Web Interface

Includes a modern dark-mode dashboard with glassmorphism-inspired UI design, interactive topic chips, and a responsive chat interface.

Custom Action Server

Implements a Python-based Rasa Action Server to handle dynamic quote retrieval, topic matching, and backend logic.

Technical Stack:

Core Framework:

-Rasa Open Source 3.x

Programming Language:

-Python 3.10 (optimized for Rasa compatibility)

Frontend:

-HTML5
-CSS3 (Flexbox layout and animations)
-JavaScript (Asynchronous Fetch API)

Backend:

-Rasa Action Server (Python SDK)


Project Structure:

project-folder/
│
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
│
├── actions/
│   └── actions.py
│
├── models/
│
├── domain.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
│
└── index.html

Description

data/
Contains the Natural Language Understanding training data and conversation rules.

actions/
Includes custom Python logic for retrieving quotes and matching user requests with topics.

domain.yml
Defines chatbot intents, entities, responses, actions, and session configuration.

index.html
Provides the browser-based chatbot interface.


Installation and Setup:

1. Environment Configuration

Ensure Python 3.10 is installed on your system.

Create and activate a virtual environment to isolate project dependencies.

powershell
Create virtual environment
py -3.10 -m venv venv

Activate virtual environment
.\venv\Scripts\activate


2. Install Dependencies

Install required libraries using pip.

powershell
pip install rasa==3.6.15 setuptools


3. Train the Model

Train the chatbot model using the Rasa training command.

powershell
rasa train


This command generates a trained chatbot model inside the models/ directory.


Running the Application

To run the assistant, you must start two server instances.


1. Start the Action Server

This server handles backend logic and quote retrieval.

powershell
rasa run actions

2. Start the Rasa Server

This server manages NLU processing and API communication.

powershell
rasa run --enable-api --cors "*"

3. Launch the Web Interface

Open the following file in a web browser:

index.html

You can now interact with the AI-Powered Quotes Assistant through the web interface.

Future Enhancements

-Sentiment analysis for emotional quote recommendations
-Expanded quote dataset across additional topics
-Integration with databases for dynamic content updates
-Deployment using Docker or cloud platforms
-Voice-enabled chatbot interaction

