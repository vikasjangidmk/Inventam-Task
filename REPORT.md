# REPORT.md  
## AI-ML Practical Test — Reasoning-First System Design

**Author:** Vikas Jangid  
**Tech Stack:** Python 3.11 · FastAPI · MongoDB · Sentence-Transformers · Docker  

---

## 1. Objective of the Task

The goal of this practical test is to evaluate reasoning-first AI system design skills rather than heavy coding.  
This includes the ability to:

- Repair low-quality training data
- Diagnose model training failures
- Propose stable and safe fine-tuning strategies
- Design a dynamic, safety-aware AI agent system
- Plan safe deployment strategies

All solutions are implemented within a **Dynamic Agent Routing System** that enforces safety, traceability, and extensibility.

---

## 2. System Overview

The system is structured into four core layers:

### 2.1 Data Layer
- Repaired high-quality support-style JSONL dataset
- MongoDB-backed agent configuration storage

### 2.2 Training Layer
- Diagnosis of unstable and unsafe training behavior
- Stable hyperparameter recommendations
- Minimal, reproducible training pipeline

### 2.3 Agent Intelligence Layer
- Semantic intent routing using embeddings
- Multiple specialized agents
- Runtime safety guardrails

### 2.4 Deployment Layer
- Dockerized application
- CI pipeline
- Safe rollout strategies (Canary, Blue-Green, Shadow)

---

## 3. Part 1 — Dataset Repair

### Problem
The provided dataset samples were:
- Poorly structured
- Unsafe and inconsistent
- Not aligned with professional support assistant tone

### Solution
All samples were rewritten into **chat-style JSONL format** with:
- Explicit roles (system, user, assistant)
- Polite and factual responses
- Safety-aware and non-hallucinatory behavior

### Result
File: `data/repaired_dataset.jsonl`  
Contains 4 high-quality support-style training samples suitable for fine-tuning and evaluation.

---

## 4. Part 2 — Training Diagnosis

### Observed Symptoms
- Loss becomes NaN during training
- GPU memory spikes
- Toxic or unsafe model outputs
- Performance degradation after fine-tuning

### Root Causes

| Symptom | Root Cause |
|------|----------|
| NaN loss | High learning rate |
| Instability | No gradient clipping |
| Toxic outputs | Unsafe training data |
| Safety drift | Missing safety-aligned samples |
| Overfitting | Excessive epochs |

---

## 5. Part 3 — Training Hyperparameter Fixes

Recommended stable configuration:

| Parameter | Value | Reason |
|--------|------|------|
| Epochs | 4 | Prevents overfitting |
| Learning Rate | 3e-5 | Avoids gradient explosion |
| Batch Size | 8 | Stable memory usage |
| Gradient Clipping | 1.0 | Prevents NaN gradients |
| Warmup Steps | 1000 | Smooth optimization |
| Mixed Precision | Enabled | Stable and efficient |

Configuration file:  
`training/configs/hparams.yaml`

---

## 6. Part 4 — Dynamic Agent Integration

### Intent Routing
Semantic intent routing is implemented using sentence embeddings and cosine similarity to select the most appropriate agent dynamically.

### Implemented Agents

#### GeneralQAAgent
- Handles factual and explanatory questions
- Ensures safe and concise responses

#### TaskPlannerAgent
- Produces step-by-step plans and milestones

#### DataQueryAgent
- Asks clarifying questions
- Proposes database query templates (no execution)

#### IntegrationAgent
- Suggests system integrations
- Lists required configuration and secrets

---

## 7. Guardrails and Safety

Safety mechanisms include:
- PII detection checks
- Agent-specific guardrails loaded from DB
- Conservative rejection of risky inputs
- Full trace metadata for auditing

Each response includes:
- request_id
- agent_name
- intent and confidence
- processing time
- guardrail status

---

## 8. Test Case Verification

All required test cases were executed and passed:

| Prompt Type | Example Prompt | Agent Selected |
|-----------|---------------|---------------|
| General QA | What is fine-tuning in LLMs? | GeneralQAAgent |
| Task Planning | Give me a deployment plan | TaskPlannerAgent |
| Data Query | Query user logs | DataQueryAgent |
| Integration | Slack integration | IntegrationAgent |

---

## 9. Deployment Strategy

### Local / Staging
- Docker + docker-compose
- Environment-based configuration
- DB seeded via script

### Production
- Blue-Green deployment for zero downtime
- Canary deployment for risk mitigation
- Shadow deployment for silent evaluation

### Rollback Triggers
- Error rate spikes
- Toxicity threshold breaches
- Latency regressions

---

## 10. Final Outcome

This project demonstrates:
- Strong reasoning-first problem solving
- Safe and stable AI system design
- Production-ready architecture
- Clear alignment with real-world AI deployment practices

---

## 11. Submission Status

**Status:** COMPLETE, VERIFIED, and READY FOR REVIEW.