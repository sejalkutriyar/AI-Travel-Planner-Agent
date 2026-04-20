import streamlit as st
import os
from dotenv import load_dotenv
from state import TravelState
from graph import build_graph

# Load API Key
load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="🌍")

st.title("🌍 AI Travel Planner — Powered by LangGraph")
st.write("Generate personalized travel itineraries powered by Groq and LangGraph!")

# Create a form for user input
with st.form("travel_form"):
    destination = st.text_input("✈️ Where do you want to go?", placeholder="e.g. Bali, Paris, Tokyo")
    duration = st.number_input("📅 How many days?", min_value=1, max_value=30, value=3)
    budget = st.selectbox("💳 What is your budget level?", ["Budget", "Mid-range", "Luxury"])
    
    submitted = st.form_submit_button("Plan My Trip! 🚀")

if submitted:
    if not destination:
        st.error("Please enter a destination!")
    else:
        with st.spinner(f"Agents are planning your {duration}-day trip to {destination}..."):
            try:
                # Prepare initial state
                initial_state: TravelState = {
                    "destination": destination,
                    "duration": str(duration),
                    "budget": budget,
                    "research_output": "",
                    "itinerary_output": "",
                    "budget_output": "",
                    "final_output": ""
                }

                # Run the graph
                app = build_graph()
                result = app.invoke(initial_state)

                # Show Final Result
                st.success("🎉 Your travel plan is ready!")
                st.markdown(result["final_output"])
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
