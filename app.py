import streamlit as st
import time
import random

# 1. Setup the Page
st.set_page_config(page_title="The Smile Check", page_icon="🌻", layout="centered")

# 2. The Genuine Praise Database
# Very simple, grounded, and sweet compliments. 
compliments = [
    "You have a genuinely beautiful smile. I hope you use it a lot today.",
    "Your eyes look really kind here. You have incredibly good energy.",
    "You look really peaceful and pretty today. Keep that vibe.",
    "Whatever you are doing today, it's working. You look effortlessly beautiful.",
    "Your vibe is just really warm and positive. It's impossible not to smile looking at this."
]

# 3. The UI
st.title("🌻 The Daily Smile Check")
st.write("Sometimes you just need a reminder of how good your energy is. Let's see today's vibe.")
st.divider()

# 4. The Camera
picture = st.camera_input("Show me your smile:")

# 5. The Gentle Feedback
if picture:
    st.image(picture, caption="Captured.", use_container_width=True)
    
    # A very short, sweet loading bar
    my_bar = st.progress(0, text="Checking today's vibe...")
    time.sleep(1)
    my_bar.progress(50, text="Analyzing the smile...")
    time.sleep(1)
    my_bar.empty()
    
    # The Praise
    st.balloons()
    result = random.choice(compliments)
    st.success(f"✨ **{result}**")
