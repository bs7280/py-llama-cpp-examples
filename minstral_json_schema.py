from llama_cpp.llama import Llama, LlamaGrammar
import json

if False:
    import httpx
    try:
        1 / 0 
        grammar_text = httpx.get("https://raw.githubusercontent.com/ggerganov/llama.cpp/master/grammars/json_arr.gbnf").text
    except:
        grammar_text = '# This is the same as json.gbnf but we restrict whitespaces at the end of the root array\n# Useful for generating JSON arrays\n\nroot   ::= arr\nvalue  ::= object | array | string | number | ("true" | "false" | "null") ws\n\narr  ::=\n  "[\\n" ws (\n            value\n    (",\\n" ws value)*\n  )? "]"\n\nobject ::=\n  "{" ws (\n            string ":" ws value\n    ("," ws string ":" ws value)*\n  )? "}" ws\n\narray  ::=\n  "[" ws (\n            value\n    ("," ws value)*\n  )? "]" ws\n\nstring ::=\n  "\\"" (\n    [^"\\\\] |\n    "\\\\" (["\\\\/bfnrt] | "u" [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F]) # escapes\n  )* "\\"" ws\n\nnumber ::= ("-"? ([0-9] | [1-9] [0-9]*)) ("." [0-9]+)? ([eE] [-+]? [0-9]+)? ws\n\n# Optional space: by convention, applied in this grammar after literal chars when allowed\nws ::= ([ \\t\\n] ws)?\n'

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

response = llm(
    "Give me an API spec for a 28 year old named Ben",
    grammar=grammar, max_tokens=-1
)

print(json.dumps(json.loads(response['choices'][0]['text']), indent=4))


