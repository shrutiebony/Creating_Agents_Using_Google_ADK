# Data Science Agentic System
Video Link: https://youtu.be/qVPYvlxUCUs


A powerful multi-agent system for comprehensive data science workflows using Google ADK and Ollama.

## 🌟 Features

- **Multi-Agent Architecture**: Specialized agents for different data science tasks
- **Workflow Management**: Predefined and custom pipelines
- **Comprehensive Coverage**: EDA, ML modeling, visualization, deployment
- **Local Execution**: Uses Ollama for privacy and offline capabilities
- **Extensible**: Easy to add new agents and workflows

## 🤖 Agents

### 1. **Data Science Orchestrator** (Root Agent)
- Coordinates all specialist agents
- Breaks down complex tasks into subtasks
- Synthesizes results from multiple agents

### 2. **Data Analyst**
- Exploratory data analysis
- Statistical analysis
- Data quality assessment
- Feature engineering suggestions

### 3. **Machine Learning Engineer**
- Model selection and training
- Hyperparameter tuning
- Model evaluation
- Feature importance analysis

### 4. **Visualization Specialist**
- Publication-quality plots
- Interactive dashboards
- Performance visualizations
- Exploratory visualizations

### 5. **Data Engineer**
- ETL pipelines
- Data transformation
- Large dataset handling
- Database operations

### 6. **Deployment Engineer**
- Model APIs (Flask/FastAPI)
- Docker containerization
- Deployment pipelines
- Model serving

## 📦 Installation

### Prerequisites

1. Install Ollama: https://ollama.com
2. Pull required model:
```bash
ollama pull qwen2.5:7b
```

### Setup

```bash
# Clone or navigate to project directory
cd Data_science_agentic_project

# Install Python dependencies
pip install -r requirements.txt

# Verify Ollama is running
ollama list
```

## 🚀 Quick Start

### Beautiful Web UI (Recommended)

```bash
# Launch the beautiful web interface
python run_ui.py

# Or run with streamlit directly
streamlit run app.py
```

The UI will open in your browser with:
- 🎨 Beautiful gradient design
- 💬 Chat interface with agents
- ⚙️ Workflow management
- 📊 Analytics dashboard
- ⚙️ Settings configuration

### Basic Usage

```python
from agent_orchestrator import DataScienceAgentOrchestrator

# Initialize system
orchestrator = DataScienceAgentOrchestrator()

# Run a data science pipeline
task = "Analyze the iris dataset and build a classification model"

results = orchestrator.run_data_science_pipeline(
    task,
    agent_sequence=['data_analyst', 'visualization_specialist', 'ml_engineer']
)
```

### Using Workflow Manager

```python
from workflow_manager import WorkflowManager
from agent_orchestrator import DataScienceAgentOrchestrator

orchestrator = DataScienceAgentOrchestrator()
workflow_manager = WorkflowManager(orchestrator)

# Run an EDA workflow
results = workflow_manager.exploratory_data_analysis("path/to/dataset.csv")

# Run an ML modeling pipeline
results = workflow_manager.ml_modeling_pipeline(
    "path/to/dataset.csv",
    task_type="classification"
)
```

### Chat with Individual Agents

```python
# Chat with a specific agent
data_analyst = orchestrator.get_agent('data_analyst')

response = data_analyst.run("""
    Load the iris dataset and calculate summary statistics
""")
```

## 📝 Examples

See `examples.py` for complete working examples:

1. **Quick EDA**: Exploratory data analysis workflow
2. **Classification**: ML model development
3. **Deployment**: Model API creation
4. **Custom Workflow**: Multi-agent collaboration
5. **Regression**: Complete regression analysis

Run examples:
```bash
python examples.py
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│    DataScienceAgentOrchestrator         │
│           (Root Agent)                   │
└───────────────┬─────────────────────────┘
                │
    ┌───────────┴───────────┐
    │                       │
    ▼                       ▼
┌─────────┐         ┌─────────────────┐
│  Agent  │         │   Workflow      │
│ Manager │         │   Manager       │
└────┬────┘         └─────────────────┘
     │
     ├─► Data Analyst
     ├─► ML Engineer
     ├─► Visualization Specialist
     ├─► Data Engineer
     └─► Deployment Engineer
```

## 🔧 Configuration

Edit `config.yaml` to customize:
- Model settings
- Agent configurations
- Workflow definitions
- System settings

## 📊 Supported Workflows

### 1. Exploratory Data Analysis
```python
workflow_manager.exploratory_data_analysis(dataset_path)
```

### 2. ML Modeling Pipeline
```python
workflow_manager.ml_modeling_pipeline(dataset_path, task_type)
```

### 3. Time Series Analysis
```python
workflow_manager.time_series_analysis(dataset_path)
```

### 4. Model Deployment
```python
workflow_manager.deploy_model(model_path, model_type)
```

### 5. Custom Pipeline
```python
workflow_manager.custom_pipeline(query, agent_sequence)
```

## 🛠️ Customization

### Adding a New Agent

```python
agents['new_agent'] = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:7b"),
    name="New Agent",
    instruction="Your agent's specialized instructions here",
    tools=[built_in_code_execution, WebSearchTool()],
)
```

### Creating Custom Workflows

```python
def my_custom_workflow(query):
    return orchestrator.run_data_science_pipeline(
        query,
        agent_sequence=['agent1', 'agent2', 'agent3']
    )
```

## 📁 Project Structure

```
Data_science_agentic_project/
│
├── agent_orchestrator.py    # Main orchestrator and agent definitions
├── workflow_manager.py      # Workflow management and pipelines
├── app.py                   # Beautiful Streamlit UI
├── run_ui.py                # UI launcher script
├── examples.py              # Example use cases
├── utils.py                 # Utility functions
├── requirements.txt         # Python dependencies
├── config.yaml             # Configuration file
├── docker-compose.yml       # Docker deployment
├── .streamlit/config.toml  # Streamlit configuration
├── README.md               # This file
├── UI_GUIDE.md             # UI documentation
├── QUICK_START_UI.md       # Quick start guide
└── results/                # Saved workflow results
```

## 🎯 Use Cases

1. **Quick Data Analysis**: Get instant insights from datasets
2. **Model Development**: Complete ML pipelines from data to deployment
3. **Research**: Exploratory analysis with statistical rigor
4. **Production**: Deploy trained models as APIs
5. **Education**: Learn data science through agent guidance

## 🔍 Requirements

- Python 3.8+
- Ollama with qwen model
- Google ADK
- LiteLLM
- Data science libraries (pandas, sklearn, etc.)

## 📈 Improvements Over Original Prototype

1. **Multi-Agent System**: 6 specialized agents vs 1 generic agent
2. **Workflow Management**: Predefined workflows for common tasks
3. **Better Instructions**: Domain-specific, detailed agent instructions
4. **Code Execution**: Built-in code execution for all agents
5. **Web Search**: Research capabilities for latest techniques
6. **Modular Architecture**: Easy to extend and customize
7. **Example Collection**: Ready-to-use examples
8. **Configuration**: YAML-based configuration
9. **Result Saving**: Automatic result persistence
10. **Professional Structure**: Production-ready codebase

## 🤝 Contributing

Feel free to extend this system with:
- New specialized agents
- Additional workflows
- Custom tools and integrations
- Improved agent instructions

## 📄 License

This project is for educational and research purposes.

## 🙏 Acknowledgments

- Google ADK for the agent framework
- Ollama for local LLM inference
- The open-source data science community



