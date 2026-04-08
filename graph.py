# graph.py — LANGGRAPH WORKFLOW
# here we build a graph
# Node  = an agent
# Edge  = which agent will run after which agent
# Flow  = Research → Itinerary → Budget → Review → END

from langgraph.graph import StateGraph, END
from state import TravelState

from agents.research_agent   import research_agent
from agents.itinerary_agent  import itinerary_agent
from agents.budget_agent     import budget_agent
from agents.review_agent     import review_agent


def build_graph():
    # initialize graph with our shared state
    graph = StateGraph(TravelState)

    # add nodes (each node = an agent)
    graph.add_node("research",  research_agent)
    graph.add_node("itinerary", itinerary_agent)
    graph.add_node("budget",    budget_agent)
    graph.add_node("review",    review_agent)

    # add edges (define execution flow)
    graph.set_entry_point("research")         # Step 1: Research
    graph.add_edge("research",  "itinerary")  # Step 2: Itinerary
    graph.add_edge("itinerary", "budget")     # Step 3: Budget
    graph.add_edge("budget",    "review")     # Step 4: Review
    graph.add_edge("review",    END)          # Done!

    return graph.compile()