"""
Quick Start Guide for Data Science Agent System
Run this script to get started immediately
"""

from agent_orchestrator import DataScienceAgentOrchestrator
from workflow_manager import WorkflowManager


def print_menu():
    """Display the main menu"""
    print("\n" + "="*70)
    print("Data Science Agentic System - Quick Start")
    print("="*70)
    print("\nSelect an option:")
    print("\n1. Test System - Verify installation and Ollama connection")
    print("2. Quick EDA - Exploratory data analysis on sklearn datasets")
    print("3. ML Modeling - Build a classification model")
    print("4. Chat with Agent - Interactive conversation with an agent")
    print("5. Custom Task - Define your own data science task")
    print("6. View Examples - See all available examples")
    print("0. Exit")
    print("\n" + "-"*70)


def test_system():
    """Test that the system is working"""
    print("\n>>> Testing system...")
    
    try:
        orchestrator = DataScienceAgentOrchestrator()
        print("✓ System initialized successfully!")
        print(f"\nAvailable agents: {', '.join(orchestrator.agents.keys())}")
        
        # Quick test with an agent
        print("\n>>> Testing agent response...")
        analyst = orchestrator.get_agent('data_analyst')
        response = analyst.run("Briefly explain what exploratory data analysis is.")
        print(f"✓ Agent responded successfully (length: {len(response)} chars)")
        
        return True
    except Exception as e:
        print(f"✗ System test failed: {e}")
        print("\nPossible issues:")
        print("  - Ollama is not running (start with: ollama serve)")
        print("  - Qwen model not installed (install with: ollama pull qwen2.5:7b)")
        print("  - Dependencies not installed (install with: pip install -r requirements.txt)")
        return False


def quick_eda():
    """Run quick EDA on a dataset"""
    print("\n>>> Starting Exploratory Data Analysis...")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    # Use iris dataset as example
    task = """
    Perform exploratory data analysis on the iris dataset from sklearn.
    
    Include:
    1. Load the dataset
    2. Display basic statistics
    3. Check for missing values
    4. Create visualizations (scatter plots, histograms, pair plots)
    5. Analyze class distribution
    6. Provide key insights
    """
    
    print("\nThis may take a few moments as agents process the data...\n")
    
    try:
        results = orchestrator.run_data_science_pipeline(
            task,
            agent_sequence=['data_analyst', 'visualization_specialist']
        )
        print("\n✓ EDA completed successfully!")
        return results
    except Exception as e:
        print(f"\n✗ EDA failed: {e}")
        return None


def ml_modeling():
    """Build an ML model"""
    print("\n>>> Starting ML Modeling...")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    task = """
    Build a classification model using the wine dataset from sklearn.
    
    Steps:
    1. Load and explore the wine dataset
    2. Prepare the data (train/test split)
    3. Train a Random Forest classifier
    4. Evaluate the model with accuracy, confusion matrix, classification report
    5. Visualize the results
    """
    
    print("\nThis may take a few moments...\n")
    
    try:
        results = orchestrator.run_data_science_pipeline(
            task,
            agent_sequence=['data_analyst', 'ml_engineer', 'visualization_specialist']
        )
        print("\n✓ ML modeling completed successfully!")
        return results
    except Exception as e:
        print(f"\n✗ ML modeling failed: {e}")
        return None


def chat_with_agent():
    """Interactive chat with an agent"""
    print("\n>>> Chat with Data Science Agents")
    
    orchestrator = DataScienceAgentOrchestrator()
    
    print("\nAvailable agents:")
    for i, name in enumerate(orchestrator.agents.keys(), 1):
        print(f"  {i}. {name}")
    
    try:
        choice = input("\nSelect agent (1-6): ")
        agent_names = list(orchestrator.agents.keys())
        agent_index = int(choice) - 1
        
        if 0 <= agent_index < len(agent_names):
            agent_name = agent_names[agent_index]
            agent = orchestrator.get_agent(agent_name)
            
            print(f"\nChatting with: {agent_name}")
            print("Type 'quit' to exit\n")
            
            while True:
                user_input = input(f"You ({agent_name}): ")
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                
                try:
                    response = agent.run(user_input)
                    print(f"\n{agent_name}: {response}\n")
                except Exception as e:
                    print(f"Error: {e}")
        else:
            print("Invalid agent selection")
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(f"Error: {e}")


def custom_task():
    """Run a custom task"""
    print("\n>>> Custom Data Science Task")
    
    user_task = input("\nDescribe your data science task: ")
    
    if not user_task:
        print("No task provided")
        return
    
    print("\nSelect agents to use (comma-separated):")
    print("  data_analyst, ml_engineer, visualization_specialist,")
    print("  data_engineer, deployment_engineer")
    
    agent_input = input("\nAgents (or press Enter for auto-select): ")
    
    agent_sequence = None
    if agent_input.strip():
        agent_sequence = [a.strip() for a in agent_input.split(',')]
    
    try:
        orchestrator = DataScienceAgentOrchestrator()
        
        print("\nProcessing your task...\n")
        results = orchestrator.run_data_science_pipeline(
            user_task,
            agent_sequence=agent_sequence
        )
        print("\n✓ Custom task completed!")
        return results
    except Exception as e:
        print(f"\n✗ Task failed: {e}")
        return None


def view_examples():
    """Display available examples"""
    print("\n>>> Available Examples\n")
    
    examples = [
        ("examples.py", [
            "1. example_1_quick_eda() - Boston Housing EDA",
            "2. example_2_classification() - Wine Classification Model",
            "3. example_3_deployment() - Model API Deployment",
            "4. example_4_custom_workflow() - Multi-agent Pipeline",
            "5. example_5_regression() - House Price Prediction",
        ]),
        ("workflow_manager.py", [
            "- exploratory_data_analysis(dataset_path)",
            "- ml_modeling_pipeline(dataset_path, task_type)",
            "- time_series_analysis(dataset_path)",
            "- deploy_model(model_path, model_type)",
            "- custom_pipeline(query, agent_sequence)",
        ])
    ]
    
    for file, examples_list in examples:
        print(f"\n{file}:")
        for ex in examples_list:
            print(f"  {ex}")
    
    print("\nTo run examples:")
    print("  python examples.py")


def main():
    """Main application loop"""
    print("\nWelcome to Data Science Agentic System!")
    print("This system provides AI-powered data science agents.")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-6): ").strip()
            
            if choice == "0":
                print("\nThank you for using Data Science Agentic System!")
                print("Goodbye!\n")
                break
            elif choice == "1":
                test_system()
            elif choice == "2":
                quick_eda()
            elif choice == "3":
                ml_modeling()
            elif choice == "4":
                chat_with_agent()
            elif choice == "5":
                custom_task()
            elif choice == "6":
                view_examples()
            else:
                print("\nInvalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()

