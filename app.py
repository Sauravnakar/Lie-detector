import streamlit as st
import time
import random
from PIL import Image, ImageStat

# 1. Setup the Page
st.set_page_config(page_title="The Vibe Check", page_icon="🌻", layout="centered")

# 2. The Dynamic Compliment Databases
bright_compliments = [
    "You are literally glowing right now. This lighting was made for you.",
    "Your smile is completely infectious. It just brightens up the whole screen.",
    "You look so fresh and vibrant today. Absolutely stunning.",
    "There is so much warmth in your face here. You look incredibly beautiful.",
    "Your eyes are sparkling in this light. Really, really pretty.",
    "You look effortlessly radiant today. Whatever you're doing, keep doing it.",
    "Such a bright, positive energy in this picture. You look amazing.",
    "You look like a literal ray of sunshine here. Beautiful smile."
]

cozy_compliments = [
    "You look so peaceful and cozy here. It’s a really beautiful, calm vibe.",
    "Your eyes look so deep and expressive in this lighting. Stunning.",
    "Even in the low light, you look completely flawless.",
    "There is such a sweet, relaxed energy about you in this picture.",
    "You look incredibly elegant. The late-night/cozy vibe really suits you.",
    "You have this quiet, beautiful confidence in this picture.",
    "You look really comfortable and effortlessly pretty.",
    "Such a warm and gentle vibe. You look genuinely beautiful here."
]

# 3. The UI
st.title("🌻 The Daily Vibe Check")
st.write("Let my visual algorithm analyze today's energy.")
st.divider()

# 4. The Camera
picture = st.camera_input("Take a quick picture:")

# 5. The Image Processing Engine
if picture:
    st.image(picture, caption="Captured.", use_container_width=True)
    
    # Fake loading bar for the "experience"
    my_bar = st.progress(0, text="Reading image pixels...")
    time.sleep(1)
    
    # ACTUAL IMAGE ANALYSIS
    # Open the image and convert to grayscale to check brightness
    img = Image.open(picture).convert('L')
    stat = ImageStat.Stat(img)
    brightness = stat.mean[0] # Gets the average pixel brightness (0 to 255)
    
    my_bar.progress(50, text="Analyzing lighting and energy levels...")
    time.sleep(1.5)
    my_bar.empty()
    
    # 6. The Dynamic Result
    st.balloons()
    
    # If the average pixel brightness is above 110, it's a bright photo
    if brightness > 110:
        result = random.choice(bright_compliments)
        st.success(f"✨ **Algorithm Result (Bright/Radiant Vibe):**")
        st.info(f"\"{result}\"")
    # If the image is dark, use the cozy compliments
    else:
        result = random.choice(cozy_compliments)
        st.success(f"🌙 **Algorithm Result (Cozy/Peaceful Vibe):**")
        st.info(f"\"{result}\"")
