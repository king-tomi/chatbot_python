
### README for Chatbot for University of Dundee

# Chatbot for University of Dundee

## Overview
This repository contains the code for a chatbot designed to assist students and prospective applicants with inquiries about the University of Dundee. The chatbot leverages OpenAI's GPT-4 for natural language processing and is deployed using FastAPI.

## Project Description
The chatbot provides information related to academic programs, admissions, campus facilities, and events at the University of Dundee. It offers accurate and friendly responses, enhancing user experience and engagement.

## Features
- Natural language processing with OpenAI GPT-4
- FastAPI-based backend for efficient request handling
- Interactive web interface for user interaction

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/king-tomi/university-chatbot.git
   cd university-chatbot

2. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
```

3. Run The FastAPI Server
  ```bash
  uvicorn app:app --reload
```

# Frontend Setup

1. Navigate to the frontend directory:
``` bash
  cd ../frontend
```

2. Install the required Node.js packages:
``` bash
  npm install
```

3. Start the React app:
```bash
  npm start
```

4. Open your browser and go to: ```http://localhost:3000```

## Usage

- Access the chatbot interface at ```http://localhost:8000.```
- Interact with the chatbot by asking questions related to the University of Dundee.

## System Prompt
- The chatbot uses a system prompt to guide its responses, ensuring they are relevant and helpful for university-related queries.

## Project Structure
``` css
dundee-chatbot/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
│
└── README.md
```
