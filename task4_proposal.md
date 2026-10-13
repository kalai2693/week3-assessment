# Technical Proposal: AI Q&A for 60-Page Contracts

**Prepared by:** [Your Name], Yoho Technologies | **Date:** [today's date]

## 1. Problem
Staff spend a lot of time searching long contracts (60+ pages) to answer questions
such as "What is the notice period?" or "Who pays for late delivery?". Manual search
is slow, and people miss clauses.

## 2. Recommended Approach: RAG (Retrieval-Augmented Generation)
1. **Ingest:** extract the text from the contract PDF (use OCR if it is scanned).
2. **Chunk:** split the text into small pieces (about 300-500 words) and keep the page number for each.
3. **Embed and store:** convert each chunk into an embedding and save it in a vector store.
4. **Retrieve:** for each question, embed the question and fetch the top 3-5 most similar chunks (cosine similarity).
5. **Generate:** send only those chunks to the LLM with the instruction "Answer only from this text. Cite the page. If the answer is not in the text, say I don't know."
6. **Show:** display the answer with page citations so the user can verify it.

The LLM is used at temperature 0 for consistent answers.

## 3. Data Requirements
- The contract PDFs (text-based, or scanned with OCR)
- 30-50 real questions with correct answers and page numbers, written by the legal team (the test set)
- Access rules: only authorised staff can see each contract
- Contracts must be stored securely (no public chatbots)

## 4. Evaluation Metric and Target
| Metric | Target |
|---|---|
| Answer accuracy on the 30-50 question test set (checked by a legal reviewer) | at least 90% |
| Citation accuracy (cited page really contains the answer) | at least 95% |
| Unsupported or invented answers | below 2% |
| Response time | under 5 seconds |

## 5. Estimated Build Time: about 3 weeks
| Week | Work |
|---|---|
| 1 | PDF ingestion, chunking, embeddings, retrieval |
| 2 | LLM prompt, citations, "I don't know" behaviour |
| 3 | Testing against the question set, simple UI, fixes |

## 6. Key Trade-offs
- **Accuracy vs cost:** a larger LLM is more accurate but costs more per question.
- **Chunk size:** small chunks give precise answers but may lose context; large chunks keep context but add noise and cost.
- **Speed vs quality:** retrieving more chunks improves answers but is slower and costs more tokens.
- **Hallucination risk:** reduced by citations and "I don't know", but not zero, so a human reviews high-value decisions.
- **Privacy:** using a private or enterprise LLM setup is safer than pasting contracts into a public chatbot, but it costs more to set up.

## 7. Human Review and Limits
The system supports staff and does **not** give final legal advice. A lawyer reviews any answer used for a legal or high-value decision.