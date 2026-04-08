# work: gather background info about the destination
# Input:  state["destination"], state["duration"]
# Output: state["research_output"]

import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from state import TravelState


def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7
    )


def research_agent(state: TravelState) -> TravelState:
    print("\n🔍 Research Agent is working...")

    llm = get_llm()
    prompt = f"""
    You are a travel research expert.
    Destination: {state['destination']}
    Trip Duration: {state['duration']} days

    Please provide:
    1. Top 5 must-visit attractions
    2. Best time to visit & current weather
    3. Local culture & customs to know
    4. Top 3 local foods to try
    5. Safety tips for travelers

    Keep it concise and practical.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["research_output"] = response.content
    print("✅ Research complete!")
    return state