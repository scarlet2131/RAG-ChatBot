# Chatbot with FARM Stack and RAG Application

Welcome to the Chatbot project! This chatbot is built using the FARM stack (FastAPI, React, MongoDB Atlas) and implements a Retrieval-Augmented Generation (RAG) application to enhance its capabilities.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  

## Introduction

This project is a chatbot application designed to provide intelligent and context-aware responses by leveraging the FARM stack and a RAG application. The chatbot uses MongoDB Atlas as its database to store and retrieve documents, enhancing its response capabilities based on the stored information.

## Features

- Intelligent and context-aware responses using RAG application
- User authentication and registration
- Integration with MongoDB Atlas for document storage and retrieval
- Real-time chat interface
- Responsive design with React

## Technologies Used

- **FastAPI**: For building the backend API
- **React**: For building the frontend user interface
- **MongoDB Atlas**: For cloud-based database storage
- **RAG Application**: For enhanced response generation using document retrieval

## Setup and Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- Node.js and npm installed
- Python 3.7+ installed
- MongoDB Atlas account

### Backend Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot/backend
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
4. Set up environment variables in a .env file:
   ```sh
   MONGO_URL=your_mongo_url
   MONGO_DB=your_database_name
   OPENAI_API_KEY=your_openai_api_key
5. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   
### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd ../frontend
2. Install the required packages:
   ```sh
   npm install
3. Start the React development server:
   ```sh
   npm start
### Usage
Access the frontend at http://localhost:3000.
Interact with the chatbot through the chat interface.
The chatbot will respond based on the documents stored in the MongoDB Atlas database.





