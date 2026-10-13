import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
MODEL = "openai/gpt-oss-120b"


def ask(prompt, temperature):
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=2000,
        reasoning_effort="low",
    )
    text = r.choices[0].message.content
    return text.strip() if text else "(empty answer)"


# ---- Temperature ----
prompt = "Suggest one creative name for a coffee shop. Reply with only the name."
for temp in [0, 1.0]:
    print(f"\n=== Temperature {temp} ===")
    answers = []
    for i in range(5):
        a = ask(prompt, temp)
        answers.append(a)
        print(f"Run {i + 1}: {a}")
    print("Unique answers:", len(set(answers)), "out of 5")

# ---- Hallucination ----
fake = "Who won the 2019 Chennai Quantum Chess Championship and what was the final score?"
print("\n=== Made-up question, plain ===")
print(ask(fake, 0))

print("\n=== Made-up question, with 'say I don't know if unsure' ===")
print(ask(fake + " If you are unsure, say I don't know.", 0))