import openai

# Setup OpenAI API
openai.api_base = "http://localhost:4891/v1"
openai.api_key = "none"
model = "none"

# Generate question and answer
prompt = "Who is Stuart Russell?"

response = openai.Completion.create(
    model=model,
    prompt=prompt,
    max_tokens=50,
    temperature=0.28,
    top_p=0.95,
    n=1,
    echo=True,
    stream=False
)

# Print the generated completion to Terminal
print(response)