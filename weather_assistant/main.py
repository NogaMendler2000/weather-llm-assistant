from assistant.weather_api import fetch_current_weather
from assistant.prompt import SYSTEM_PROMPT
from assistant.llm_client import ask_llm, extract_city_for_weather_api


def main():
    print("Weather Chatbot ☁️")
    print("Talk to me about the weather. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        # The LLM extract the city 
        city = extract_city_for_weather_api(user_input)

        # if no city was mentioned, just reply without calling the weather API
        if city is None:
            response = ask_llm(
                system_prompt=SYSTEM_PROMPT,
                user_input=user_input,
                external_data={}
            )
            print("\nAssistant:", response, "\n")
            continue

        # fetch weather only if a city was found
        weather_data = fetch_current_weather(city)

        response = ask_llm(
            system_prompt=SYSTEM_PROMPT,
            user_input=user_input,
            external_data=weather_data
        )

        print("\nAssistant:", response, "\n")


if __name__ == "__main__":
    main()
