#!/usr/bin/env python3
"""
🧠 Task 1: Embeddings - Teaching Computers to Understand Meaning
"""

import os
from sentence_transformers import SentenceTransformer, util

def main():
    # TODO 1: Initialize model that converts text → meaningful numbers
    # Replace ___ with: "all-MiniLM-L6-v2"
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Scenario: User searching documentation
    query = "which day i need to come to office and which day i can work from home"

    docs = [
        "Password recovery: Use the 'Reset Password' link on login page and go to first page where is it is written Dhiraj notes",
        "Vacation policy: Request time off 2 weeks in advance only Monday and Friday requests accepted",
        "Account security: Enable two-factor authentication",
        "Login help: Contact IT if you cannot access your account"
    ]

    # TODO 2: Convert query and docs to embeddings
    # Replace ___ with: model.encode(query)
    query_emb =  model.encode(query)
    # Replace ___ with: model.encode(docs)
    doc_embs = model.encode(docs)

    # TODO 3: Find semantic matches
    # Replace ___ with: util.cos_sim(query_emb, doc_embs)[0]
    scores = util.cos_sim(query_emb, doc_embs)[0]

    print(f"Query: '{query}'\n")
    print("Results (score > 0.3 = relevant):")
    for doc, score in zip(docs, scores):
        marker = "✅" if score > 0.3 else "  "
        print(f"{marker} [{score:.2f}] {doc}")

    print("\n💡 Notice: Found 'Password recovery' and 'Login help'")
    print("   Even though query didn't contain those exact words!")

if __name__ == "__main__":
    main()