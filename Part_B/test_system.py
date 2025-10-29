"""
Test script to verify the system is working correctly
"""

from agent_orchestrator import DataScienceAgentOrchestrator
from workflow_manager import WorkflowManager


def test_system():
    """Test the basic functionality of the system"""
    
    print("\n" + "="*70)
    print("Data Science Agent System - Test Suite")
    print("="*70 + "\n")
    
    # Test 1: Initialize orchestrator
    print("Test 1: Initializing orchestrator...")
    try:
        orchestrator = DataScienceAgentOrchestrator()
        print("✓ Orchestrator initialized successfully")
        print(f"  - Available agents: {list(orchestrator.agents.keys())}")
    except Exception as e:
        print(f"✗ Failed to initialize orchestrator: {e}")
        return False
    
    # Test 2: Get agents
    print("\nTest 2: Accessing individual agents...")
    try:
        for agent_name in orchestrator.agents.keys():
            agent = orchestrator.get_agent(agent_name)
            print(f"  ✓ Retrieved agent: {agent_name}")
    except Exception as e:
        print(f"✗ Failed to retrieve agents: {e}")
        return False
    
    # Test 3: Initialize workflow manager
    print("\nTest 3: Initializing workflow manager...")
    try:
        workflow_manager = WorkflowManager(orchestrator)
        print("✓ Workflow manager initialized successfully")
    except Exception as e:
        print(f"✗ Failed to initialize workflow manager: {e}")
        return False
    
    # Test 4: Simple agent interaction
    print("\nTest 4: Testing agent interaction...")
    try:
        analyst = orchestrator.get_agent('data_analyst')
        response = analyst.run("What are the key steps in exploratory data analysis?")
        print("✓ Agent interaction successful")
        print(f"  - Response length: {len(response)} characters")
    except Exception as e:
        print(f"✗ Agent interaction failed: {e}")
        print("  Note: This might fail if Ollama is not running or model is not installed")
        return False
    
    # Test 5: System summary
    print("\n" + "="*70)
    print("System Summary")
    print("="*70)
    print(f"✓ Total agents: {len(orchestrator.agents)}")
    print(f"✓ Agents configured: {', '.join(orchestrator.agents.keys())}")
    print(f"✓ Model: {orchestrator.model_name}")
    print(f"✓ Results directory: {workflow_manager.results_dir}")
    
    print("\n" + "="*70)
    print("All Tests Passed!")
    print("="*70)
    print("\nThe system is ready to use.")
    print("\nNext steps:")
    print("  1. Run: python examples.py")
    print("  2. Or use the orchestrator in your own code")
    print("  3. Check the README.md for usage examples\n")
    
    return True


if __name__ == "__main__":
    success = test_system()
    exit(0 if success else 1)

