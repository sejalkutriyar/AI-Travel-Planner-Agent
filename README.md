✅ 📄 README.md (Use this template)
🌍 AI Travel Planner — Powered by LangGraph

An intelligent multi-agent travel planning system that generates personalized travel itineraries based on user preferences like destination, duration, and budget.

✨ Features
🤖 Multi-agent architecture using LangGraph
🔍 Research Agent → Finds travel info
📅 Itinerary Agent → Plans day-wise schedule
💰 Budget Agent → Estimates cost
✅ Review Agent → Improves final output
⚡ Fast responses using Groq LLM
🧠 How It Works
User enters:
Destination
Number of days
Budget level
Agents collaborate:
Research → gathers info
Itinerary → creates plan
Budget → estimates cost
Review → final optimization
Final structured travel plan is generated 🎯
🛠️ Tech Stack
Python
LangGraph
LangChain
Groq API
dotenv
📂 Project Structure
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
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/your-username/AI-Travel-Planner-Agent.git
cd AI-Travel-Planner-Agent
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Setup environment variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

⚠️ Never share your .env file publicly

4️⃣ Run the project
python main.py
📸 Example Output
6-day trip to Tokyo (Budget)

Day 1: Arrival + local exploration
Day 2: Cultural sites
Day 3: Food tour
...
🔐 Security Note
API keys are stored using environment variables
.env is excluded via .gitignore
Sensitive data is not committed to the repository
🚀 Future Improvements
Add UI (React / Streamlit)
Integrate real-time flight & hotel APIs
Add map visualization
Save user travel history
🤝 Contributing

Feel free to fork the repo and improve the project!