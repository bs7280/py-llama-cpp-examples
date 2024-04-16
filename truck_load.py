from llama_cpp.llama import Llama, LlamaGrammar
import json

# grammar = LlamaGrammar.from_string(grammar_text)

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "JSON from truck load",
    "description": "JSON from truck load",
    "type": "object",
    "properties": {
        "origin_city": {
            "type": "string",
            "description": "What is the origin city name of this message?",
        },
        "origin_state": {
            "type": "string",
            "description": "What is the origin statecode for this message?",
        },
        "destination_city": {
            "type": "string",
            "description": "What is the destination city name of this message?",
        },
        "destination_state": {
            "type": "string",
            "description": "What is the destination statecode for this message?",
        },
        "equipment": {
            "type": "string",
            "enum": ["Van", "Reefer", "Flatbed"],
            "description": "What is the type of message often Van, Reefer, or Flatbed?",
        },
        "weight": {
            "type": "number",
            "description": "Get the weight as a number from this message",
        },
        "weight_unit": {"type": "string"},
        "hot": {
            "type": "boolean",
            "default": False,
            "description": "True or False Does this have the message HOT in it?",
        },
        "team": {
            "type": "boolean",
            "default": False,
            "description": "True or False Does this have the message TEAM in it?",
        },
        "latefee": {
            "type": "number",
            "default": 0,
            "description": "What is the dollar amount fee if a load is late? If not present return with 0",
        },
        "dropoff_time": {
            "type": "string",
            "default": "",
            "description": "What is the HH:MM dropoff time if it exists? If not present return with empty str",
        },
    },
    "required": [
        "origin_city",
        "origin_state",
        "destination_city",
        "destination_state",
        "equipment",
    ],
}

schema = json.dumps(schema)

grammar = LlamaGrammar.from_json_schema(schema)
llm = Llama("mistral-7b-instruct-v0.1.Q4_K_M.gguf")

prompt = "Truck load picking up in Chicago,IL Dropping off in Columbus, Ohio at 8:00 AM"

response = llm(prompt, grammar=grammar, max_tokens=-1)

print(f"Prompt: \n**{prompt}**")
print("Json Schema:")
print("```")
print(json.dumps(json.loads(schema), indent=4))
print("```")
print("-------------------")
print("Response:")
print("```")
print(json.dumps(json.loads(response["choices"][0]["text"]), indent=4))
print("```")
