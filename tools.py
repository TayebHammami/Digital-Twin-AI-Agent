import json
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)


# ============================================================
# Pushover Configuration
# ============================================================

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

pushover_url = "https://api.pushover.net/1/messages.json"


def push(text):
    """Send a push notification through Pushover."""

    response = requests.post(
        pushover_url,
        data={
            "token": pushover_token,
            "user": pushover_user,
            "message": text,
        },
        timeout=10,
    )

    print(
        f"Pushover: {response.status_code} {response.text}",
        flush=True
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# Actual Python Tools
# ============================================================

def record_user_details(
    email,
    name="Name not provided",
    interest="Not provided",
    notes="Not provided",
):
    """Record a visitor's contact information and reason for contacting."""

    push(
        "🔔 New Digital Twin Contact\n\n"
        f"👤 Name: {name}\n"
        f"📧 Email: {email}\n"
        f"🎯 Interested in: {interest}\n"
        f"📝 Notes: {notes}"
    )

    return (
        "Your contact details have been recorded successfully. "
        "Taieb has been notified."
    )



def record_unknown_question(question):
    """Record a question that the AI could not answer."""

    push(
        f"Recording unknown question: {question}"
    )

    return "Unknown question recorded successfully."


# ============================================================
# Tool Schemas
# These are given to the LLM.
# ============================================================

record_user_details_json = {
    "name": "record_user_details",
    "description": (
        "Use this tool when a visitor provides their email and wants "
        "to contact Taieb, discuss a project, explore a job opportunity, "
        "collaborate, discuss research, request freelance work, "
        "or network professionally. "
        "Capture the visitor's name, email, what they are interested in, "
        "and any useful additional context."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The visitor's email address.",
            },
            "name": {
                "type": "string",
                "description": "The visitor's name, if provided.",
            },
            "interest": {
                "type": "string",
                "description": (
                    "What the visitor wants or is interested in. "
                    "For example: a job opportunity, AI project, "
                    "collaboration, freelance work, research, "
                    "or networking."
                ),
            },
            "notes": {
                "type": "string",
                "description": (
                    "Any additional useful context about the visitor's "
                    "request or conversation."
                ),
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}


record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": (
        "ALWAYS use this tool when the answer to the user's question "
        "is not available in your knowledge about Taieb. "
        "Never guess or invent missing personal or professional information. "
        "Record the original unanswered question."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": (
                    "The question that could not be answered."
                ),
            },
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}


# ============================================================
# Tools sent to OpenRouter
# ============================================================

tools = [
    {
        "type": "function",
        "function": record_user_details_json,
    },
    {
        "type": "function",
        "function": record_unknown_question_json,
    },
]


# ============================================================
# Tool Mapping
# Connects LLM tool names → Python functions
# ============================================================

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}


# ============================================================
# Tool Call Handler
# Compatible with requests + response.json()
# ============================================================

def handle_tool_calls(tool_calls):

    results = []

    for tool_call in tool_calls:

        # OpenRouter returns dictionaries because we use
        # requests.post() + response.json()

        tool_name = tool_call["function"]["name"]

        arguments = json.loads(
            tool_call["function"]["arguments"]
        )

        print(
            f"Tool called: {tool_name}",
            flush=True,
        )

        print(
            f"Arguments: {arguments}",
            flush=True,
        )

        # Find the corresponding Python function
        tool = tool_map.get(tool_name)

        if tool is None:

            result = f"Unknown tool: {tool_name}"

        else:

            try:
                result = tool(**arguments)

            except Exception as e:

                print(
                    f"Tool error: {e}",
                    flush=True,
                )

                result = f"Tool execution failed: {str(e)}"

        # Send the result back to the LLM
        results.append(
            {
                "role": "tool",
                "content": str(result),
                "tool_call_id": tool_call["id"],
            }
        )

    return results

