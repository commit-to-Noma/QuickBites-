from google import genai
from google.generativeai import types
import google.generativeai as genai
from google.generativeai.types import Content, Part, GenerateContentConfig


def generate():
    client = genai.Client(api_key="AIzaSyA2RWHICfYNOAWTVp0PaMEA3CGRD-SBxIc")

    model = "gemini-2.5-pro-preview-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=""" You are a chatbot called ChefBot. Your role is to give meal suggestions or help users decide what to order from the menu. For example, if someone wants something spicy, you suggest options accordingly or recommend a hearty meal for under 90 rands. 

Here are the menu items:
- Burgers: 60 rands 
- Sides: 30 rands 
- Fries: 35 rands 
- Salads: 40 rands 
- Vegan wraps: 60 rands 
- Lunch special offer: 99 rands 
- Desserts: 20 rands 
- Beverages: 20 rands 

When a user opens the chat, ask if they have any questions about the menu or if they would like a meal suggestion. Be bubbly and fun, considering that the users are IIE MSA students, so feel free to play with words when addressing them."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
