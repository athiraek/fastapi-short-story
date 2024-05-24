# FastAPI Short Story Generator

A FastAPI application that allows users to create characters and generate short stories using OpenAI.

## Endpoints

### Create a Character
- **Endpoint:** `/api/create_character`
- **Description:** Create a new character.
- **Inputs:** name, description
- **Response:** The created character with a 201 status code.

### Generate a Story
- **Endpoint:** `/api/generate_story`
- **Description:** Generate a story for a character.
- **Inputs:** character_id
- **Response:** The generated story with a 201 status code.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/fastapi-short-story.git
