# 3-Minute Pitch: Contract Q&A

## Opening (20 seconds)
"Good morning. Your team spends hours searching 60-page contracts for simple
answers like the notice period or the penalty clause. I propose an AI assistant
that answers these questions in seconds, and shows the exact page, so people
can verify it."

## How it works (60 seconds)
"We use an approach called RAG. First, we split the contract into small pieces
and convert each piece into an embedding, which captures its meaning. When
someone asks a question, we find the 3 to 5 most relevant pieces using cosine
similarity. Then we send only those pieces to the language model and tell it:
answer only from this text, cite the page, and say 'I don't know' if the answer
is not there. The user sees the answer and the page number."

## Data and success target (40 seconds)
"We need the contract PDFs and 30 to 50 real questions with correct answers
from your legal team. We will test against these. Our targets are: at least 90%
correct answers, at least 95% correct page citations, and fewer than 2%
invented answers."

## Time and trade-offs (30 seconds)
"Build time is about 3 weeks. The main trade-offs are cost versus accuracy,
and speed versus quality. Hallucination can be reduced but not removed, so a
lawyer still reviews any high-value decision. The assistant supports your team
and does not replace legal advice."

## Close (10 seconds)
"I recommend a 3-week pilot on 5 contracts, measured against your question
set. Thank you. Happy to take questions."

---

# Q: "Why not just ask ChatGPT?"

**Short answer (30 seconds):**
"You can, for casual use. But for contracts, a public chatbot has five problems:

1. **Confidentiality:** pasting a client contract into a public tool may break
   confidentiality or company policy. Our system keeps data in a controlled setup.
2. **Hallucination:** ChatGPT can confidently invent a clause that does not
   exist. We saw this in our own test, where a model invented a full winner,
   score and prize for an event that never happened. Our system answers only
   from the contract and says 'I don't know' otherwise.
3. **No citations:** a plain answer has no page reference, so nobody can check it.
   Ours always shows the page.
4. **No measurement:** we cannot prove ChatGPT is 90% accurate on your contracts.
   We test our system against your questions and report the score.
5. **Scale and control:** a 60-page contract may not fit well in one prompt,
   and there is no access control, audit trail or cost control. RAG sends only
   the relevant pieces, which is cheaper and gives access control."

**One-line version:** "ChatGPT gives an answer. Our system gives an answer you can verify, on data you control, with a measured accuracy."