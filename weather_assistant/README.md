# Weather Chatbot – LLM & External API Integration 

## Overview
This project implements a conversational Weather Chatbot that combines a Large Language Model (LLM) with an external weather data API.  
The system is designed to demonstrate correct API integration, clear separation of responsibilities, and robust hallucination prevention.

## Project Idea
The chatbot allows users to ask weather-related questions in free natural language.  
The system identifies the relevant location, retrieves real weather data from the OpenWeather API, and uses a language model **only** to explain or interpret this data in a natural and user-friendly way.

## Design Principles
- Clear separation of concerns between language understanding and data retrieval  
- External APIs serve as the **single source of factual truth**  
- Controlled and deterministic use of the language model to prevent hallucinations  

## Project Structure
- `main.py` – Main application loop and orchestration  
- `assistant/weather_api.py` – OpenWeather API integration  
- `assistant/llm_client.py` – OpenAI LLM interaction and entity extraction  
- `assistant/prompt.py` – System prompt and behavioral rules  
- `assistant/config.py` – API key configuration  
- `requirements.txt` – Project dependencies  

## Execution Instructions
1. Install Python **3.10** or higher  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Insert your OpenAI API key and OpenWeather API key in:
   assistant/config.py
4. Run the application:
   python main.py
5. Interact with the chatbot, to exit type:
   exit

