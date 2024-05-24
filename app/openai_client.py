import openai

openai.api_key = "your-openai-api-key"

def generate_story(character_name: str, character_description: str) -> str:
    prompt = f"Write a short story (4 to 5 sentences) about {character_name}. {character_description}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )
    story = response.choices[0].text.strip()
    return story
