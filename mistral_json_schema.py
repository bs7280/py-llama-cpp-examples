from llama_cpp.llama import Llama, LlamaGrammar
import json

#grammar = LlamaGrammar.from_string(grammar_text)

schema = '''
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Name and Age API",
    "description": "An API that accepts a name and age as input parameters.",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the person."
        },
        "age": {
            "type": "integer",
            "description": "The age of the person."
        }
    },
    "required": ["name", "age"]
}'''

grammar = LlamaGrammar.from_json_schema(schema)
llm = Llama("mistral-7b-instruct-v0.1.Q4_K_M.gguf")

prompt = "Give me an API spec for a 28 year old named Ben"

response = llm(
    prompt,
    grammar=grammar, max_tokens=-1
)

print(f"Prompt: \n**{prompt}**")
print("Json Schema:")
print('```')
print(json.dumps(json.loads(schema), indent=4))
print('```')
print("-------------------")
print("Response:")
print('```')
print(json.dumps(json.loads(response['choices'][0]['text']), indent=4))
print('```')


