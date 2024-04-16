from llama_cpp.llama import Llama, LlamaGrammar
import json
from pydantic import BaseModel
from datetime import datetime
import time


def get_grammar(schema: dict):
    schema = json.dumps(schema)
    return LlamaGrammar.from_json_schema(schema)


class MeetingSchedule(BaseModel):
    title: str
    description: str = None
    time: datetime
    timezone: str


# Get JSON of pydantic object
meeting_schema = MeetingSchedule.schema()


grammar = get_grammar(meeting_schema)

llm = Llama("mistral-7b-instruct-v0.1.Q4_K_M.gguf")

st = time.time()

prompt = "Lets catch up about the foobar project tomorrow at 4pm CST"
response = llm(prompt, grammar=grammar, max_tokens=-1)
print(f"Elapsed: {time.time() - st}s Prompt: {prompt}")
print(json.dumps(json.loads(response["choices"][0]["text"]), indent=4))

print("------")

print("------")

st = time.time()

prompt = "Generate a json object for the following meeting: Lets get lunch at Al's Beef tomorrow at lunch"
response = llm(
    prompt=prompt,
    # grammar=grammar,
    max_tokens=-1,
)
print(f"Elapsed: {time.time() - st}s Prompt: {prompt}")
print(response["choices"][0]["text"])
