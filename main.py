# main.py — ENTRY POINT
# here the program starts
# takes input from user and runs the graph

import os
from dotenv import load_dotenv
from state import TravelState
from graph import build_graph

# load API key from .env file
load_dotenv()


def main():
    print("=" * 55)
    print("   🌍  AI TRAVEL PLANNER — Powered by LangGraph")
    print("=" * 55)

    # take input from user
    destination = input("\n✈️  Where do you want to go? (e.g. Bali, Paris, Tokyo): ").strip()
    duration    = input("📅  How many days for the trip? (e.g. 5): ").strip()
    budget      = input("💳  What is your budget level? (Budget / Mid-range / Luxury): ").strip()

    print(f"\n🚀 Planning your {duration}-day trip to {destination}...")
    print("-" * 55)

    # make initial state
    initial_state: TravelState = {
        "destination":      destination,
        "duration":         duration,
        "budget":           budget,
        "research_output":  "",
        "itinerary_output": "",
        "budget_output":    "",
        "final_output":     ""
    }

    # build graph and run it
    app    = build_graph()
    result = app.invoke(initial_state)

    # print final output
    print("\n" + "=" * 55)
    print("   🎉  YOUR TRAVEL PLAN IS READY!")
    print("=" * 55)
    print(result["final_output"])
    print("\n" + "=" * 55)
    print("   Bon Voyage! Have an amazing trip! ✈️")
    print("=" * 55)


if __name__ == "__main__":
    main()