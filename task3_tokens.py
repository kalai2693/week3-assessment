import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

texts = {
    "Short English": "How do I reset my password?",
    "Long English": "Our company provides support for billing, technical and account issues. "
                    "Customers can raise a ticket through the website or the mobile app, and "
                    "our team responds within one working day.",
    "Code": "def add(a, b):\n    return a + b\nprint(add(2, 3))",
    "Tamil": "எனது கடவுச்சொல்லை எப்படி மாற்றுவது?",
}

print("Text | Words | Tokens | Words per token")
for name, text in texts.items():
    words = len(text.split())
    tokens = len(enc.encode(text))
    print(f"{name} | {words} | {tokens} | {words / tokens:.2f}")

# Monthly cost estimate
chats_per_day = 300
input_tokens = 1200
output_tokens = 300
days = 30

# CHANGE THESE to the prices your trainer gave you (per 1 million tokens)
input_price_per_million = 0.15
output_price_per_million = 0.60

total_input = chats_per_day * days * input_tokens
total_output = chats_per_day * days * output_tokens
cost = (total_input / 1_000_000) * input_price_per_million + \
       (total_output / 1_000_000) * output_price_per_million

print()
print("Total input tokens per month:", total_input)
print("Total output tokens per month:", total_output)
print(f"Monthly cost: ${cost:.2f}")