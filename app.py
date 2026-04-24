import random
import streamlit as st

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
# 1. The Input Field
user_entry = st.text_area("Write your thoughts here...", height=200)

if st.button("Analyze My Mood"):
    if user_entry:
        # 2. Simple 'Logic' (This is a placeholder for Azure AI)
        st.divider()
        st.subheader("Assistant Analysis")
        
        # We search for keywords to suggest actions
        if "stressed" in user_entry.lower() or "overwhelmed" in user_entry.lower():
            st.warning("Mood Detected: Stressed 😰")
            st.write("### Suggestion: 1-Minute Grounding")
            st.info("Stop what you are doing. Name 3 things you can see and 2 things you can hear right now.")
        
        elif "happy" in user_entry.lower() or "great" in user_entry.lower():
            st.success("Mood Detected: Positive ✨")
            st.write("### Investigator Challenge: Savoring the Evidence")
            st.write("Since you're feeling great, your mission is to tell one person 'Thank You' today. It strengthens your positive 'paper trail'!")
            
            if st.button("Mission Accepted!"):
                st.confetti()
                st.balloons()
                
        elif "sad" in user_entry.lower() or "bad" in user_entry.lower():
            st.error("Mood Detected: Sad 😔")
            st.write("### A Virtual Hug for You")
            st.write("I'm so sorry you're feeling this way, Mina. Remember that it's okay to have bad days.")
            st.info("💡 Try this: Name one thing, no matter how small, that made you smile today.") 
        else:
            st.info("I'm listening. Reflecting on your thoughts is a great first step.")
            
        
    else:
        st.error("Please write something first!")

# # Sidebar for the 'Supportive Friend' vibe
st.sidebar.title("🌿 My Wellness Space")
st.sidebar.write("Tracking your self-care journey")
st.sidebar.progress(40, text="Weekly Self-Care Goal")
st.sidebar.write("❤️ Keep going, Mina!")

# --- Mental Forensic Report Section ---
st.divider()
st.header("✨ Your Personal Growth Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Journaling Streak", value="3 Days", delta="1")
with col2:
    st.metric(label="Primary Mood", value="Stressed", delta="-10%", delta_color="inverse")
with col3:
    st.metric(label="Missions Completed", value="2/5")

st.info("💡Warm Note from your Assistant: Your stress levels are down 10% compared to last week. Great work!")