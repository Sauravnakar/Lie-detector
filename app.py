import streamlit as st
import time

# 1. Setup the Page
st.set_page_config(page_title="Saurav's Predictive AI", page_icon="🤖", layout="centered")

# 2. Keep track of her massive losing streak
if 'losses' not in st.session_state:
    st.session_state.losses = 0

# 3. The UI
st.title("🤖 The Predictive Algorithm")
st.write("I trained a machine learning model on your PUBG decision-making. It knows exactly what you are going to do before you do it.")
st.divider()

st.subheader("Can you beat the Boss in Rock, Paper, Scissors?")
player_choice = st.radio("Make your move:", ("🪨 Rock", "📄 Paper", "✂️ Scissors"), horizontal=True)

# 4. The Rigged Game Engine
if st.button("Play Hand", use_container_width=True):
    # Fake loading bar to make it look highly technical
    progress_text = "Running predictive algorithms..."
    my_bar = st.progress(0, text=progress_text)
    
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text="Analyzing your predictable behavior...")
    
    time.sleep(0.5)
    my_bar.empty()
    
    # The Cheat Code: AI always picks the winning counter-move
    if "Rock" in player_choice:
        ai_choice = "📄 Paper"
    elif "Paper" in player_choice:
        ai_choice = "✂️ Scissors"
    else:
        ai_choice = "🪨 Rock"
        
    # The Results
    st.success(f"**The AI chose:** {ai_choice}")
    st.error("❌ **YOU LOSE.** The algorithm predicted your move flawlessly.")
    
    # Increase her losing streak
    st.session_state.losses += 1

# 5. The Scoreboard of Shame
if st.session_state.losses > 0:
    st.divider()
    st.metric(label="Your Total Losses", value=st.session_state.losses, delta="Too predictable", delta_color="inverse")
    
    if st.session_state.losses == 3:
        st.warning("Three losses in a row. You should probably just give up.")
    elif st.session_state.losses >= 5:
        st.error("Are you actually still trying? You cannot beat my code.")
