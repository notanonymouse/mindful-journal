import streamlit as st

st.set_page_config(page_title="MindfulJournal", page_icon="🧘")

st.title("🧘 My Mindful Journal")
st.write("How are you feeling today, Yagmur?")

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
        else:
            st.info("I'm listening. Reflecting on your thoughts is a great first step.")
            
        st.balloons()
    else:
        st.error("Please write something first!")

# Sidebar for the 'Forensic' twist
st.sidebar.title("Growth Investigation")
st.sidebar.write("Tracking your mental 'evidence'")
st.sidebar.progress(40, text="Weekly Consistency")