# System Architecture

## 🏗️ Overall Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│  (quick_start.py, examples.py, test_system.py, utils.py)    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     Application Layer                        │
│                 (agent_orchestrator.py)                      │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │          DataScienceAgentOrchestrator                    │ │
│  │  - Agent initialization                                 │ │
│  │  - Pipeline coordination                                 │ │
│  │  - Result synthesis                                      │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────┬───────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────┐
│                      Agent Layer                             │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Orchestrator│  │  Data Analyst│  │  ML Engineer │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │Visualization │  │Data Engineer │  │Deployment    │      │
│  │ Specialist   │  │              │  │Engineer      │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────────────────┬───────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────┐
│                      Tools Layer                             │
│  - Built-in code execution                                  │
│  - Web search                                               │
│  - File operations                                          │
└──────────────────────────────────┬───────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────┐
│                    Model Layer (Ollama)                      │
│  - Qwen 2.5:7b (configurable)                               │
│  - Local LLM inference                                      │
│  - Privacy-preserving                                       │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow

### 1. User Request Flow

```
User Query
    │
    ▼
Orchestrator analyzes task
    │
    ▼
Breaks into subtasks
    │
    ▼
Routes to specialized agents
    │
    ▼
Each agent executes
    │
    ▼
Results aggregated
    │
    ▼
Return to user
```

### 2. Agent Communication

```
Agent 1 ──► Intermediate Results ──► Agent 2 ──► Final Results
    │                                      │
    └──────► All results ──────────────────┘
                │
                ▼
          Orchestrator synthesizes
```

## 🤖 Agent Responsibilities

### Orchestrator Agent
- **Input**: User task
- **Process**: Planning, delegation, coordination
- **Output**: Synthesized results
- **Tools**: Code execution, web search

### Data Analyst Agent
- **Input**: Dataset/query
- **Process**: EDA, statistics, quality checks
- **Output**: Analysis report, insights
- **Tools**: Code execution, web search

### ML Engineer Agent
- **Input**: Prepared data
- **Process**: Model training, validation, tuning
- **Output**: Trained model, metrics
- **Tools**: Code execution, web search

### Visualization Specialist
- **Input**: Data/results
- **Process**: Create visualizations
- **Output**: Plots, charts, dashboards
- **Tools**: Code execution, web search

### Data Engineer Agent
- **Input**: Raw data
- **Process**: ETL, transformation
- **Output**: Processed data
- **Tools**: Code execution, web search

### Deployment Engineer
- **Input**: Trained model
- **Process**: API creation, containerization
- **Output**: Deployed model, API
- **Tools**: Code execution, web search

## 📁 File Responsibilities

### Core Files

**agent_orchestrator.py**
- Defines all agents
- Implements orchestrator logic
- Agent initialization
- Pipeline execution

**workflow_manager.py**
- Workflow definitions
- Pipeline orchestration
- Result persistence
- Predefined workflows

**examples.py**
- Usage demonstrations
- Complete examples
- Best practices
- Tutorial content

### Interface Files

**quick_start.py**
- Interactive menu
- User-friendly interface
- Simplified access
- Guided workflows

**test_system.py**
- System verification
- Health checks
- Installation testing
- Error detection

**utils.py**
- Helper functions
- Dataset loaders
- Common utilities
- Info display

### Configuration Files

**config.yaml**
- System settings
- Agent configuration
- Workflow definitions
- Parameters

**requirements.txt**
- Python dependencies
- Version specifications
- Package list

**setup.py**
- Installation script
- Package definition
- Distribution config

## 🔧 Extension Points

### Adding a New Agent

1. Define agent in `agent_orchestrator.py`:
```python
agents['new_agent'] = Agent(
    model=LiteLlm(model=self.model_name),
    name="New Agent Name",
    instruction="Agent responsibilities...",
    tools=[built_in_code_execution, WebSearchTool()],
)
```

2. Add to workflows in `workflow_manager.py`

3. Update documentation

### Adding a New Workflow

1. Add method to `WorkflowManager` class:
```python
def new_workflow(self, params):
    query = "Your workflow query"
    return self.orchestrator.run_data_science_pipeline(
        query,
        agent_sequence=['agent1', 'agent2']
    )
```

2. Add to configuration in `config.yaml`

3. Document in README

## 🔐 Security & Privacy

- **Local Execution**: All LLM calls via Ollama
- **No Data Leakage**: Data stays on your machine
- **Configurable**: Change models easily
- **Offline Capable**: Works without internet

## 📊 Performance Considerations

### Optimization Strategies

1. **Model Selection**: Use smaller models for faster response
2. **Agent Sequencing**: Run essential agents only
3. **Caching**: Results saved for reuse
4. **Parallel Execution**: Future enhancement

### Resource Usage

- **CPU**: Primary compute for Ollama
- **RAM**: Model loading and data processing
- **Disk**: Model storage and results
- **GPU**: Optional acceleration

## 🎯 Design Principles

1. **Modularity**: Each agent independent
2. **Extensibility**: Easy to add functionality
3. **Usability**: Simple interfaces
4. **Documentation**: Comprehensive guides
5. **Testing**: Built-in verification
6. **Configuration**: External settings
7. **Privacy**: Local-first approach

## 🚀 Deployment Architecture

### Local Development
```
Developer Machine
  ├── Ollama (Model Server)
  ├── Python Environment
  ├── Agent System
  └── Results Storage
```

### Future: Production
```
Production Server
  ├── API Gateway
  ├── Agent Orchestrator
  ├── Specialized Agents
  ├── Model Server (Ollama)
  └── Result Database
```

## 📈 Scalability

### Current State
- Single machine execution
- Sequential agent processing
- Local model inference

### Future Enhancements
- Parallel agent execution
- Distributed processing
- Cloud deployment
- Load balancing
- Auto-scaling

## 🔄 Integration Points

### External Integrations (Possible)

1. **Databases**: PostgreSQL, MongoDB
2. **Cloud Storage**: S3, GCS
3. **ML Platforms**: MLflow, Weights & Biases
4. **APIs**: RESTful integrations
5. **Notebooks**: Jupyter support
6. **Monitoring**: Prometheus, Grafana

### Current Integrations

1. **Ollama**: LLM inference
2. **Google ADK**: Agent framework
3. **LiteLLM**: Model abstraction
4. **Sklearn**: ML libraries
5. **Pandas**: Data processing
6. **Matplotlib/Plotly**: Visualization

## 🎓 Learning the System

### Beginner Path
1. Run `quick_start.py`
2. Read `GETTING_STARTED.md`
3. Try simple examples
4. Explore agent outputs

### Intermediate Path
1. Study `agent_orchestrator.py`
2. Run all examples
3. Modify agent instructions
4. Create custom workflows

### Advanced Path
1. Add new agents
2. Integrate external tools
3. Optimize performance
4. Deploy to production

## 📝 Summary

This architecture provides:
- ✅ Clear separation of concerns
- ✅ Modular design
- ✅ Easy extensibility
- ✅ Well-documented
- ✅ Production-ready structure
- ✅ Privacy-focused
- ✅ Comprehensive functionality

Built for data scientists who want AI-powered assistance while maintaining full control and privacy.

