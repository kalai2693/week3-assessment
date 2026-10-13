import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

# 1. Load the clean data
df = pd.read_csv("tickets_clean.csv")
labels = sorted(df["category"].unique())

# 2. Split 80% train, 20% test
X_train_text, X_test_text, y_train, y_test = train_test_split(
    df["text"], df["category"],
    test_size=0.2, stratify=df["category"], random_state=42)

# 3. Convert text to numbers (TF-IDF)
tfidf = TfidfVectorizer()
X_train = tfidf.fit_transform(X_train_text)
X_test = tfidf.transform(X_test_text)

# 4. Baseline (always predicts the most common category) and the real model
baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)

# 5. Report results for both
for name, m in [("Baseline", baseline), ("Model", model)]:
    pred = m.predict(X_test)
    print("=====", name, "=====")
    print("Accuracy:", round(accuracy_score(y_test, pred), 2))
    print("Macro F1:", round(f1_score(y_test, pred, average="macro"), 2))
    print("Confusion matrix (rows=true, columns=predicted):", labels)
    print(confusion_matrix(y_test, pred, labels=labels))
    print()

# 6. Misclassified tickets
pred = model.predict(X_test)
errors = pd.DataFrame({"text": X_test_text, "true": y_test, "predicted": pred})
errors = errors[errors["true"] != errors["predicted"]]
print("===== Misclassified tickets =====")
print(errors.to_string())
print()

# 7. KMeans (no labels used)
X_all = tfidf.fit_transform(df["text"])
df["cluster"] = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X_all)
print("===== KMeans clusters vs real categories =====")
print(pd.crosstab(df["cluster"], df["category"]))