import streamlit as st

# 1. Setup the Page
st.set_page_config(page_title="Türk Daması", page_icon="♟️", layout="centered")

# 2. Live Multiplayer Magic (Shared Server State)
# This creates one single board on the cloud that both of your phones connect to.
@st.cache_resource
def get_game_state():
    return {
        "board": [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ],
        "selected": None,
        "turn": "W",
        "message": "Game started. ⚪ White moves first."
    }

game = get_game_state()

# 3. UI & Multiplayer Controls
st.title("♟️ Online Türk Daması")
st.write("I built us a private, live server. We are looking at the exact same board.")

col1, col2 = st.columns([2, 1])
with col1:
    st.info(game["message"])
with col2:
    # Because it's web-based, she clicks this to see your move appear
    if st.button("🔄 Refresh Board", use_container_width=True):
        st.rerun()

st.divider()

# 4. The Sandbox Game Engine
# We use a 8x8 grid of buttons.
for r in range(8):
    cols = st.columns(8)
    for c in range(8):
        piece = game["board"][r][c]
        
        # Determine button graphic
        display = " "
        if piece == 'W': display = "⚪"
        elif piece == 'B': display = "⚫"
        
        # Highlight selected piece
        if game["selected"] == (r, c):
            display = "🎯"
            
        with cols[c]:
            if st.button(display, key=f"{r}-{c}", use_container_width=True):
                
                # Action 1: Select your own piece
                if piece == game["turn"]:
                    game["selected"] = (r, c)
                    st.rerun()
                    
                # Action 2: Move the selected piece to an empty square
                elif piece == ' ' and game["selected"] is not None:
                    old_r, old_c = game["selected"]
                    game["board"][r][c] = game["turn"]
                    game["board"][old_r][old_c] = ' '
                    game["turn"] = 'B' if game["turn"] == 'W' else 'W' # Switch turn
                    game["selected"] = None
                    game["message"] = f"Move played. Now it's {'⚪ White' if game['turn'] == 'W' else '⚫ Black'}'s turn."
                    st.rerun()
                    
                # Action 3: Remove a captured opponent piece from the board
                elif piece != game["turn"] and piece != ' ' and game["selected"] is None:
                    game["board"][r][c] = ' '
                    st.rerun()

# 5. Reset Controls
st.divider()
if st.button("🚨 Reset Entire Board"):
    game.clear()
    game.update(get_game_state())
    st.rerun()
