from sentence_transformers import SentenceTransformer, util
import os

MODEL_NAME = os.getenv("SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2")
model = SentenceTransformer(MODEL_NAME)

INTENTS = {
    "general_query": "Answer factual questions, clarifications and explanations",
    "task_planning": "Create step-by-step plans, roadmaps and milestones",
    "data_query": "Help with databases, SQL, analytics and data queries",
    "integration": "Integrate services like Jira, Slack, Gmail and webhooks"
}

# Precompute embeddings at module load
intent_embeddings = {k: model.encode(v, normalize_embeddings=True) for k, v in INTENTS.items()}

def route_intent(prompt: str):
    q_emb = model.encode(prompt, normalize_embeddings=True)
    scores = {k: float(util.cos_sim(q_emb, emb)) for k, emb in intent_embeddings.items()}
    best_intent = max(scores, key=scores.get)
    confidence = scores[best_intent]
    return best_intent, float(confidence), scores
