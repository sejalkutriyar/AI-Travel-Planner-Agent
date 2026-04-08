# ============================================================
# state.py — SHARED STATE
# Yeh dictionary saare agents ke beech share hoti hai.
# Har agent is state ko read karta hai aur apna result likhta hai.
# ============================================================

from typing import TypedDict


class TravelState(TypedDict):
    destination: str         # where user want to go
    duration: str            # trip for how many days
    budget: str              # Budget level
    research_output: str     # Agent 1 output
    itinerary_output: str    # Agent 2 output
    budget_output: str       # Agent 3 output
    final_output: str        # Agent 4 output