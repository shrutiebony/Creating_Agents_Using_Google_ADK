# Creating Agents Using Google ADK

This repository contains two complementary tracks for learning and building AI agents with Google's Agent Development Kit (ADK).

## Repository Structure

```
Creating_Agents_Using_Google_ADK/
├── google-adk-codelabs/              # Hands-on Google ADK codelab exercises
└── data-science-multi-agent-system/  # Full multi-agent data science application
```

---

## `google-adk-codelabs`

**Video:** https://youtu.be/Mb3cJ-TYzhA

Hands-on exercises based on official Google Codelabs. Work through these in order to build foundational ADK skills, from a first agent to tool use and MCP integration.

| Subfolder | Codelab | What you learn |
|-----------|---------|----------------|
| `From_Prototypes_to_Agents_with_ADK_renovation-agent` | [From Prototypes to Agents with ADK](https://codelabs.developers.google.com/your-first-agent-with-adk#5) | Turn prompt-based prototypes into a structured agent pipeline (renovation proposal agent) |
| `AI_Agents_with ADK_ Empowering_with_Tools` | [Building AI Agents with ADK: Empowering with Tools](https://codelabs.developers.google.com/devsite/codelabs/build-agents-with-adk-empowering-with-tools#5) | Extend agents with tools — APIs, databases, and custom functions |
| `Travel_Agent_using_MCP_Toolbox_for_Databases_and_Agent_Development_Kit_(ADK)` | [Build a Travel Agent using MCP Toolbox & ADK](https://codelabs.developers.google.com/travel-agent-mcp-toolbox-adk#0) | Combine ADK with the Model Context Protocol (MCP) Toolbox for Databases |

**Learning path:** basic agent structure → tool integration → real-world MCP + database workflows.

See [`google-adk-codelabs/README.md`](google-adk-codelabs/README.md) for setup details and links.

---

## `data-science-multi-agent-system`

**Video:** https://youtu.be/qVPYvlxUCUs

A production-style multi-agent system for end-to-end data science workflows. Six specialized agents collaborate under a root orchestrator to handle analysis, modeling, visualization, engineering, and deployment.

| Agent | Role |
|-------|------|
| Data Science Orchestrator | Coordinates tasks and synthesizes results across agents |
| Data Analyst | EDA, statistics, data quality, feature suggestions |
| Machine Learning Engineer | Model selection, training, tuning, evaluation |
| Visualization Specialist | Charts, dashboards, performance plots |
| Data Engineer | ETL pipelines, transformations, large datasets |
| Deployment Engineer | Model APIs, Docker, serving infrastructure |

**Key capabilities:**
- Predefined workflows (EDA, ML modeling, time series, deployment)
- Streamlit web UI for chat and workflow management
- Local execution via Ollama (`qwen2.5:7b`)
- YAML-based configuration and Docker support

**Quick start:**

```bash
cd data-science-multi-agent-system
pip install -r requirements.txt
python run_ui.py
```

See [`data-science-multi-agent-system/README.md`](data-science-multi-agent-system/README.md) for full documentation, architecture, and examples.

---

## How the two tracks relate

| | `google-adk-codelabs` | `data-science-multi-agent-system` |
|---|---|---|
| **Purpose** | Learn ADK fundamentals step by step | Apply ADK to a complex, real-world domain |
| **Scope** | Three focused codelab projects | Six-agent orchestrated platform with UI |
| **Best for** | Getting started with ADK | Exploring multi-agent architecture and workflows |
| **Prerequisites** | Google API key / Vertex AI setup per codelab | Ollama + Python 3.8+ |

Start with `google-adk-codelabs` to learn core ADK concepts, then explore `data-science-multi-agent-system` to see how those concepts scale into a full multi-agent application.
