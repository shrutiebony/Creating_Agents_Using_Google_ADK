# Beautiful UI Guide

## 🎨 Welcome to the Data Science Agent UI

The UI is built with Streamlit - a modern, beautiful, and interactive web interface.

## 🚀 Getting Started

### Quick Start

```bash
# Run the launcher
python run_ui.py

# Or run directly with streamlit
streamlit run app.py
```

The UI will automatically open in your browser at `http://localhost:8501`

## 📱 UI Features

### 1. 🏠 Home Page

**Quick Actions:**
- 📊 Quick EDA - Perform exploratory data analysis
- 🧠 ML Modeling - Build machine learning models
- 🚀 Model Deployment - Deploy trained models

**Example Workflows:**
- Iris Classification
- Wine Quality Analysis
- House Price Prediction
- Customer Segmentation

### 2. 💬 Chat Page

**Interactive Chat with Agents:**
- Select any agent from the top buttons
- Chat directly with specialized agents
- Real-time responses
- Conversation history

**Available Agents:**
- 🎯 Orchestrator - Coordinates all agents
- 📊 Data Analyst - EDA and statistics
- 🧠 ML Engineer - Model development
- 🎨 Visualization - Charts and plots
- ⚙️ Data Engineer - ETL pipelines
- 🚀 Deployment - Model serving

### 3. ⚙️ Workflows Page

**Three Workflow Types:**

#### Tab 1: 📊 Exploratory Analysis
- Input: Dataset path or sklearn dataset name
- Click "Run EDA Workflow"
- Automatic data analysis and visualization

#### Tab 2: 🧠 ML Pipeline
- Input: Dataset path
- Select task type (classification/regression/clustering)
- Complete ML pipeline from data to model

#### Tab 3: 🚀 Deployment
- Input: Model path
- Select model type
- Create deployment-ready APIs

**Custom Workflow:**
- Describe your custom task
- Select which agents to use
- Run fully customized workflows

### 4. 📊 Analytics Page

**System Health Dashboard:**
- Agent status
- Workflow count
- System status
- Last activity

**Activity Log:**
- Complete history of all workflows
- Timestamps for each activity
- Expandable details

**Export Results:**
- Download all results as JSON
- Archive your workflow history

### 5. ⚙️ Settings Page

**Model Configuration:**
- View current model
- Change model settings
- Model information

**Agent Settings:**
- Enable/disable agents
- Configure agent behavior

**System Information:**
- Framework details
- Backend information
- Available tools

**Reset System:**
- Reset all state
- Clear history
- Fresh start

## 🎨 Beautiful Design Features

### Visual Elements

1. **Gradient Headers**
   - Purple gradient theme
   - Modern and professional

2. **Agent Cards**
   - Hover effects
   - Shadow and animations
   - Icon-based display

3. **Interactive Buttons**
   - Gradient styling
   - Hover animations
   - Smooth transitions

4. **Status Indicators**
   - Success boxes (green)
   - Info boxes (blue)
   - Color-coded metrics

5. **Responsive Layout**
   - Wide layout for better UX
   - Collapsible sidebar
   - Column-based organization

## 💡 Usage Tips

### Tip 1: Start with Examples
- Go to Home page
- Try the example workflows
- See how different agents work together

### Tip 2: Use Quick Actions
- Navigate to Workflows
- Select a predefined workflow
- Enter your data path
- Click run and watch the magic!

### Tip 3: Chat with Agents
- Go to Chat page
- Select an agent
- Ask specific questions
- Get detailed responses

### Tip 4: Monitor Activity
- Check Analytics page
- Track all your workflows
- Export results when done

## 🔧 Customization

### Change Theme Colors

Edit the CSS in `app.py`:

```python
st.markdown("""
    <style>
    /* Change gradient colors */
    background: linear-gradient(90deg, #your_color1 0%, #your_color2 100%);
    </style>
""", unsafe_allow_html=True)
```

### Add Custom Workflows

Edit `workflows_page()` in `app.py`:

```python
if st.button("My Custom Workflow"):
    # Your workflow logic here
    pass
```

### Modify Agent Cards

Edit the `display_agent_card()` function:

```python
def display_agent_card(name, description, icon):
    st.markdown(f"""
        <div class="agent-card">
            <h3>{icon} {name}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)
```

## 📊 Keyboard Shortcuts

- `R` - Refresh data
- `Ctrl+C` - Stop server
- `Ctrl+R` - Reload page

## 🐛 Troubleshooting

### UI Won't Start

```bash
# Make sure dependencies are installed
pip install -r requirements.txt

# Check if port 8501 is available
# If not, streamlit will use the next available port
```

### Browser Issues

1. Try a different browser
2. Clear browser cache
3. Check browser console for errors

### Slow Performance

1. Use smaller datasets for testing
2. Close other applications
3. Consider using a GPU for Ollama

## 🎯 Best Practices

1. **Start Small**: Begin with simple examples
2. **Read Responses**: Agent outputs are detailed
3. **Save Results**: Export important workflows
4. **Use Chat**: Ask agents for explanations
5. **Check Settings**: Configure before complex tasks

## 🚀 Advanced Usage

### Custom CSS

Add your own styles in the `<style>` section:

```python
st.markdown("""
    <style>
    .my-custom-class {
        /* Your custom styles */
    }
    </style>
""", unsafe_allow_html=True)
```

### Custom Components

Create reusable components:

```python
def my_custom_component():
    st.markdown("### My Component")
    # Your logic here
```

## 📸 Screenshots

The UI includes:
- 🎨 Beautiful gradient themes
- 📊 Interactive dashboards
- 💬 Chat interface
- ⚙️ Workflow management
- 📈 Analytics and metrics

## 🎉 Enjoy!

You now have a beautiful, modern UI for your Data Science Agent System!

```bash
# Start using it now
python run_ui.py
```

Happy Data Science! 🚀

