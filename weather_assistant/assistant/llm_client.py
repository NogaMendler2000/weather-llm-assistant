from openai import OpenAI
from assistant.config import OPENAI_API_KEY
import json


def ask_llm(system_prompt: str, user_input: str, external_data: dict) -> str:
    if not OPENAI_API_KEY:
        return "OpenAI API key not configured."

    client = OpenAI(api_key=OPENAI_API_KEY)

    # Build the conversation for the language model
    messages = [
        # System prompt defines the assistant's behavior and rules
        {"role": "system", "content": system_prompt},

        # Pass authoritative external data (weather API results)
        # so the model relies on real facts and does not hallucinate
        {
            "role": "system",
            "content": f"Authoritative external data:\n{external_data}"
        },

        # The user's actual question
        {"role": "user", "content": user_input},
    ]

    # Ask the language model to generate a response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.2  # low creativity for stable explanations
    )

    return response.choices[0].message.content.strip()


def extract_city_for_weather_api(user_input: str) -> str | None:
    """
    Extracts a city name that can be safely used with the weather API.
    - If the user mentions a city, return that city.
    - If the user mentions a country, return its capital city.
    - If the request is unclear, return None.
    """

    if not OPENAI_API_KEY:
        return None

    client = OpenAI(api_key=OPENAI_API_KEY)

    # Instruct the model to return structured JSON only
    messages = [
        {
            "role": "system",
            "content": (
                "Extract a city name to query a weather API.\n"
                "- If the user mentions a CITY, return that city.\n"
                "- If the user mentions a COUNTRY, return the CAPITAL CITY of that country.\n"
                "- If the request is unclear or too broad, return null.\n"
                "Return ONLY valid JSON in this format:\n"
                '{"city": string | null}'
            )
        },
        {"role": "user", "content": user_input}
    ]

    # Call the model with zero temperature for deterministic output
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    try:
        data = json.loads(response.choices[0].message.content.strip())

        # Return the extracted city (or None)
        return data.get("city")
    except Exception:
        # If parsing fails, safely return None instead of guessing
        return None
