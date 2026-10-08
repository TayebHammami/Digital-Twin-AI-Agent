import os
import requests
import gradio as gr
from dotenv import load_dotenv

from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES

load_dotenv(override=True)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "inclusionai/ling-3.0-flash-sante:free"

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is missing from your .env file.")

SYSTEM_MESSAGES = [
    {
        "role": "system",
        "content": TWIN_SYSTEM_PROMPT,
    }
]


def chat(message, history):
    # Keep the latest complete exchange instead of sending an ever-growing history.
    messages = (
        SYSTEM_MESSAGES
        + history[-1:]
        + [{"role": "user", "content": message}]
    )

    max_tool_rounds = 5

    for _ in range(max_tool_rounds):
        response = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": messages,
                "tools": tools,
            },
            timeout=60,
        )

        response.raise_for_status()
        data = response.json()

        choice = data["choices"][0]
        assistant_message = choice["message"]

        messages.append(assistant_message)

        if choice.get("finish_reason") != "tool_calls":
            return assistant_message.get("content", "")

        tool_calls = assistant_message.get("tool_calls", [])
        if not tool_calls:
            return "I couldn't complete the tool call."

        tool_results = handle_tool_calls(tool_calls)
        messages.extend(tool_results)

    return "I stopped because the tool-call loop reached its safety limit."


chatbot = gr.Chatbot(
    show_label=False,
    elem_id="twin-chatbot",
    height="100%",
)

textbox = gr.Textbox(
    placeholder="Ask me about my background, projects, skills, or contact...",
    show_label=False,
    container=False,
    elem_id="twin-input",
    lines=1,
    max_lines=6,
)

demo = gr.ChatInterface(
    fn=chat,
    chatbot=chatbot,
    textbox=textbox,
    examples=EXAMPLES,
    title="Digital Twin",
    description=(
        "Talk to my AI twin about my career, projects, and technical experience. "
        "Interested in connecting? Interested in working together or discussing an opportunity? "
        "Share your name, email, and what you'd like to discuss, and I'll be notified."

    ),)


 
if __name__ == "__main__":
    demo.launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )
