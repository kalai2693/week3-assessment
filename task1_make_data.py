import pandas as pd

billing = [
 "I was charged twice for my monthly subscription", "Please send me the invoice for last month",
 "My refund has not arrived yet", "The amount on my bill is higher than expected",
 "How do I update my credit card for payment", "I want to cancel auto renewal and get a refund",
 "Payment failed but money was deducted from my bank", "Can I get a GST invoice for my purchase",
 "Why was I charged a late fee on my bill", "Discount code was not applied at checkout payment",
 "I need a receipt for my last payment", "Billing cycle date needs to be changed",
 "I was overcharged on my invoice this month", "Please explain the extra charge on my statement"]
technical = [
 "The app crashes every time I open it", "Website shows error 500 when I upload a file",
 "Page is loading very slowly on my browser", "The mobile app freezes on the home screen",
 "I get a timeout error when syncing data", "Video call keeps disconnecting with connection error",
 "The export to PDF feature is not working", "Notifications are not showing up on my phone",
 "Software update fails with installation error", "The search bar returns an error message",
 "Dashboard does not load after the latest update", "Bluetooth device will not connect to the app",
 "Screen goes blank when I click the save button"]
account = [
 "I forgot my password and need to reset it", "How do I change my email address on my profile",
 "Please delete my account permanently", "I cannot log in to my account",
 "My account is locked after too many attempts", "I want to update my phone number on my account",
 "How can I enable two factor authentication", "Please merge my two accounts into one",
 "I did not receive the verification email for sign up", "Change the name on my profile",
 "Need to add a new user to my team account", "My username is showing incorrectly",
 "How do I deactivate my account temporarily"]

rows = [(t, "Billing") for t in billing] + [(t, "Technical") for t in technical] + [(t, "Account") for t in account]
df = pd.DataFrame(rows, columns=["text", "category"])

# 5 duplicates (same ticket, different casing / extra spaces)
dups = df.sample(5, random_state=1).copy()
dups["text"] = [t.upper() if i % 2 else t + "  " for i, t in enumerate(dups["text"])]
dups["category"] = dups["category"].str.upper()

# 5 missing values
missing = pd.DataFrame({
    "text": ["My invoice looks wrong", None, "app not working", None, "need help with login"],
    "category": [None, "Billing", None, "Technical", "Account"]})

raw = pd.concat([df, dups, missing]).sample(frac=1, random_state=7).reset_index(drop=True)

# inconsistent casing
i = raw.sample(10, random_state=3).index
raw.loc[i, "category"] = raw.loc[i, "category"].str.lower()
j = raw.sample(8, random_state=5).index
raw.loc[j, "text"] = raw.loc[j, "text"].str.upper()

raw.to_csv("tickets_raw.csv", index=False)
print(len(raw), "rows written")