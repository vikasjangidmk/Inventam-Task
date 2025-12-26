# AI-ML Practical Test  
### Reasoning-First Dynamic Agent System

**Author:** Vikas Jangid  
**Stack:** Python 3.11 · FastAPI · MongoDB · Sentence-Transformers · Docker  

---

## 📌 Project Overview

This repository contains a **production-oriented, reasoning-first AI system** built to evaluate:

- Data quality repair
- Training failure diagnosis
- Safe fine-tuning practices
- Dynamic AI agent orchestration
- Safety-aware deployment strategies

The project intentionally focuses on **decision-making, safety, and system design** rather than heavy model training or prompt engineering.

---

## 🎯 Task Objective

The goal of this task is to demonstrate the ability to:

- Repair low-quality training data
- Diagnose model instability and unsafe behavior
- Recommend stable hyperparameters
- Integrate these concepts into a **Dynamic Agent System**
- Plan safe, real-world AI deployment strategies

This aligns with real-world ML/AI engineering workflows.

---

## 🧠 System Architecture (High-Level)

```
User Prompt
     ↓
Semantic Intent Router (Embeddings)
     ↓
Dynamic Agent Selection
     ↓
Agent Guardrails + Instructions (DB)
     ↓
Structured Response + Trace
```

---

## 🗂️ Repository Structure

```
AI-ML-Practical-Test/
├── agents/                 # Agent logic & routing
├── data/                   # Repaired dataset
├── training/               # Training configs & script
├── docs/                   # Training diagnosis
├── .github/workflows/      # CI pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── REPORT.md               # Detailed task report
├── README.md               # This file
└── .env.example
```

---

## 🔧 Core Components

### 1️⃣ Dataset Repair
- Location: `data/repaired_dataset.jsonl`
- Converted into chat-style JSONL
- Safe, polite, non-hallucinatory support responses

---

### 2️⃣ Training Diagnosis
Identified issues:
- NaN loss
- Gradient instability
- Toxic outputs
- Overfitting

Root causes:
- High learning rate
- Missing gradient clipping
- Unsafe data
- Excessive epochs

---

### 3️⃣ Hyperparameter Fixes
Configured stable training parameters:

| Parameter | Value |
|--------|------|
| Epochs | 4 |
| Learning Rate | 3e-5 |
| Batch Size | 8 |
| Gradient Clipping | 1.0 |
| Warmup Steps | 1000 |
| Mixed Precision | Enabled |

Config file:
```
training/configs/hparams.yaml
```

---

## 🤖 Dynamic Agent System

The system dynamically routes user prompts to specialized agents using semantic similarity.

### Implemented Agents

| Agent | Purpose |
|----|-------|
| GeneralQAAgent | General explanations |
| TaskPlannerAgent | Step-by-step planning |
| DataQueryAgent | Query guidance (no execution) |
| IntegrationAgent | Integration suggestions |

Each agent:
- Loads instructions from DB
- Applies safety guardrails
- Returns structured trace data

---

## 🛡️ Safety & Guardrails

- PII detection
- DB-driven guardrails
- Conservative rejection of risky prompts
- Full request traceability

Every response includes:
- request_id
- agent_name
- intent + confidence
- processing time
- guardrail status

---

## 🧪 Test Case Validation

All required test cases passed successfully:

| Prompt | Expected Agent |
|------|---------------|
| What is fine-tuning in LLMs? | GeneralQAAgent |
| Deployment plan | TaskPlannerAgent |
| User logs query | DataQueryAgent |
| Slack integration | IntegrationAgent |

---

## 🚀 How to Run Locally

### 1️⃣ Setup Environment
```bash
cp .env.example .env
```

### 2️⃣ Run with Docker
```bash
docker compose up --build
```

### 3️⃣ Seed Database
```bash
docker exec -it <app_container> python -m agents.seed_db
```

### 4️⃣ Test API
```bash
curl -X POST http://localhost:8000/run -H "Content-Type: application/json" -d '{"user_prompt":"Create a plan to fix NaN losses"}'
```

---

## 🧩 Deployment Strategy

- **Blue-Green Deployment** → Zero downtime
- **Canary Deployment** → Risk-controlled rollout
- **Shadow Deployment** → Silent evaluation

Rollback triggers:
- Error rate spikes
- Toxicity threshold breaches
- Latency regressions

---

## 📄 Documentation

- Detailed reasoning & explanation → `REPORT.md`
- Training diagnosis → `docs/diagnosis.md`

---

## ✅ Submission Notes

- Secrets are excluded from the repo
- `.env.example` provided for reference
- Placeholder LLM calls can be replaced with production models
- Designed for real-world AI system evaluation

---

## 📌 Status

**✔ Task Completed  
✔ Verified  
✔ Ready for Review**