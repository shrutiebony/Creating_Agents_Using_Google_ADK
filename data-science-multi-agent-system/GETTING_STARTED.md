# Getting Started Guide

## Step 1: Prerequisites

### Install Ollama

1. Download from https://ollama.com
2. Install Ollama
3. Start Ollama service (usually runs automatically)

### Pull Required Model

```bash
ollama pull qwen2.5:7b
```

Or use a different model:
```bash
ollama pull qwen3:8b
```

Verify installation:
```bash
ollama list
```

You should see qwen models listed.

## Step 2: Install Python Dependencies

```bash
# Navigate to project directory
cd Data_science_agentic_project

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Verify Installation

Run the test script:

```bash
python test_system.py
```

This will:
- Check if all agents initialize correctly
- Test agent communication
- Verify Ollama connection
- Display system status

Expected output:
```
✓ Orchestrator initialized successfully
✓ Retrieved agents
✓ Agent responded successfully
All Tests Passed!
```

## Step 4: Choose Your Starting Point

### Option A: Interactive Quick Start (Recommended for Beginners)

```bash
python quick_start.py
```

This provides a menu-driven interface where you can:
- Test the system
- Run quick examples
- Chat with agents
- Execute custom tasks

### Option B: Run Examples

```bash
python examples.py
```

Then select an example to run:
- Quick EDA
- Classification Model
- Model Deployment
- Custom Workflow
- Regression Analysis

### Option C: Use in Your Own Code

```python
from agent_orchestrator import DataScienceAgentOrchestrator

# Initialize
orchestrator = DataScienceAgentOrchestrator()

# Run a task
task = "Analyze the iris dataset and build a classification model"
results = orchestrator.run_data_science_pipeline(
    task,
    agent_sequence=['data_analyst', 'ml_engineer']
)
```

## Step 5: Your First Project

Let's start with a simple example:

### Example: Quick Data Analysis

```python
from agent_orchestrator import DataScienceAgentOrchestrator

# Initialize
orchestrator = DataScienceAgentOrchestrator()

# Ask for analysis
task = """
Perform exploratory data analysis on the iris dataset from sklearn.
Create visualizations showing feature distributions and relationships.
"""

# Run it
results = orchestrator.run_data_science_pipeline(
    task,
    agent_sequence=['data_analyst', 'visualization_specialist']
)
```

This will:
1. Load the iris dataset
2. Perform statistical analysis
3. Create visualizations
4. Provide insights

## Common Issues and Solutions

### Issue 1: "Connection refused" when running agents

**Solution**: Make sure Ollama is running
```bash
ollama serve
```

### Issue 2: "Model not found"

**Solution**: Pull the required model
```bash
ollama pull qwen2.5:7b
```

### Issue 3: Import errors

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue 4: Slow responses

**Solution**: 
- Use smaller model: `qwen2.5:7b` instead of `qwen3:8b`
- Close other applications using GPU
- Increase system resources

## Next Steps

1. **Read the README**: Understand the full system capabilities
2. **Explore Examples**: Run different examples from `examples.py`
3. **Try Your Own Data**: Use your own datasets
4. **Customize Agents**: Modify agent instructions in `agent_orchestrator.py`
5. **Create Workflows**: Define custom workflows in `workflow_manager.py`

## Learning Path

### Beginner
1. Run `python quick_start.py`
2. Select "1. Test System"
3. Select "2. Quick EDA"
4. Read the output

### Intermediate
1. Run `python examples.py`
2. Modify examples to use your data
3. Create custom agent conversations

### Advanced
1. Modify agent instructions
2. Create custom workflows
3. Add new specialized agents
4. Integrate with your own tools

## Resources

- **Documentation**: `README.md`
- **Examples**: `examples.py`
- **Improvements**: `IMPROVEMENTS.md`
- **Configuration**: `config.yaml`
- **Test Suite**: `test_system.py`

## Getting Help

If you encounter issues:

1. Check that Ollama is running: `ollama list`
2. Run test suite: `python test_system.py`
3. Check error messages carefully
4. Verify model is installed: `ollama list`
5. Ensure dependencies are installed: `pip list`

## Happy Data Science!

You're now ready to use the Data Science Agentic System. Start with the quick start menu and explore the possibilities!

```bash
python quick_start.py
```

