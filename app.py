import streamlit as st
import os
from dotenv import load_dotenv
from state import TravelState
from graph import build_graph

# Load API Key
load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="🌍", layout="centered")

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def is_valid_destination(place_name):
    """Uses Groq LLM to strictly verify if the input is a real location."""
    try:
        llm = ChatGroq(model="llama3-8b-8192", temperature=0)
        prompt = f"""You are a strict geography validator. 
User entered: '{place_name}'
Is this a real, existing geographical location, city, country, or well-known travel destination?
Ignore letter spam like 'abc', 'xyz', 'asdf', or imaginary places.
Reply EXACTLY with the word 'YES' or 'NO' and nothing else."""
        
        response = llm.invoke([HumanMessage(content=prompt)])
        answer = response.content.strip().upper()
        
        # Strictly check for exact 'YES' or starting with 'YES' to avoid false positives
        return answer == "YES" or answer.startswith("YES")
    except Exception:
        # If API fails for some reason during check, fallback to True to not block the user
        return True

# --- CUSTOM CSS FOR PREMIUM LOOK ---
st.markdown("""
<style>
    /* Main Background & Font applied by config.toml, this adds extra polish */
    
    /* Center the subtitle */
    .st-emotion-cache-1y4p8pa, .st-emotion-cache-16idsys p {
        text-align: center;
        color: #94A3B8;
        font-size: 1.1rem;
    }

    /* Style the form container */
    div[data-testid="stForm"] {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        padding: 24px;
        margin-top: 20px;
    }

    /* Form Submit Button (Green Glow Effect) */
    button[kind="formSubmit"] {
        width: 100%;
        background: linear-gradient(135deg, #00C853, #00A344) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        padding: 12px !important;
        box-shadow: 0 4px 14px rgba(0, 200, 83, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    button[kind="formSubmit"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 200, 83, 0.6) !important;
    }

    /* Input Fields Styling to make them look like distinct, empty boxes */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: #0F172A !important; /* Darker background to contrast with the form */
        border: 1px solid #475569 !important; /* Visible outline box */
        border-radius: 8px !important;
    }
    
    div[data-baseweb="input"] > div:focus-within, div[data-baseweb="select"] > div:focus-within {
        border: 1px solid #00C853 !important; /* Green glow when typing */
        box-shadow: 0 0 0 1px #00C853 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI Travel Planner")
st.write("Generate personalized travel itineraries powered by Groq and LangGraph!")

# Create a form for user input
with st.form("travel_form"):
    destination = st.text_input("✈️ Where do you want to go?", placeholder="e.g. Bali, Paris, Tokyo")
    duration = st.number_input("📅 How many days?", min_value=1, max_value=30, value=3)
    budget = st.selectbox("💳 What is your budget level?", ["Budget", "Mid-range", "Luxury"])
    
    submitted = st.form_submit_button("Plan My Trip! 🚀")

if submitted:
    if not destination.strip():
        st.error("Please enter a destination!")
    else:
        # Step 1: Validate location
        is_valid = False
        with st.spinner(f"Verifying location '{destination}' exists..."):
            is_valid = is_valid_destination(destination)
            
        if not is_valid:
            st.error(f"❌ '{destination}' does not appear to be a valid real-world location. Please enter a valid city, country, or tourist destination.")
        else:
            # Step 2: Generate itinerary
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
                    st.error(f"An error occurred while building the plan: {e}")
