import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_predict

df = pd.read_csv("tickets_clean.csv")

pipe = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))
pred = cross_val_predict(pipe, df["text"], df["category"], cv=5)

errors = pd.DataFrame({"text": df["text"], "true": df["category"], "predicted": pred})
errors = errors[errors["true"] != errors["predicted"]]
print("Total errors:", len(errors), "out of", len(df))
print(errors.head(5).to_string())