import ollama
def generate_query_with_ollama(screen_name, user_input, matched_fields):
    field_names = [f["key"] for f in matched_fields]

    prompt = f"""
You are a query generator. 
Screen: {screen_name}
User command: "{user_input}"
Available fields: {field_names}

Generate a JSON filter for the API in this format:
{{
  "limit": 20,
  "page": 1,
  "criteria": [
    {{"key": "Status", "value": ["Active"], "type": "in"}}
  ],
  "sortfield": "Key",
  "direction": "desc"
}}
Only include fields found in user command.
"""

    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    try:
        return response['message']['content']
    except Exception:
        return {"error": "Failed to parse Ollama response"}
