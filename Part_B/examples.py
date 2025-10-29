"""
Example use cases for the Data Science Agent System
"""

from agent_orchestrator import DataScienceAgentOrchestrator
from workflow_manager import WorkflowManager


def example_1_quick_eda():
    """Example 1: Quick Exploratory Data Analysis"""
    print("\n" + "="*60)
    print("Example 1: Quick EDA on Boston Housing Dataset")
    print("="*60 + "\n")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    query = """
    Analyze the Boston housing dataset from sklearn.
    Create comprehensive visualizations showing:
    - Distribution of target variable
    - Feature distributions
    - Correlation heatmap
    - Outlier visualizations
    """
    
    results = orchestrator.run_data_science_pipeline(
        query,
        agent_sequence=['data_analyst', 'visualization_specialist']
    )
    
    return results


def example_2_classification():
    """Example 2: Classification Model Development"""
    print("\n" + "="*60)
    print("Example 2: Develop a Classification Model")
    print("="*60 + "\n")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    query = """
    Build a classification model using the breast cancer dataset from sklearn.
    
    Requirements:
    1. Explore the data
    2. Split into train/test (80/20)
    3. Train multiple classifiers (Random Forest, SVM, XGBoost)
    4. Compare performance
    5. Select best model and optimize hyperparameters
    6. Evaluate with confusion matrix and classification report
    7. Plot feature importance
    """
    
    results = orchestrator.run_data_science_pipeline(
        query,
        agent_sequence=['data_analyst', 'ml_engineer', 'visualization_specialist']
    )
    
    return results


def example_3_deployment():
    """Example 3: Model Deployment"""
    print("\n" + "="*60)
    print("Example 3: Deploy a Machine Learning Model")
    print("="*60 + "\n")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    query = """
    Create a Flask API for serving a machine learning model.
    
    Requirements:
    1. Train a simple classifier on iris dataset
    2. Create a Flask/FastAPI application
    3. Add prediction endpoint
    4. Add health check endpoint
    5. Create Dockerfile
    6. Provide usage instructions
    """
    
    results = orchestrator.run_data_science_pipeline(
        query,
        agent_sequence=['ml_engineer', 'deployment_engineer']
    )
    
    return results


def example_4_custom_workflow():
    """Example 4: Custom Multi-Agent Workflow"""
    print("\n" + "="*60)
    print("Example 4: Custom Workflow - Data Pipeline")
    print("="*60 + "\n")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    # Chat with individual agents
    data_engineer = orchestrator.get_agent('data_engineer')
    analyst = orchestrator.get_agent('data_analyst')
    
    print("Step 1: Data Engineer setting up pipeline...")
    pipeline_code = data_engineer.run("""
    Create a data processing pipeline that:
    1. Reads CSV files
    2. Handles missing values
    3. Applies feature scaling
    4. Exports to parquet format
    
    Provide complete, runnable code.
    """)
    
    print("\nStep 2: Data Analyst examining results...")
    analysis = analyst.run(f"""
    Review this data processing pipeline and suggest improvements:
    {pipeline_code}
    """)
    
    return {"pipeline": pipeline_code, "analysis": analysis}


def example_5_regression():
    """Example 5: Regression Analysis"""
    print("\n" + "="*60)
    print("Example 5: Regression Model Development")
    print("="*60 + "\n")
    
    workflow_manager = WorkflowManager(
        DataScienceAgentOrchestrator()
    )
    
    query = """
    Build a regression model to predict house prices using the California housing dataset.
    
    Include:
    1. Load and explore data
    2. Handle missing values and outliers
    3. Feature engineering
    4. Train multiple regression models (Linear, Ridge, Lasso, Random Forest, XGBoost)
    5. Compare using MSE, RMSE, R2
    6. Visualize predictions vs actual
    7. Feature importance analysis
    """
    
    results = workflow_manager.custom_pipeline(
        query,
        ['data_analyst', 'ml_engineer', 'visualization_specialist']
    )
    
    workflow_manager.save_results(results, "regression_analysis")
    
    return results


def run_all_examples():
    """Run all examples sequentially"""
    examples = [
        ("Quick EDA", example_1_quick_eda),
        ("Classification Model", example_2_classification),
        ("Model Deployment", example_3_deployment),
        ("Custom Workflow", example_4_custom_workflow),
        ("Regression Analysis", example_5_regression),
    ]
    
    print("="*60)
    print("Running All Examples")
    print("="*60)
    
    for name, example_func in examples:
        print(f"\n>>> Running: {name}")
        try:
            example_func()
            print(f"✓ {name} completed")
        except Exception as e:
            print(f"✗ {name} failed: {e}")
        print("-"*60)
    
    print("\nAll examples completed!")


if __name__ == "__main__":
    # Run specific example or all
    example_choice = input("""
    Select example to run:
    1. Quick EDA
    2. Classification Model
    3. Model Deployment
    4. Custom Workflow
    5. Regression Analysis
    6. Run all
    
    Enter choice (1-6): """)
    
    if example_choice == "1":
        example_1_quick_eda()
    elif example_choice == "2":
        example_2_classification()
    elif example_choice == "3":
        example_3_deployment()
    elif example_choice == "4":
        example_4_custom_workflow()
    elif example_choice == "5":
        example_5_regression()
    elif example_choice == "6":
        run_all_examples()
    else:
        print("Invalid choice, running example 1...")
        example_1_quick_eda()

