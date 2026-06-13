import streamlit as st
import time

# 1. Setup the Page
st.set_page_config(page_title="Emoji Decoder", page_icon="🍿", layout="centered")

# 2. Game Memory
if 'level' not in st.session_state:
    st.session_state.level = 0
    st.session_state.score = 0
    st.session_state.game_over = False

# 3. The Visual Game Database
# Emojis mixed with her interests: K-Dramas, PUBG, and Movies
levels = [
    {
        "emojis": "🪂 🔫 🍳 🐔 🍽️", 
        "options": ["Call of Duty", "PUBG", "Fortnite", "Cooking Simulator"], 
        "answer": "PUBG",
        "roast": "If you got this wrong, you are officially banned from the lobby."
    },
    {
        "emojis": "🦑 ☂️ 🍪 👧 🔫", 
        "options": ["Alice in Wonderland", "Squid Game", "Money Heist", "Parasite"], 
        "answer": "Squid Game",
        "roast": "Red light, green light... you survived."
    },
    {
        "emojis": "👨‍💼 🚁 🌪️ 🇰🇵 💔", 
        "options": ["Crash Landing On You", "Descendants of the Sun", "Vincenzo", "Goblin"], 
        "answer": "Crash Landing On You",
        "roast": "The ultimate K-Drama test."
    },
    {
        "emojis": "🚢 🧊 🚪 🥶 💀", 
        "options": ["Pirates of the Caribbean", "Aquaman", "Titanic", "Jaws"], 
        "answer": "Titanic",
        "roast": "He definitely could have fit on that door."
    },
    {
        "emojis": "🦇 👨🏻 🚗 🌃 🦇", 
        "options": ["Dracula", "Batman", "Spider-Man", "Twilight"], 
        "answer": "Batman",
        "roast": "Just a rich guy with a lot of gadgets."
    },
    {
        "emojis": "🧟‍♂️ 🚆 🩸 🏃‍♂️ 🇰🇷", 
        "options": ["World War Z", "Train to Busan", "The Walking Dead", "All of Us Are Dead"], 
        "answer": "Train to Busan",
        "roast": "Never taking public transport in Korea again."
    }
]

# 4. The UI Engine
st.title("🍿 The Pop Culture Decoder")
st.write("Let's see how fast your brain really is. Guess the Movie, Game, or K-Drama based ONLY on the emojis.")
st.divider()

# 5. The Gameplay Loop
if not st.session_state.game_over:
    
    current_level = levels[st.session_state.level]
    
    # Progress Bar
    st.caption(f"Level {st.session_state.level + 1} of {len(levels)} | Score: {st.session_state.score}")
    st.progress(st.session_state.level / len(levels))
    
    # Massive Emojis
    st.markdown(f"<h1 style='text-align: center; font-size: 70px;'>{current_level['emojis']}</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Multiple Choice Buttons (Fast tapping!)
    col1, col2 = st.columns(2)
    
    # Define a helper function to handle the button clicks
    def check_answer(choice):
        if choice == current_level["answer"]:
            st.session_state.score += 1
            st.toast("✅ Correct!")
        else:
            st.toast(f"❌ Wrong! It was {current_level['answer']}")
        
        # Move to next level or end game
        if st.session_state.level < len(levels) - 1:
            st.session_state.level += 1
        else:
            st.session_state.game_over = True
            
    # The Buttons
    with col1:
        if st.button(current_level["options"][0], use_container_width=True):
            check_answer(current_level["options"][0])
            st.rerun()
        if st.button(current_level["options"][1], use_container_width=True):
            check_answer(current_level["options"][1])
            st.rerun()
            
    with col2:
        if st.button(current_level["options"][2], use_container_width=True):
            check_answer(current_level["options"][2])
            st.rerun()
        if st.button(current_level["options"][3], use_container_width=True):
            check_answer(current_level["options"][3])
            st.rerun()

# 6. The Results Screen
else:
    st.balloons()
    st.header("🎬 Director's Cut: Final Score")
    st.markdown(f"### You scored: {st.session_state.score} / {len(levels)}")
    
    if st.session_state.score == len(levels):
        st.success("Perfect score. Okay, I respect your pop culture knowledge.")
    elif st.session_state.score > 3:
        st.warning("Not bad, but you need to watch more movies instead of playing PUBG.")
    else:
        st.error("Terrible. Absolutely terrible. We need to reset your internet router.")
        
    st.divider()
    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.level = 0
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()
