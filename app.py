import streamlit as st
import time
import random

# 1. Setup the Page
st.set_page_config(page_title="Cinematic Vibe Check", page_icon="✨", layout="centered")

# 2. The Positive Aesthetic Database
# 100% compliments, zero roasts. Fun, cool, and confident.
aesthetics = [
    {
        "title": "🎬 The K-Drama Lead", 
        "desc": "Main character energy activated. You look like the protagonist who is about to inherit a massive company or completely change someone's life. 10/10 screen presence."
    },
    {
        "title": "🌃 The Berlin Local", 
        "desc": "Effortlessly cool. You look like you know the password to every secret cafe in the city and always have the best music playlist. Elite street-style energy."
    },
    {
        "title": "🎥 The Movie Trailer Protagonist", 
        "desc": "The lighting and the vibe are flawless. The algorithm is genuinely confused if this is a live selfie or a screenshot from an upcoming movie."
    },
    {
        "title": "👑 The 'Undefeated' Vibe", 
        "desc": "High confidence, incredibly good energy. You look like someone who wins every argument and looks absolutely flawless while doing it."
    },
    {
        "title": "☕ The Cozy Aesthetic", 
        "desc": "Warm, peaceful, and super aesthetic. You give off the exact vibe of sitting in a quiet coffee shop while it's raining outside. Flawless energy."
    }
]

# 3. The UI
st.title("✨ Cinematic Vibe Check")
st.write("My visual algorithm analyzes lighting, angles, and energy to tell you what your cinematic aesthetic is today. Let's see your vibe.")
st.divider()

# 4. The Camera Input
picture = st.camera_input("Take a selfie for the algorithm:")

# 5. The Fake AI Processing Engine
if picture:
    st.image(picture, caption="Target Acquired. Initiating scan...", use_container_width=True)
    
    # Fake technical loading bar (Builds anticipation)
    my_bar = st.progress(0, text="Analyzing facial geometry and lighting...")
    time.sleep(1)
    my_bar.progress(40, text="Calculating aesthetic energy levels...")
    time.sleep(1.5)
    my_bar.progress(80, text="Matching with cinematic profiles...")
    time.sleep(1)
    my_bar.empty()
    
    # The Result
    result = random.choice(aesthetics)
    st.balloons()
    st.success("✅ Scan Complete.")
    st.header(result["title"])
    st.info(result["desc"])
