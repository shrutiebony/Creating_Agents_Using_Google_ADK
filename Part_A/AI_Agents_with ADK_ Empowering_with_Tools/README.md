# AI Proposal Architect with ADK


---

## Project Overview

This repository showcases the **“AI Proposal Architect with ADK”** — a practical guide to evolving a **prompt-based prototype** into a **fully autonomous AI agent** using the **Vertex AI Agent Development Kit (ADK)**.

The agent intelligently generates and stores a **Kitchen Renovation Proposal Document** in **Google Cloud Storage (GCS)**.  
It demonstrates agent orchestration, tool integration, and task automation using **Gemini models**.

---

## Key Outcomes

By completing this project, you’ll learn how to:

1) Configure a **goal-driven AI agent** using the Vertex AI ADK.  
2) Build a **structured Python project** (`agent.py`, `.env`, `requirements.txt`).  
3) Integrate **GCS tools** for file creation and data persistence.  
4) Implement a **root agent** that autonomously completes user-defined tasks.  
5) Run and test agents in **Google Cloud Shell** or local environments.  

---

## Prerequisites

Before starting, ensure you have:

| Requirement                 | Description                               |
| 1) **Google Cloud Project** | Billing enabled and APIs activated        |
| 2) **Google Cloud Shell**   | Recommended for consistent environment    |
| 3) **Vertex AI API**        | Must be enabled in your GCP project       |
| 4) **GCS Bucket**           | Destination for proposal document storage |

---

## Setup & Installation

### Create Virtual Environment
```bash
# Create a root directory for agentic apps
mkdir agentic-apps && cd agentic-apps

# Create your project folder
mkdir kitchen-design-agent && cd kitchen-design-agent

# Create and activate Python virtual environment
python -m venv .venv
source .venv/bin/activate
```

---

### Install ADK & Dependencies

```bash
# Install Vertex AI Agent Development Kit (ADK)
pip install google-adk

# (Optional) Install additional dependencies
# pip install -r requirements.txt
```

---

###  Configure Environment Variables

Create a `.env` file in your project root (`kitchen-design-agent/`).

<details>
<summary> Example .env file</summary>

```bash
# --- Google Cloud Configuration ---
PROJECT_ID="your-gcp-project-id"

# --- Agent / Model Configuration ---
MODEL_NAME="gemini-2.5-flash"

# --- Tool Configuration (GCS Storage Tool) ---
GCS_BUCKET_NAME="your-proposal-storage-bucket"
```

</details>

> **Tip:** Grant your service account the `Storage Object Creator` role
> so the agent can upload files to your specified bucket.

---

---

## 🔁 Execution Flow

```mermaid
sequenceDiagram
  autonumber
  participant U as User
  participant A as ADK Agent
  participant M as Gemini Model
  participant T as GCS Writer Tool
  participant B as GCS Bucket

  U->>A: Generate renovation proposal
  A->>M: Plan and draft proposal
  M-->>A: Structured proposal text
  A->>T: save_file(path, bytes)
  T->>B: Upload to bucket
  B-->>T: Return object URL
  T-->>A: Success + URL
  A-->>U: Respond with GCS file link

---

## 🪄 Example Use Case

**User:**

> “Generate a modern kitchen renovation proposal for a 12x10 ft space with minimalist design.”

**Agent:**

> “Done! I’ve created your Kitchen Renovation Proposal and stored it at:
> `gs://your-proposal-storage-bucket/kitchen-proposal.pdf`”

---



