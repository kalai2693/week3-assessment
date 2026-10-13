# Week 3 Assessment

## How to run
- Task 1: `python task1_make_data.py`, then `task1_audit.py`, then `task1_model.py`
- Task 2: `python task2_search.py`
- Task 3: `python task3_tokens.py` and `python task3_llm.py` (needs GROQ_API_KEY in .env)
- Task 4: see `task4_decision_table.md`, `task4_proposal.md`, `task4_pitch.md`

---

## Task 1: Data audit and model evaluation

| | Before | After |
|---|---|---|
| Rows | 50 | 41 |
| Missing text | 4.0% (2 rows) | 0 |
| Missing category | 4.0% (2 rows) | 0 |
| Duplicates | 0 exact, about 5 after fixing casing | 0 |
| Category labels | 9 spellings (Billing, billing, BILLING, ...) | 3 (Account, Billing, Technical) |
| Category balance | Billing 17, Account 16, Technical 15 (mixed casing) | Billing 14, Account 14, Technical 13 |

Rows 50 -> 41 after cleaning. Casing was fixed first, then rows with missing values and duplicates were removed. The classes are well balanced, so a baseline that always predicts the most common class gets only about one third accuracy.
(Run `python task1_audit.py` and paste the output here)
Submitted by: kalaiarasan