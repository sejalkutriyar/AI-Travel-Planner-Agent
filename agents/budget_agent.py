# work: make a cost breakdown of the whole trip
# Input:  state["destination"], state["duration"],
#         state["budget"], state["itinerary_output"]
# Output: state["budget_output"]

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


def budget_agent(state: TravelState) -> TravelState:
    print("\n💰 Budget Agent is working...")

    llm = get_llm()
    prompt = f"""
    You are a travel budget specialist.
    Destination: {state['destination']}
    Duration: {state['duration']} days
    Budget Level: {state['budget']}

    Based on this itinerary:
    {state['itinerary_output']}

    Provide a realistic budget breakdown in INR (Indian Rupees):
    1. Flights (round trip estimate)
    2. Accommodation (per night x days)
    3. Food & Dining (per day estimate)
    4. Local Transport (per day)
    5. Attractions & Entry fees
    6. Shopping & Miscellaneous
    7. TOTAL ESTIMATED COST

    Also give 3 money-saving tips for this destination.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["budget_output"] = response.content
    print("✅ Budget breakdown ready!")
    return state