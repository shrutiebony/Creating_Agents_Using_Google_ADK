"""
Utility functions for the Data Science Agent System
"""

import json
import os
from typing import Dict, Any, List
from datetime import datetime


class AgentUtils:
    """Utility class for agent operations"""
    
    @staticmethod
    def save_conversation(messages: List[Dict], filename: str = None):
        """Save conversation to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.json"
        
        os.makedirs("./conversations", exist_ok=True)
        filepath = os.path.join("./conversations", filename)
        
        with open(filepath, 'w') as f:
            json.dump(messages, f, indent=2, default=str)
        
        print(f"Conversation saved to: {filepath}")
        return filepath
    
    @staticmethod
    def format_agent_response(response: Any) -> str:
        """Format agent response for display"""
        if isinstance(response, str):
            return response
        elif isinstance(response, dict):
            return json.dumps(response, indent=2)
        else:
            return str(response)
    
    @staticmethod
    def create_task_summary(results: Dict[str, Any]) -> str:
        """Create a summary of task results"""
        summary = f"""
Task Summary
{'='*50}
Total Agents Used: {len(results)}
Agents: {', '.join(results.keys())}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        return summary
    
    @staticmethod
    def list_available_datasets() -> List[str]:
        """List commonly used sklearn datasets"""
        return [
            "iris - Classification, 150 samples, 4 features",
            "wine - Classification, 178 samples, 13 features",
            "breast_cancer - Classification, 569 samples, 30 features",
            "boston - Regression, 506 samples, 13 features",
            "digits - Classification, 1797 samples, 64 features",
            "diabetes - Regression, 442 samples, 10 features",
            "california_housing - Regression, 20640 samples, 8 features",
        ]
    
    @staticmethod
    def get_dataset_info(dataset_name: str) -> str:
        """Get information about a dataset"""
        info = {
            "iris": "Fisher's Iris dataset (3 classes, 150 samples, 4 features)",
            "wine": "Wine quality dataset (3 classes, 178 samples, 13 features)",
            "breast_cancer": "Wisconsin Breast Cancer (2 classes, 569 samples, 30 features)",
            "boston": "Boston Housing Prices (506 samples, 13 features)",
            "digits": "Handwritten digits (10 classes, 1797 samples, 64 features)",
            "diabetes": "Diabetes progression (442 samples, 10 features)",
            "california_housing": "California Housing Prices (20640 samples, 8 features)",
        }
        return info.get(dataset_name.lower(), "Unknown dataset")
    
    @staticmethod
    def validate_csv_file(filepath: str) -> bool:
        """Validate that a CSV file exists and is readable"""
        if not os.path.exists(filepath):
            return False
        try:
            import pandas as pd
            pd.read_csv(filepath, nrows=5)
            return True
        except:
            return False
    
    @staticmethod
    def get_file_info(filepath: str) -> Dict[str, Any]:
        """Get information about a file"""
        info = {
            "exists": os.path.exists(filepath),
            "size": 0,
            "extension": "",
        }
        
        if info["exists"]:
            info["size"] = os.path.getsize(filepath)
            info["extension"] = os.path.splitext(filepath)[1]
        
        return info


class DatasetLoader:
    """Helper class to load common datasets"""
    
    @staticmethod
    def load_sklearn_dataset(name: str):
        """Load a sklearn dataset by name"""
        try:
            from sklearn import datasets
            
            dataset_map = {
                "iris": datasets.load_iris,
                "wine": datasets.load_wine,
                "breast_cancer": datasets.load_breast_cancer,
                "boston": datasets.load_boston if hasattr(datasets, 'load_boston') else None,
                "digits": datasets.load_digits,
                "diabetes": datasets.load_diabetes,
                "california_housing": lambda: datasets.fetch_california_housing(return_X_y=False),
            }
            
            loader = dataset_map.get(name.lower())
            if loader:
                return loader()
            else:
                return None
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return None
    
    @staticmethod
    def get_sample_code(dataset_name: str) -> str:
        """Get sample code to load a dataset"""
        code_templates = {
            "sklearn": f"""
from sklearn.datasets import load_{dataset_name}
import pandas as pd

# Load dataset
data = load_{dataset_name}()

# Create DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print(f"Loaded {{dataset_name}} dataset")
print(f"Shape: {{df.shape}}")
""",
            "csv": f"""
import pandas as pd

# Load CSV
df = pd.read_csv('{dataset_name}')

print(f"Loaded dataset: {{df.shape}}")
print(df.head())
""",
        }
        
        return code_templates.get("sklearn", "")


def print_system_info():
    """Print system information"""
    print("\n" + "="*60)
    print("Data Science Agent System - Information")
    print("="*60)
    
    try:
        import google.adk
        print("✓ Google ADK installed")
    except:
        print("✗ Google ADK not installed")
    
    try:
        import litellm
        print("✓ LiteLLM installed")
    except:
        print("✗ LiteLLM not installed")
    
    try:
        import pandas
        print("✓ Pandas installed")
    except:
        print("✗ Pandas not installed")
    
    try:
        import sklearn
        print("✓ Scikit-learn installed")
    except:
        print("✗ Scikit-learn not installed")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    # Demo utility functions
    print_system_info()
    
    print("\nAvailable datasets:")
    for dataset in AgentUtils.list_available_datasets():
        print(f"  - {dataset}")
    
    print("\nUtility functions loaded successfully!")

