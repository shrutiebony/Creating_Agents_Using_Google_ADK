"""
Data Science Agent Orchestrator
A multi-agent system for comprehensive data science workflows
"""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import built_in_code_execution, WebSearchTool
from typing import List, Dict, Any
import json


class DataScienceAgentOrchestrator:
    """Orchestrates multiple specialized data science agents"""
    
    def __init__(self, model_name: str = "ollama_chat/qwen2.5:7b"):
        self.model_name = model_name
        self.agents = {}
        self.conversation_history = []
        
        # Initialize all specialized agents
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Initialize all specialized agents"""
        
        # Root/Orchestrator Agent
        self.agents['orchestrator'] = Agent(
            model=LiteLlm(model=self.model_name),
            name="Data Science Orchestrator",
            instruction="""You are a senior data science orchestrator. You coordinate multiple specialized agents to solve data science problems.
            
When a task comes in:
1. Analyze the problem requirements
2. Break it down into subtasks
3. Determine which specialist agents are needed
4. Coordinate the workflow between agents
5. Synthesize results into a final solution

Available agents:
- data_analyst: Exploratory data analysis, statistics, data cleaning
- ml_engineer: Machine learning model development and training
- visualization_specialist: Creating plots, charts, dashboards
- data_engineer: Data pipelines, ETL, data processing
- deployment_engineer: Model deployment and serving

Always think step-by-step and provide clear reasoning."""
,
            tools=[built_in_code_execution, WebSearchTool()],
        )
        
        # Data Analyst Agent
        self.agents['data_analyst'] = Agent(
            model=LiteLlm(model=self.model_name),
            name="Data Analyst",
            instruction="""You are a data analyst specializing in exploratory data analysis and statistics.

Your responsibilities include:
- Loading and examining datasets
- Identifying data quality issues (missing values, outliers, duplicates)
- Computing descriptive statistics
- Performing statistical tests
- Data cleaning and preprocessing
- Feature engineering suggestions
- Correlation and relationship analysis

Always provide clear, interpretable analysis with statistical rigor.
Use pandas, numpy, scipy for statistical analysis.
Include data quality reports with your findings.""",
            tools=[built_in_code_execution, WebSearchTool()],
        )
        
        # ML Engineer Agent
        self.agents['ml_engineer'] = Agent(
            model=LiteLlm(model=self.model_name),
            name="Machine Learning Engineer",
            instruction="""You are a machine learning engineer specializing in model development and training.

Your responsibilities include:
- Selecting appropriate ML algorithms for the problem
- Implementing scikit-learn, XGBoost, or deep learning models
- Feature engineering and selection
- Model training and validation
- Hyperparameter tuning
- Cross-validation and evaluation metrics
- Model interpretation and explainability

Use scikit-learn, xgboost, tensorflow, pytorch as needed.
Always provide evaluation metrics, confusion matrices, and feature importance.
Ensure models are reproducible with random seeds.""",
            tools=[built_in_code_execution, WebSearchTool()],
        )
        
        # Visualization Specialist
        self.agents['visualization_specialist'] = Agent(
            model=LiteLlm(model=self.model_name),
            name="Visualization Specialist",
            instruction="""You are a data visualization specialist creating compelling visualizations.

Your responsibilities include:
- Creating publication-quality plots using matplotlib and seaborn
- Building interactive visualizations with plotly
- Designing dashboards and reports
- Visualizing model performance
- Creating exploratory visualizations
- Making data accessible through charts

Use matplotlib, seaborn, plotly for static and interactive visualizations.
Create clean, informative, and aesthetically pleasing visualizations.
Always include proper labels, titles, and legends.""",
            tools=[built_in_code_execution, WebSearchTool()],
        )
        
        # Data Engineer
        self.agents['data_engineer'] = Agent(
            model=LiteLlm(model=self.model_name),
            name="Data Engineer",
            instruction="""You are a data engineer specializing in data pipelines and ETL processes.

Your responsibilities include:
- Building ETL pipelines
- Data transformation and wrangling
- Handling large datasets efficiently
- Working with different data formats (CSV, JSON, Parquet, etc.)
- Database operations
- Data quality checks and validation
- Optimizing data processing performance

