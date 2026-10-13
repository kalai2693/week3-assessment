### Model results (80/20 split, 9 test tickets)

| Model | Accuracy | Macro F1 |
|---|---|---|
| Baseline (always most common) | 0.33 | 0.17 |
| TF-IDF + Logistic Regression | 0.89 | 0.89 |

Confusion matrix (rows = true, columns = predicted; order: Account, Billing, Technical)

Baseline:
[[3 0 0]
 [3 0 0]
 [3 0 0]]

Model:
[[3 0 0]
 [0 3 0]
 [1 0 2]]

The model is much better than the baseline. The test set is small (9 tickets),
so one mistake changes the score a lot.

### Misclassified tickets
1. "page is loading very slowly on my browser" (true: Technical, predicted: Account).
   Reason: it has no strong technical keywords like "error" or "crash", and
   with so little training data the model had few words to learn from.
2. "please explain the extra charge on my statement" (true: Billing, predicted: Account).
   Reason: the words "explain", "extra" and "statement" also appear in
   account-type tickets, and it has no strong billing words like "invoice",
   "refund" or "payment", so the model got confused.
3. "i did not receive the verification email for sign up" (true: Account, predicted: Billing).
   Reason: the word "email" appears in billing tickets such as "send me the
   invoice", and the strong Account words ("password", "login") are missing.
   Words shared between categories mislead TF-IDF.

### KMeans (no labels)
1. The clusters do not match the real categories well: clusters 0 and 2 each
   contain a mix of Account, Billing and Technical tickets.
2. Only cluster 1 is fairly clean (5 of 6 tickets are Technical), so Technical
   was the easiest group to find without labels.
3. KMeans only groups by word similarity and never sees the labels, while the
   supervised model learns from labels, so the model is much more accurate.
   Overall, cross-validation found 10 errors out of 41 tickets (about 76% accuracy).
Mistakes happen mostly when a ticket is short or shares words with another category.