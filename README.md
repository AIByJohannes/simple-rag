# Simple RAG Chatbot

## Description
This project implements a Retrieval Augmented Generation (RAG) system. It provides a chatbot interface that can answer questions based on a knowledge base. The system is containerized using Docker for ease of deployment and development.

## Project Structure

The project is organized into the following main directories:

*   `/app`: Contains the FastAPI backend application.
    *   `main.py`: The main entry point for the FastAPI application, defining API endpoints.
    *   `services.py`: Houses the business logic for the application.
    *   `models.py`: Defines Pydantic models for data validation and serialization.
    *   `database.py`: Handles MongoDB connection and data interaction logic.
    *   `config.py`: Manages application configuration settings.
    *   `requirements.txt`: Lists Python dependencies for the backend.
*   `/web`: Contains the Vite + React frontend application.
    *   `src/App.jsx`: The main React component for the user interface.
    *   `package.json`: Lists JavaScript dependencies and scripts for the frontend.
*   `/docker`: Contains Dockerfiles for building the application services.
    *   `api.Dockerfile`: Dockerfile for the FastAPI backend.
    *   `web.Dockerfile`: Dockerfile for the Vite + React frontend.
*   `docker-compose.yml`: Located in the project root, this file defines and configures the services (API, web, database, etc.) for local development and deployment.
*   `chatbot.py`: A simple Python script in the project root for command-line interaction with the backend API (primarily for testing).

## Getting Started

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)

### Building and Running the Application

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Build and start the services** using Docker Compose:
    ```bash
    docker-compose up --build -d
    ```
    The `-d` flag runs the containers in detached mode (in the background).

3.  **Access the applications:**
    *   **API Backend:** [http://localhost:8000](http://localhost:8000)
    *   **Web Frontend:** [http://localhost:3000](http://localhost:3000)

### Stopping the Application

To stop all running services, navigate to the project root directory and run:
```bash
docker-compose down
```
If you want to remove the volumes (like the MongoDB data), you can use:
```bash
docker-compose down -v
```

## API Endpoints

Currently, the following API endpoint is available:

*   **`GET /`**
    *   **Description:** Returns a welcome message from the API.
    *   **Response:**
        ```json
        {
          "message": "Welcome to the FastAPI application!"
        }
        ```

More endpoints for chat functionality and knowledge base interaction will be added as development progresses.

## Functional Requirements
1. Implement a traditional simple RAG system.
2. Make the RAG system accessible via an API.
3. Provide a web application with a user interface for chat.

## Technical Requirements
The project aims to use the following technologies:
- **Containerization:** Docker, Docker Compose
- **Database:** MongoDB (for application data and potentially vector search in the future)
- **LLM Inference:** Placeholder for vLLM (or a similar solution) for serving Large Language Models (e.g., Llama 8B) and embeddings (e.g., Nomic).
- **Backend API:** Python with FastAPI and LangChain.
- **Frontend Web App:** Vite + React.

---
*This README is a work in progress and will be updated as the project evolves.*
