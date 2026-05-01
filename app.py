import os
import random
import streamlit as st
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# --- 1. SET UP THE BRAIN (Azure Connection) ---
load_dotenv()
key = os.getenv("AZURE_LANGUAGE_KEY")
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")

def get_azure_sentiment(text):
    try:
        client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
        response = client.analyze_sentiment(documents=[text])[0]
        return response.sentiment  # Returns 'positive', 'neutral', or 'negative'
    except Exception as e:
        return "neutral" # Fallback if Azure is busy

# --- 2. THE APP INTERFACE (Streamlit) ---
st.set_page_config(page_title="MindfulJournal", page_icon="🧘")

st.title("🧘 My Mindful Journal")
st.write("How are you feeling today, Mina?")

affirmations = [
    "You are doing enough, even on the days you don't feel like it. ✨",
    "Transitioning careers is brave. Keep going! 🚀",
    "Your progress matters more than your speed. 🐢",
    "Don't forget to breathe today. You've got this!"
]

st.info(random.choice(affirmations))

user_entry = st.text_area("Write your thoughts here...", height=200)

if st.button("Analyze My Mood"):
    if user_entry:
        # --- 3. THE MAGIC HAPPENS HERE ---
        # We use Azure instead of just looking for keywords!
        with st.spinner('Azure AI is reflecting on your thoughts...'):
            mood = get_azure_sentiment(user_entry)
        
        st.divider()
        st.subheader("Assistant Analysis")
        
        if mood == "negative":
            st.warning("Azure AI Detected: You seem to be having a hard time 😰")
            st.write("### Suggestion: 1-Minute Grounding")
            st.info("Stop what you are doing. Name 3 things you can see and 2 things you can hear right now.")
        
        elif mood == "positive":
            st.success("Azure AI Detected: You're in a great head space! ✨")
            st.write("### Investigator Challenge: Savoring the Evidence")
            st.write("Your mission is to tell one person 'Thank You' today!")
                
        else:
            st.info("Azure AI Detected: Balanced & Neutral. I'm listening. Reflecting on your thoughts is a great first step.")
    else:
        st.error("Please write something first!")

# --- Sidebar & Metrics (Keep these as they are!) ---
st.sidebar.title("🌿 My Wellness Space")
st.sidebar.write("Tracking your self-care journey")
st.sidebar.progress(40, text="Weekly Self-Care Goal")

st.divider()
st.header("✨ Your Personal Growth Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Journaling Streak", value="3 Days", delta="1")
with col2:
    st.metric(label="Primary Mood", value="Stressed", delta="-10%", delta_color="inverse")
with col3:
    st.metric(label="Missions Completed", value="2/5")
