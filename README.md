# 🌍 AI Travel Planner — Powered by LangGraph

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Enabled-orange.svg)](https://python.langchain.com/docs/langgraph)
[![Groq](https://img.shields.io/badge/LLM-Groq-green.svg)](https://groq.com)

An intelligent multi-agent travel planning system that generates personalized travel itineraries based on user preferences like destination, duration, and budget.

---

## ✨ Features

- **🤖 Multi-agent architecture** using LangGraph
- **🔍 Research Agent** → Finds relevant travel info
- **📅 Itinerary Agent** → Plans day-wise schedule
- **💰 Budget Agent** → Estimates and optimizes costs
- **✅ Review Agent** → Refines and improves final output
- **⚡ Fast responses** using Groq LLM

## 🧠 How It Works

1. **User enters:**
   - Destination
   - Number of days
   - Budget level (e.g., Budget, Moderate, Luxury)

2. **Agents collaborate:**
   - **Research:** Gathers info about the destination
   - **Itinerary:** Creates a detailed daily plan
   - **Budget:** Estimates the cost of the trip
   - **Review:** Optimizes the final itinerary

3. **Output:** A nicely structured and detailed travel plan is generated! 🎯

## 🛠️ Tech Stack

- **[Python](https://python.org/)**
- **[LangGraph](https://python.langchain.com/docs/langgraph/)** & **[LangChain](https://www.langchain.com/)**
- **[Groq API](https://groq.com/)**
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**

---

## 📂 Project Structure

```text
Travel_Planner/
│
├── agents/
│   ├── research_agent.py
│   ├── itinerary_agent.py
│   ├── budget_agent.py
│   └── review_agent.py
│
├── main.py
├── graph.py
├── state.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sejalkutriyar/AI-Travel-Planner-Agent.git
cd AI-Travel-Planner-Agent
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup environment variables
Create a `.env` file in the root directory:
```bash
GROQ_API_KEY=your_api_key_here
```
> ⚠️ **Security Note:** Never share your `.env` file publicly. API keys are stored using environment variables and `.env` is excluded via `.gitignore`. Sensitive data should not be committed to the repository.

### 4️⃣ Run the project
```bash
python main.py
```

---

## 📸 Example Output

**6-day trip to Tokyo (Budget)**

- **Day 1:** Arrival + local exploration
- **Day 2:** Cultural sites
- **Day 3:** Food tour
- *...*

---

## 🚀 Future Improvements

- [ ] Add a Web UI (React / Streamlit)
- [ ] Integrate real-time flight & hotel APIs
- [ ] Add map visualizations
- [ ] Save user travel history

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit a PR to improve the project.