# Py Llamacpp examples 
Repo to store examples of using local LLMs 

## Setup
Will depend on machine, everything is running on my m1 max with 64 GB of Ram

Useful links: 
- Setup: [MacOS Install with Metal GPU - llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/install/macos/)
- Inspiration: [Using llama-cpp-python grammars to generate JSON | Simon Willison’s TILs](https://til.simonwillison.net/llms/llama-cpp-python-grammars)

## Models:
- For the most part Im using the quantized versions of llms from the bloke: [TheBloke/Mistral-7B-Instruct-v0.1-GGUF · Hugging Face](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)


## Usage:

- minstral_json_schema.py - Demonstrates using a 7B model to generate valid output for a given JsonSchema. Couple things to note
    - output should always match json schema given
    - the given Json Schema **Does NOT** count towards the context limit.
    - Using a 7B model which is pretty fast on my machine.
