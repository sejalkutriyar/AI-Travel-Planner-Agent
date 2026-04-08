# work: make a day-by-day plan based on research
# Input:  state["research_output"], state["duration"], state["budget"]
# Output: state["itinerary_output"]

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


def itinerary_agent(state: TravelState) -> TravelState:
    print("\n🗓️  Itinerary Agent is working...")

    llm = get_llm()
    prompt = f"""
    You are an expert travel planner.
    Destination: {state['destination']}
    Duration: {state['duration']} days
    Budget Level: {state['budget']}

    Based on this research:
    {state['research_output']}

    Create a detailed day-by-day itinerary:
    - Morning, Afternoon, Evening activities for each day
    - Recommended restaurants for each day
    - Travel tips between locations
    - Estimated time at each spot

    Format clearly as Day 1, Day 2, etc.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["itinerary_output"] = response.content
    print("✅ Itinerary ready!")
    return state