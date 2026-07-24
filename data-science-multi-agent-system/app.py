"""
Beautiful Web UI for Data Science Agent System
Built with Streamlit
"""

import streamlit as st
import time
import json
from datetime import datetime
from agent_orchestrator import DataScienceAgentOrchestrator
from workflow_manager import WorkflowManager
from utils import AgentUtils

# Page configuration
st.set_page_config(
    page_title="Data Science AI Agents",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .agent-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .agent-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .success-box {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        background: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)


# Initialize session state
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = None
if 'workflow_manager' not in st.session_state:
    st.session_state.workflow_manager = None
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []


def initialize_system():
    """Initialize the agent system"""
    if st.session_state.orchestrator is None:
        with st.spinner('🤖 Initializing AI Agents...'):
            try:
                st.session_state.orchestrator = DataScienceAgentOrchestrator()
                st.session_state.workflow_manager = WorkflowManager(
                    st.session_state.orchestrator
                )
                return True
            except Exception as e:
                st.error(f"Failed to initialize system: {e}")
                return False
    return True


def display_agent_card(name, description, icon):
    """Display an agent card"""
    st.markdown(f"""
        <div class="agent-card">
            <h3>{icon} {name}</h3>
            <p style="color: #666;">{description}</p>
        </div>
    """, unsafe_allow_html=True)


def main():
    # Header
    st.markdown('<div class="main-header">🤖 Data Science AI Agents</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">AI-Powered Multi-Agent System for Data Science Workflows</p>', unsafe_allow_html=True)
    
    # Initialize system
    if not initialize_system():
        st.stop()
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🎯 Navigation")
        page = st.radio(
            "Select Page",
            ["🏠 Home", "💬 Chat with Agent", "⚙️ Workflows", "📊 Analytics", "⚙️ Settings"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("## 🤖 Agents")
        
        agents = {
            "🎯 Orchestrator": "Coordinates all agents",
            "📊 Data Analyst": "EDA and statistics",
            "🧠 ML Engineer": "Model development",
            "🎨 Visualization": "Charts and plots",
            "⚙️ Data Engineer": "ETL pipelines",
            "🚀 Deployment": "Model serving"
        }
        
        for agent_name, desc in agents.items():
            display_agent_card(agent_name, desc, "")
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("## 📈 Quick Stats")
        st.metric("Agents Available", "6")
        st.metric("Workflows", "5+")
        st.metric("Status", "✅ Online")
    
    # Main content based on selected page
    if page == "🏠 Home":
        home_page()
    elif page == "💬 Chat with Agent":
        chat_page()
    elif page == "⚙️ Workflows":
        workflows_page()
    elif page == "📊 Analytics":
        analytics_page()
    elif page == "⚙️ Settings":
        settings_page()


def home_page():
    """Home page with quick actions"""
    
    st.markdown("## 🎉 Welcome to Data Science AI Agents")
    
    # Quick start cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown("### 📊 Quick EDA")
            st.markdown("Perform exploratory data analysis on your data")
            if st.button("Start EDA", key="eda_btn", use_container_width=True):
                st.session_state.quick_action = "eda"
                st.rerun()
    
    with col2:
        with st.container():
            st.markdown("### 🧠 ML Modeling")
            st.markdown("Build and train machine learning models")
            if st.button("Start ML", key="ml_btn", use_container_width=True):
                st.session_state.quick_action = "ml"
                st.rerun()
    
    with col3:
        with st.container():
            st.markdown("### 🚀 Deploy Model")
            st.markdown("Deploy your trained models as APIs")
            if st.button("Deploy", key="deploy_btn", use_container_width=True):
                st.session_state.quick_action = "deploy"
                st.rerun()
    
    st.markdown("---")
    
    # Example workflows
    st.markdown("## 🚀 Example Workflows")
    
    examples = [
        {
            "name": "Iris Classification",
            "description": "Classify iris species using the famous dataset",
            "agents": ["Data Analyst", "ML Engineer", "Visualization"],
            "button": "iris_class"
        },
        {
            "name": "Wine Quality Analysis",
            "description": "Analyze wine quality characteristics",
            "agents": ["Data Analyst", "Visualization"],
            "button": "wine_analysis"
        },
        {
            "name": "House Price Prediction",
            "description": "Predict house prices using regression",
            "agents": ["Data Analyst", "ML Engineer", "Visualization"],
            "button": "house_pred"
        },
        {
            "name": "Customer Segmentation",
            "description": "Segment customers using clustering",
            "agents": ["Data Analyst", "ML Engineer"],
            "button": "customer_seg"
        }
    ]
    
    for example in examples:
        with st.expander(f"📝 {example['name']} - {example['description']}"):
            st.markdown(f"**Agents Involved:** {', '.join(example['agents'])}")
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("▶️ Run", key=example['button']):
                    # Run example
                    run_example(example['name'])
    
    # Recent activity
    st.markdown("---")
    st.markdown("## 📜 Recent Activity")
    
    if st.session_state.conversation_history:
        for activity in st.session_state.conversation_history[-5:]:
            st.info(f"✅ {activity['task']} - {activity['timestamp']}")
    else:
        st.info("No recent activity. Start by running an example!")


def chat_page():
    """Chat interface with individual agents"""
    
    st.markdown("## 💬 Chat with AI Agents")
    
    # Agent selection
    agent_names = list(st.session_state.orchestrator.agents.keys())
    
    cols = st.columns(6)
    agent_icons = {
        'orchestrator': '🎯',
        'data_analyst': '📊',
        'ml_engineer': '🧠',
        'visualization_specialist': '🎨',
        'data_engineer': '⚙️',
        'deployment_engineer': '🚀'
    }
    
    for i, (agent_name, icon) in enumerate(agent_icons.items()):
        with cols[i]:
            if st.button(f"{icon}\n{agent_name.replace('_', ' ').title()}", 
                        key=f"agent_sel_{i}", use_container_width=True):
                st.session_state.selected_agent = agent_name
    
    # Display selected agent
    if 'selected_agent' in st.session_state:
        selected = st.session_state.selected_agent
        st.info(f"🤖 Chatting with: **{selected.replace('_', ' ').title()}**")
    
    # Chat interface
    st.markdown("---")
    
    # Display chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat['user'])
        with st.chat_message("assistant"):
            st.write(chat['assistant'])
    
    # User input
    user_input = st.chat_input("Ask your agent a question...")
    
    if user_input and 'selected_agent' in st.session_state:
        # Add user message
        st.session_state.chat_history.append({
            'user': user_input,
            'assistant': ''
        })
        
        # Get response
        with st.spinner('Thinking...'):
            try:
                agent = st.session_state.orchestrator.get_agent(
                    st.session_state.selected_agent
                )
                response = agent.run(user_input)
                
                # Update chat history
                st.session_state.chat_history[-1]['assistant'] = response
                
                # Save to conversation history
                st.session_state.conversation_history.append({
                    'task': f"Chat with {st.session_state.selected_agent}",
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")


def workflows_page():
    """Workflow execution page"""
    
    st.markdown("## ⚙️ Run Data Science Workflows")
    
    workflow_tab1, workflow_tab2, workflow_tab3 = st.tabs(
        ["📊 Exploratory Analysis", "🧠 ML Pipeline", "🚀 Deployment"]
    )
    
    with workflow_tab1:
        st.markdown("### Exploratory Data Analysis")
        dataset_path = st.text_input(
            "Dataset Path",
            placeholder="path/to/data.csv or sklearn dataset name",
            value="iris"
        )
        
        if st.button("Run EDA Workflow", type="primary"):
            run_eda_workflow(dataset_path)
    
    with workflow_tab2:
        st.markdown("### Machine Learning Modeling")
        
        col1, col2 = st.columns(2)
        with col1:
            dataset_path = st.text_input(
                "Dataset Path",
                key="ml_dataset",
                value="wine"
            )
        with col2:
            task_type = st.selectbox(
                "Task Type",
                ["classification", "regression", "clustering"]
            )
        
        if st.button("Run ML Pipeline", type="primary"):
            run_ml_workflow(dataset_path, task_type)
    
    with workflow_tab3:
        st.markdown("### Model Deployment")
        
        model_path = st.text_input(
            "Model Path",
            placeholder="path/to/model.pkl"
        )
        
        model_type = st.selectbox(
            "Model Type",
            ["sklearn", "pytorch", "tensorflow", "xgboost"]
        )
        
        if st.button("Deploy Model", type="primary"):
            run_deployment_workflow(model_path, model_type)
    
    st.markdown("---")
    st.markdown("### 📝 Custom Workflow")
    
    custom_query = st.text_area(
        "Describe your custom task",
        placeholder="e.g., Analyze sales data and predict future trends...",
        height=100
    )
    
    selected_agents = st.multiselect(
        "Select Agents",
        agent_names := list(st.session_state.orchestrator.agents.keys()),
        default=['data_analyst', 'visualization_specialist']
    )
    
    if st.button("Run Custom Workflow", type="primary"):
        if custom_query and selected_agents:
            run_custom_workflow(custom_query, selected_agents)
        else:
            st.warning("Please provide a task and select at least one agent")


def analytics_page():
    """Analytics and results page"""
    
    st.markdown("## 📊 Analytics & Results")
    
    # System health
    st.markdown("### 🏥 System Health")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Agents", "6/6", "✅")
    with col2:
        st.metric("Workflows", len(st.session_state.conversation_history))
    with col3:
        st.metric("Status", "Online", "🟢")
    with col4:
        st.metric("Last Activity", "Now" if st.session_state.conversation_history else "N/A")
    
    st.markdown("---")
    
    # Activity log
    st.markdown("### 📜 Activity Log")
    
    if st.session_state.conversation_history:
        for activity in reversed(st.session_state.conversation_history):
            with st.expander(f"📝 {activity['task']} - {activity['timestamp']}"):
                st.text("Task details would appear here")
    else:
        st.info("No activity recorded yet")
    
    # Export results
    st.markdown("---")
    st.markdown("### 💾 Export Results")
    
    if st.button("📥 Download Results"):
        if st.session_state.conversation_history:
            filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            json_data = json.dumps(st.session_state.conversation_history, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name=filename,
                mime="application/json"
            )
        else:
            st.warning("No results to export")


def settings_page():
    """Settings page"""
    
    st.markdown("## ⚙️ Settings")
    
    # Model settings
    st.markdown("### 🤖 Model Configuration")
    
    current_model = st.text_input(
        "Model Name",
        value="ollama_chat/qwen2.5:7b"
    )
    
    st.info("💡 Model is managed by Ollama. Change model by running: `ollama pull <model_name>`")
    
    # Agent settings
    st.markdown("### 🎯 Agent Settings")
    
    for agent_name in st.session_state.orchestrator.agents.keys():
        st.checkbox(
            f"Enable {agent_name.replace('_', ' ').title()}",
            value=True,
            key=f"agent_enable_{agent_name}"
        )
    
    # System info
    st.markdown("---")
    st.markdown("### ℹ️ System Information")
    
    system_info = {
        "Framework": "Google ADK",
        "Model Backend": "Ollama",
        "Default Model": "qwen2.5:7b",
        "Agents": "6",
        "Tools": "Code Execution, Web Search"
    }
    
    for key, value in system_info.items():
        col1, col2 = st.columns(2)
        with col1:
            st.text(key)
        with col2:
            st.text(value)
    
    # Reset button
    st.markdown("---")
    if st.button("🔄 Reset System", type="secondary"):
        st.session_state.orchestrator = None
        st.session_state.workflow_manager = None
        st.session_state.conversation_history = []
        st.session_state.chat_history = []
        st.success("System reset complete. Refresh page to reinitialize.")
        st.rerun()


# Workflow execution functions
def run_example(example_name):
    """Run an example workflow"""
    st.success(f"Running example: {example_name}")
    # Add execution logic here


def run_eda_workflow(dataset_path):
    """Run EDA workflow"""
    with st.spinner("Running EDA workflow..."):
        try:
            results = st.session_state.workflow_manager.exploratory_data_analysis(
                dataset_path
            )
            st.success("✅ EDA completed successfully!")
            st.json(results)
        except Exception as e:
            st.error(f"Error: {e}")


def run_ml_workflow(dataset_path, task_type):
    """Run ML pipeline workflow"""
    with st.spinner("Running ML pipeline..."):
        try:
            results = st.session_state.workflow_manager.ml_modeling_pipeline(
                dataset_path,
                task_type
            )
            st.success("✅ ML pipeline completed successfully!")
            st.json(results)
        except Exception as e:
            st.error(f"Error: {e}")


def run_deployment_workflow(model_path, model_type):
    """Run deployment workflow"""
    with st.spinner("Setting up model deployment..."):
        try:
            results = st.session_state.workflow_manager.deploy_model(
                model_path,
                model_type
            )
            st.success("✅ Deployment setup completed!")
            st.json(results)
        except Exception as e:
            st.error(f"Error: {e}")


def run_custom_workflow(query, agent_sequence):
    """Run custom workflow"""
    with st.spinner(f"Running workflow with {len(agent_sequence)} agents..."):
        try:
            results = st.session_state.orchestrator.run_data_science_pipeline(
                query,
                agent_sequence=agent_sequence
            )
            st.success("✅ Custom workflow completed!")
            
            # Display results
            for agent_name, result in results.items():
                with st.expander(f"Results from {agent_name}"):
                    st.text(str(result)[:500])
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()

