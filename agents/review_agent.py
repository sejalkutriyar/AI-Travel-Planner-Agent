# work: review all outputs and create one polished final plan
# Input:  previous state outputs
# Output: state["final_output"]

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


def review_agent(state: TravelState) -> TravelState:
    print("\n✅ Review Agent is making final plan...")

    llm = get_llm()
    prompt = f"""
    You are a senior travel consultant doing a final review.
    Destination: {state['destination']}
    Duration: {state['duration']} days
    Budget: {state['budget']}

    You have received:
    RESEARCH:  {state['research_output']}
    ITINERARY: {state['itinerary_output']}
    BUDGET:    {state['budget_output']}

    Create ONE beautiful, complete travel plan that:
    1. Starts with a short exciting intro about the destination
    2. Includes the day-by-day itinerary (neatly formatted)
    3. Includes the budget breakdown
    4. Ends with 5 pro travel tips
    5. Makes the traveler excited about the trip!

    Format it nicely with emojis and clear sections.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["final_output"] = response.content
    print("✅ Final plan ready!")
    return state