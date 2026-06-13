import streamlit as st
import random

# 1. Setup the Page
st.set_page_config(page_title="Vault Hacker", page_icon="🔓", layout="centered")

# 2. Interactive Memory (The Game Engine)
if 'secret_code' not in st.session_state:
    # Generates a random 3-digit PIN every time she plays
    st.session_state.secret_code = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    st.session_state.attempts = 7
    st.session_state.history = []
    st.session_state.game_over = False
    st.session_state.won = False

# 3. The UI Header
st.title("🔓 Crack The Boss's Vault")
st.write("You found my secure vault. It contains a secret message, but you only have **7 attempts** to hack the 3-digit PIN before the system locks you out forever.")
st.divider()

# 4. The Interactive Gameplay Loop
if not st.session_state.game_over:
    
    # Progress bar showing her remaining attempts
    st.write(f"**Battery Life (Attempts Left): {st.session_state.attempts}**")
    st.progress(st.session_state.attempts / 7)
    
    st.write("Enter your 3-digit guess:")
    col1, col2, col3 = st.columns(3)
    guess1 = col1.number_input("Digit 1", min_value=0, max_value=9, step=1)
    guess2 = col2.number_input("Digit 2", min_value=0, max_value=9, step=1)
    guess3 = col3.number_input("Digit 3", min_value=0, max_value=9, step=1)
    
    if st.button("💻 Hack the System", use_container_width=True):
        st.session_state.attempts -= 1
        guess = [guess1, guess2, guess3]
        feedback = []
        
        # The Logic: Tells her if each number is too high, too low, or correct
        for i in range(3):
            if guess[i] == st.session_state.secret_code[i]:
                feedback.append("✅ Correct")
            elif guess[i] < st.session_state.secret_code[i]:
                feedback.append("⬆️ Higher")
            else:
                feedback.append("⬇️ Lower")
                
        # Save the guess to the history log
        log_entry = f"**{guess1} - {guess2} - {guess3}** ➡️ | {feedback[0]} | {feedback[1]} | {feedback[2]} |"
        st.session_state.history.insert(0, log_entry)
        
        # Win/Loss Conditions
        if guess == st.session_state.secret_code:
            st.session_state.game_over = True
            st.session_state.won = True
        elif st.session_state.attempts == 0:
            st.session_state.game_over = True
            st.session_state.won = False
            
        st.rerun() # Instantly refreshes the screen

    # Show her past guesses so she can use logic to solve it
    if st.session_state.history:
        st.write("---")
        st.subheader("📜 Hacker Log")
        for h in st.session_state.history:
            st.write(h)

# 5. The Results Screen
else:
    if st.session_state.won:
        st.balloons()
        st.success("🔓 SYSTEM BREACHED. ACCESS GRANTED.")
        st.write("### 📩 The Secret Message:")
        # The reward message (Validating, but arrogant)
        st.info("Okay, I admit it... your English is actually getting better, and you are slightly smarter than the average PUBG bot. Don't let this compliment go to your head.")
    else:
        st.error("🚨 ACCESS DENIED. SYSTEM LOCKED.")
        code = st.session_state.secret_code
        st.write(f"The PIN was: **{code[0]} - {code[1]} - {code[2]}**")
        st.warning("You are officially terrible at being a hacker. Please stick to video games.")
        
    if st.button("🔄 Reboot System and Try Again"):
        del st.session_state.secret_code
        st.rerun()
