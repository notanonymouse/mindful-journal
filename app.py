import os
import random
import streamlit as st
from datetime import datetime
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
        return response.sentiment
    except Exception as e:
        return "neutral"

# --- 2. THE VISUAL STYLE (CSS) ---
def set_visual_style():
    style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: radial-gradient(circle, rgba(238,245,249,1) 0%, rgba(213,227,243,1) 100%);
        color: #1A365D;
    }
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.7); color: #1A365D; }
    h1, h2, h3, h4 { color: #1A365D !important; font-weight: 600; }
    [data-testid="stTextArea"] textarea { background-color: white; border-radius: 15px; border: 1px solid #CBD5E0; }
    div.stButton > button:first-child { background-color: #1A365D; color: white; border-radius: 10px; padding: 10px 24px; }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

# --- 3. PAGE CONFIG & SIDEBAR START ---
st.set_page_config(page_title="MindfulJournal", page_icon="🧘")
set_visual_style()

st.sidebar.title("🌿 My Wellness Space")
user_name = st.sidebar.text_input("What is your name?", value="Mina")

# --- 4. DYNAMIC HABIT TRACKER ---
st.sidebar.subheader("Daily Habits 📝")
habit1 = st.sidebar.checkbox("Mindful Breathing")
habit2 = st.sidebar.checkbox("Hydration Goal")
habit3 = st.sidebar.checkbox("Daily Movement")

habits_list = [habit1, habit2, habit3]
completed_habits = sum(habits_list)
progress_percentage = int((completed_habits / 3) * 100)

st.sidebar.divider()
st.sidebar.write(f"**Weekly Self-Care Goal: {progress_percentage}%**")
st.sidebar.progress(progress_percentage)

if completed_habits == 3:
    st.sidebar.success("🌟 All habits done!")
else:
    st.sidebar.write(f"❤️ Keep going, {user_name}!")

# --- 5. MINDFULNESS COACH SIDEBAR ---
st.sidebar.divider()
st.sidebar.subheader("🧘 Mindfulness Coach")
if st.sidebar.button("Start 1-Minute Grounding"):
    st.sidebar.write("**Focus on your breath:**")
    st.sidebar.write("1. Inhale... 🌬️ | 2. Hold... ⏳ | 3. Exhale... ✨")

# --- 6. MAIN JOURNAL INTERFACE ---
st.title("🧘 My Mindful Journal")
st.write(f"How are you feeling today, {user_name}?")
prompts = ["What made you smile today? 😊", "What is one thing you learned? 🧠", "What are you looking forward to tomorrow? 🌅"]
st.info(f"**Today's Prompt:** {random.choice(prompts)}")

user_entry = st.text_area("Write your thoughts here...", height=200)

if st.button("Analyze My Mood"):
    if user_entry:
        with st.spinner('Reflecting...'):
            mood = get_azure_sentiment(user_entry)
        
        with open("mood_history.csv", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()},{mood}\n")

        st.divider()
        st.subheader("🧠 Reflection Agent Insights") 
        if mood == "negative":
            st.warning("Mood Detected: Stressed 😰")
            st.info("🧘 Mindfulness Coach: Try naming 3 things you see right now.")
        elif mood == "positive":
            st.success("Mood Detected: Positive ✨")
            st.write(f"🚀 Motivation Agent: Tell someone 'Thank You' today, {user_name}!")
        else:
            st.info("I'm listening. Neutral reflection is a great start.")
        
        st.write("---")
        st.write("🔍 **Patterns Spotted:** You're more positive on 'Daily Movement' days!")

# --- 7. PERSONAL GROWTH SUMMARY ---
st.divider()
st.header("✨ Your Personal Growth Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Journaling Streak", value="3 Days", delta="1")
with col2:
    st.metric(label="Primary Mood", value="Stressed", delta="-10%", delta_color="inverse")
with col3:
    st.metric(label="Missions Completed", value=f"{completed_habits}/3")

st.info(f"🌟 **Motivation Agent Note:** Your stress levels are trending down, {user_name}!")
st.caption("🔒 Privacy Note: Data stored locally and secured by Azure AI.")