Use pandas, polars, dask for data manipulation.
Write efficient, scalable code for data processing.
Handle memory constraints and optimize for performance.""",
            tools=[built_in_code_execution, WebSearchTool()],
        )
        
        # Deployment Engineer
        self.agents['deployment_engineer'] = Agent(
            model=LiteLlm(model=self.model_name),
            name="Deployment Engineer",
            instruction="""You are a deployment engineer specializing in ML model deployment and serving.

Your responsibilities include:
- Creating model APIs with Flask/FastAPI
- Model serialization (pickle, joblib, ONNX)
- Containerizing applications with Docker
- Deployment pipelines
- Model monitoring and logging
- Creating model serving endpoints
- Performance optimization

Use Flask, FastAPI for APIs.
Create production-ready, scalable deployments.
Include proper error handling and logging.""",
            tools=[built_in_code_execution, WebSearchTool()],
        )
    
    def run_data_science_pipeline(self, user_query: str, agent_sequence: List[str] = None) -> Dict[str, Any]:
        """
        Run a data science pipeline with multiple agents
        
        Args:
            user_query: The user's data science task
            agent_sequence: List of agent names to use in sequence
                           If None, orchestrator decides
        
        Returns:
            Results from the pipeline
        """
        print(f"\n{'='*60}")
        print(f"Data Science Pipeline Starting")
        print(f"{'='*60}\n")
        print(f"User Query: {user_query}\n")
        
        # If no sequence specified, let orchestrator decide
        if agent_sequence is None:
            # Ask orchestrator for the plan
            planning_query = f"""
            Analyze this data science task: {user_query}
            
            Suggest which agents should be involved and in what order.
            Return your analysis as a structured plan.
            """
            
            orchestrator_plan = self.agents['orchestrator'].run(planning_query)
            print(f"Orchestrator Plan:\n{orchestrator_plan}\n")
        
        # For now, use default sequence or provided one
        if agent_sequence is None:
            agent_sequence = ['data_analyst', 'visualization_specialist', 'ml_engineer']
        
        results = {}
        previous_output = user_query
        
        # Run agents in sequence
        for agent_name in agent_sequence:
            if agent_name not in self.agents:
                print(f"Warning: Agent '{agent_name}' not found, skipping...")
                continue
            
            print(f"\n{'='*60}")
            print(f"Running: {agent_name}")
            print(f"{'='*60}\n")
            
            # Create context-aware query
            query = f"""
            Previous context: {previous_output}
            
            Your task is to contribute to this data science project based on the above context.
            Focus on your specialized area and produce actionable insights/code.
            """
            
            # Run agent
            agent = self.agents[agent_name]
            output = agent.run(query)
            results[agent_name] = output
            previous_output = output
            
            print(f"\n{agent_name} completed.")
        
        return results
    
    def get_agent(self, name: str) -> Agent:
        """Get a specific agent by name"""
        return self.agents.get(name)
    
    def chat_with_agent(self, agent_name: str, message: str) -> str:
        """Have a conversation with a specific agent"""
        if agent_name not in self.agents:
            return f"Agent '{agent_name}' not found. Available agents: {list(self.agents.keys())}"
        
        agent = self.agents[agent_name]
        response = agent.run(message)
        return response


def main():
    """Main function to demonstrate the system"""
    print("Initializing Data Science Agent System...\n")
    
    # Initialize orchestrator
    orchestrator = DataScienceAgentOrchestrator()
    
    # Example usage
    print("Available agents:", list(orchestrator.agents.keys()))
    
    # Example task
    task = """
    Analyze the iris dataset and build a classification model to predict species.
    Create visualizations of the data distribution and model performance.
    """
    
    print("\nStarting example task...")
    results = orchestrator.run_data_science_pipeline(
        task,
        agent_sequence=['data_analyst', 'visualization_specialist', 'ml_engineer']
    )
    
    print("\n\nPipeline completed!")
    print("Results keys:", list(results.keys()))


if __name__ == "__main__":
    main()

