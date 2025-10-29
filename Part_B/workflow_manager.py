"""
Workflow Manager for Data Science Pipelines
Provides predefined workflows and custom pipeline creation
"""

from agent_orchestrator import DataScienceAgentOrchestrator
from typing import List, Dict, Any, Optional
import os
import json
from datetime import datetime


class WorkflowManager:
    """Manages different data science workflows"""
    
    def __init__(self, orchestrator: DataScienceAgentOrchestrator):
        self.orchestrator = orchestrator
        self.workflow_history = []
        self.results_dir = "./results"
        
        # Ensure results directory exists
        os.makedirs(self.results_dir, exist_ok=True)
    
    def exploratory_data_analysis(self, dataset_path: str) -> Dict[str, Any]:
        """
        Complete exploratory data analysis workflow
        """
        query = f"""
        Perform comprehensive exploratory data analysis on: {dataset_path}
        
        Include:
        1. Load and examine the dataset
        2. Basic statistics and data quality checks
        3. Missing value analysis
        4. Correlation analysis
        5. Outlier detection
        6. Data distribution analysis
        7. Feature engineering suggestions
        """
        
        return self.orchestrator.run_data_science_pipeline(
            query,
            agent_sequence=['data_analyst', 'visualization_specialist']
        )
    
    def ml_modeling_pipeline(self, dataset_path: str, task_type: str = "classification") -> Dict[str, Any]:
        """
        Complete ML modeling pipeline
        Args:
            dataset_path: Path to dataset
            task_type: 'classification' or 'regression'
        """
        query = f"""
        Build a machine learning model for {task_type} using: {dataset_path}
        
        Steps:
        1. Data loading and exploration
        2. Data preprocessing and feature engineering
        3. Train/validation split
        4. Train multiple models and compare
        5. Hyperparameter tuning for best model
        6. Evaluate with appropriate metrics
        7. Generate performance visualizations
        """
        
        return self.orchestrator.run_data_science_pipeline(
            query,
            agent_sequence=['data_analyst', 'ml_engineer', 'visualization_specialist']
        )
    
    def time_series_analysis(self, dataset_path: str) -> Dict[str, Any]:
        """
        Time series analysis workflow
        """
        query = f"""
        Perform time series analysis on: {dataset_path}
        
        Include:
        1. Time series visualization
        2. Trend and seasonality analysis
        3. Stationarity tests
        4. Forecasting models (ARIMA, Prophet, etc.)
        5. Performance evaluation
        """
        
        return self.orchestrator.run_data_science_pipeline(
            query,
            agent_sequence=['data_engineer', 'visualization_specialist', 'ml_engineer']
        )
    
    def deploy_model(self, model_path: str, model_type: str = "sklearn") -> Dict[str, Any]:
        """
        Deploy a trained model
        """
        query = f"""
        Deploy a {model_type} model from: {model_path}
        
        Steps:
        1. Load and test the model
        2. Create a REST API with FastAPI
        3. Add model endpoints
        4. Create Docker configuration
        5. Generate deployment instructions
        """
        
        return self.orchestrator.run_data_science_pipeline(
            query,
            agent_sequence=['deployment_engineer']
        )
    
    def custom_pipeline(self, query: str, agent_sequence: List[str]) -> Dict[str, Any]:
        """
        Run a custom pipeline with specified agent sequence
        """
        return self.orchestrator.run_data_science_pipeline(query, agent_sequence)
    
    def save_results(self, results: Dict[str, Any], workflow_name: str):
        """Save workflow results to disk"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{workflow_name}_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"Results saved to: {filepath}")
        return filepath


def example_usage():
    """Example usage of the WorkflowManager"""
    
    # Initialize system
    orchestrator = DataScienceAgentOrchestrator()
    workflow_manager = WorkflowManager(orchestrator)
    
    print("Data Science Workflow Manager Initialized!\n")
    print("Available workflows:")
    print("1. exploratory_data_analysis(dataset_path)")
    print("2. ml_modeling_pipeline(dataset_path, task_type)")
    print("3. time_series_analysis(dataset_path)")
    print("4. deploy_model(model_path, model_type)")
    print("5. custom_pipeline(query, agent_sequence)")
    
    # Example: EDA on iris dataset
    print("\n" + "="*60)
    print("Example: Running EDA workflow")
    print("="*60 + "\n")
    
    task = "Perform exploratory data analysis on the sklearn iris dataset"
    
    results = workflow_manager.custom_pipeline(
        task,
        ['data_analyst', 'visualization_specialist']
    )
    
    return results


if __name__ == "__main__":
    example_usage()

