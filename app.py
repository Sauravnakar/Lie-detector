import streamlit as st
import time
import random

# 1. Setup the Page
st.set_page_config(page_title="Saurav's Polygraph", page_icon="🕵️‍♂️", layout="centered")

st.title("🕵️‍♂️ The Ultimate Lie Detector")
st.write("My algorithms are highly advanced. Type a statement you think is true, and let's see if you are lying.")
st.divider()

# 2. The Input
statement = st.text_input("Enter a statement (e.g., 'I am the best PUBG player'):")

# 3. The Interactive Game Engine
if st.button("Run Analysis", use_container_width=True):
    if statement:
        # The Fake Loading Bar (The funny part)
        progress_text = "Connecting to the mainframe..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.04)  # Makes the loading bar take a few seconds
            if percent_complete == 30:
                my_bar.progress(percent_complete + 1, text="Analyzing brainwaves...")
            elif percent_complete == 60:
                my_bar.progress(percent_complete + 1, text="Detecting massive amounts of lag in your logic...")
            elif percent_complete == 85:
                my_bar.progress(percent_complete + 1, text="Finalizing polygraph results...")
            else:
                my_bar.progress(percent_complete + 1, text=progress_text)
        
        time.sleep(0.5)
        my_bar.empty() # Clears the loading bar

        # 4. The Roasts (It always says she is lying)
        roasts = [
            "🚨 100% CAP. The system detects a massive lie.",
            "🚨 ERROR: Statement is so false it almost crashed my server.",
            "✅ TRUE. Wait, no... algorithm recalibrating... 🚨 FALSE. Definitely a lie.",
            "🚨 99.9% FALSE. The 0.1% is just pity points.",
            "🚨 FALSE. Even the AI is laughing at this statement."
        ]

        st.error(random.choice(roasts))
    else:
        st.warning("You have to actually type something, Boss.")
