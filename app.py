import streamlit as st
import time
import random

# 1. Setup the Page
st.set_page_config(page_title="The Aura Scanner", page_icon="📸", layout="centered")

# 2. The Aura Database (80% compliment, 20% roast)
auras = [
    {
        "title": "☕ The Ruthless CEO", 
        "desc": "Your facial geometry screams 'I drink iced coffee in the middle of winter and fire people for fun.' High boss energy, but definitely a menace to society."
    },
    {
        "title": "🎬 The K-Drama Villain", 
        "desc": "The algorithm detects high levels of 'I am secretly right about everything.' You look like the character who shows up in episode 4 to ruin the main couple's lives, and we love it."
    },
    {
        "title": "🎮 The Carried Gamer", 
        "desc": "Scanning indicates you probably complain about lag while someone else carries the squad. But the lighting in this picture is good, so we'll let it slide."
    },
    {
        "title": "🌙 The Sleepy Prodigy", 
        "desc": "You look like you need 14 hours of sleep and an iced matcha, but you could still outsmart everyone in the room. High IQ, low energy."
    }
]

# 3. The UI
st.title("📸 The Aura Scanner")
st.write("My computer vision model doesn't just see faces; it reads energy. Take a selfie right now and let the algorithm diagnose your vibe.")
st.divider()

# 4. The Camera Input
picture = st.camera_input("Take a selfie for analysis:")

# 5. The Fake AI Processing Engine
if picture:
    st.image(picture, caption="Target Acquired. Initiating scan...", use_container_width=True)
    
    # Fake technical loading bar
    my_bar = st.progress(0, text="Initializing facial recognition...")
    time.sleep(1)
    my_bar.progress(30, text="Analyzing main character energy...")
    time.sleep(1.5)
    my_bar.progress(60, text="Detecting traces of PUBG rage...")
    time.sleep(1.5)
    my_bar.progress(90, text="Finalizing aesthetic matrix...")
    time.sleep(1)
    my_bar.empty()
    
    # The Result
    result = random.choice(auras)
    st.success("✅ Scan Complete.")
    st.header(result["title"])
    st.info(result["desc"])
