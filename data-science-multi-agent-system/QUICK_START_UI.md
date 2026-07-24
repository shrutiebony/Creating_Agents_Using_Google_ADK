# 🚀 Quick Start with the Beautiful UI

## Step 1: Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install Ollama (if not already installed)
# Visit: https://ollama.com

# Pull the model
ollama pull qwen2.5:7b
```

## Step 2: Launch the UI

### Option A: Using the Launcher (Easiest)

```bash
python run_ui.py
```

### Option B: Using Streamlit Directly

```bash
streamlit run app.py
```

The UI will automatically open in your browser at:
👉 **http://localhost:8501**

## Step 3: Explore the UI

### 🏠 Home Page
- See quick action buttons
- Browse example workflows
- View recent activity

### 💬 Chat Page  
- Select an agent from the buttons
- Ask questions in the chat input
- Get real-time AI responses

### ⚙️ Workflows Page
- Choose from 3 workflow types
- Or create custom workflows
- Run complete data science pipelines

### 📊 Analytics Page
- Monitor system health
- View activity log
- Export your results

### ⚙️ Settings Page
- Configure agents
- Adjust model settings
- View system information

## 🎨 UI Preview

### Home Screen
```
┌─────────────────────────────────────────────────┐
│         🤖 Data Science AI Agents               │
│   AI-Powered Multi-Agent System for Data        │
├─────────────────────────────────────────────────┤
│  Quick Actions:                                  │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
│  │ 📊 Quick│  │ 🧠 ML   │  │ 🚀 Deploy│         │
│  │    EDA  │  │ Modeling│  │   Model │         │
│  └─────────┘  └─────────┘  └─────────┘         │
│                                                 │
│  Example Workflows:                             │
│  • Iris Classification                          │
│  • Wine Quality Analysis                        │
│  • House Price Prediction                       │
└─────────────────────────────────────────────────┘
```

### Chat Interface
```
┌─────────────────────────────────────────────────┐
│  💬 Chat with AI Agents                         │
├─────────────────────────────────────────────────┤
│  [🎯] [📊] [🧠] [🎨] [⚙️] [🚀]                  │
│                                                 │
│  🤖 Chatting with: Data Analyst                 │
├─────────────────────────────────────────────────┤
│  User: What is exploratory data analysis?       │
│  Agent: EDA involves summarizing...            │
│                                                 │
│  ┌────────────────────────────────────────────┐│
│  │ Ask your agent a question...               ││
│  └────────────────────────────────────────────┘│
└─────────────────────────────────────────────────┘
```

## 🎯 Try These Examples

### Example 1: Quick Chat
1. Go to **Chat Page**
2. Click **📊 Data Analyst**
3. Type: "Explain exploratory data analysis"
4. See the detailed response!

### Example 2: Run EDA
1. Go to **Workflows Page**
2. Select **Exploratory Analysis** tab
3. Enter: `iris`
4. Click **Run EDA Workflow**
5. Watch the results appear!

### Example 3: ML Pipeline
1. Go to **Workflows Page**
2. Select **ML Pipeline** tab
3. Enter: `wine`
4. Select: `classification`
5. Click **Run ML Pipeline**
6. Get a trained model!

## 💡 Tips & Tricks

1. **Use Sidebar**: Quick navigation to different sections
2. **Browse Agents**: See what each agent can do
3. **Check Activity**: Monitor all your workflows
4. **Export Results**: Save your work as JSON
5. **Customize**: Modify settings for your needs

## 🎨 UI Features

✅ **Beautiful Gradient Theme** - Purple gradient colors
✅ **Interactive Cards** - Hover effects and animations
✅ **Real-time Updates** - See results as they happen
✅ **Chat Interface** - Talk with AI agents
✅ **Workflow Management** - Orchestrate multi-agent tasks
✅ **Analytics Dashboard** - Monitor system health
✅ **Settings Panel** - Configure everything

## 🐛 Troubleshooting

### UI Not Loading?
```bash
# Check if port is in use
netstat -ano | findstr :8501  # Windows
lsof -i :8501  # Mac/Linux

# Use different port
streamlit run app.py --server.port=8502
```

### Model Not Found?
```bash
# Pull the model
ollama pull qwen2.5:7b

# List available models
ollama list
```

### Slow Performance?
- Use smaller datasets
- Close other applications
- Check system resources

## 🚀 Next Steps

1. ✅ Start the UI
2. ✅ Try example workflows
3. ✅ Chat with agents
4. ✅ Create custom workflows
5. ✅ Export your results

## 📚 More Information

- **Full Guide**: See `UI_GUIDE.md`
- **Architecture**: See `ARCHITECTURE.md`
- **Examples**: See `examples.py`
- **Improvements**: See `IMPROVEMENTS.md`

## 🎉 You're Ready!

Your beautiful Data Science Agent UI is ready to use!

```bash
python run_ui.py
```

Enjoy your AI-powered data science! 🚀🤖

