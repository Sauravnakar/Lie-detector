import streamlit as st
import random

# 1. Setup the Page
st.set_page_config(page_title="Boss Tycoon", page_icon="💸", layout="centered")

# 2. Live Multiplayer State (The Cloud Engine)
@st.cache_resource
def get_game_state():
    return {
        "board": [
            {"name": "🏁 GO (Collect $200)", "price": 0, "rent": 0, "owner": None, "icon": "🏁"},
            {"name": "☕ The Local Shisha Bar", "price": 100, "rent": 20, "owner": None, "icon": "☕"},
            {"name": "🛍️ Alexanderplatz", "price": 150, "rent": 30, "owner": None, "icon": "🛍️"},
            {"name": "🎮 PUBG Server Room", "price": 200, "rent": 50, "owner": None, "icon": "🎮"},
            {"name": "🪩 Berghain (You're not on the list)", "price": 250, "rent": 70, "owner": None, "icon": "🪩"},
            {"name": "🏢 The Boss's Office", "price": 300, "rent": 90, "owner": None, "icon": "🏢"},
            {"name": "✈️ Brandenburg Airport", "price": 350, "rent": 110, "owner": None, "icon": "✈️"},
            {"name": "👑 The Main Character Mansion", "price": 400, "rent": 150, "owner": None, "icon": "👑"}
        ],
        "players": {
            "Saurav": {"pos": 0, "money": 1000},
            "Intern": {"pos": 0, "money": 1000}
        },
        "turn": "Saurav",
        "logs": ["Game initialized. The Boss (Saurav) moves first."],
        "game_over": False,
        "winner": None
    }

game = get_game_state()

# 3. Game Logic Functions
def roll_dice(player_name):
    if game["game_over"]:
        return
        
    opponent = "Intern" if player_name == "Saurav" else "Saurav"
    roll = random.randint(1, 4) # 1 to 4 to keep them landing on spaces often
    
    old_pos = game["players"][player_name]["pos"]
    new_pos = (old_pos + roll) % len(game["board"])
    game["players"][player_name]["pos"] = new_pos
    
    space = game["board"][new_pos]
    log_msg = f"🎲 {player_name} rolled a {roll} and landed on {space['name']}."
    
    # Pass GO mechanic
    if new_pos < old_pos:
        game["players"][player_name]["money"] += 200
        log_msg += " Passed GO! Collected $200."
        
    # Property Logic
    if space["price"] > 0:
        if space["owner"] is None:
            # Auto-buy if they have enough money
            if game["players"][player_name]["money"] >= space["price"]:
                game["players"][player_name]["money"] -= space["price"]
                space["owner"] = player_name
                log_msg += f" Bought it for ${space['price']}!"
            else:
                log_msg += " Too poor to buy it."
        elif space["owner"] != player_name:
            # Pay Rent
            rent = space["rent"]
            game["players"][player_name]["money"] -= rent
            game["players"][opponent]["money"] += rent
            log_msg += f" Paid ${rent} rent to {space['owner']}."
            
            # Check Bankruptcy
            if game["players"][player_name]["money"] < 0:
                game["game_over"] = True
                game["winner"] = opponent
                log_msg += f" 💀 {player_name} IS BANKRUPT!"
                
    game["logs"].insert(0, log_msg)
    game["turn"] = opponent

# 4. UI Design
st.title("💸 Berlin Boss Tycoon")
st.write("Welcome to real estate. Roll the dice, buy the map, and bankrupt your opponent.")

# Bank Accounts
col1, col2 = st.columns(2)
with col1:
    st.metric("Saurav's Bank", f"${game['players']['Saurav']['money']}")
with col2:
    st.metric("Intern's Bank", f"${game['players']['Intern']['money']}")

st.divider()

# Controls
if not game["game_over"]:
    st.subheader(f"Current Turn: **{game['turn']}**")
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("🎲 Saurav Roll", disabled=(game["turn"] != "Saurav"), use_container_width=True):
            roll_dice("Saurav")
            st.rerun()
    with c2:
        if st.button("🎲 Intern Roll", disabled=(game["turn"] != "Intern"), use_container_width=True):
            roll_dice("Intern")
            st.rerun()
    with c3:
        if st.button("🔄 Refresh Screen", use_container_width=True):
            st.rerun()
else:
    st.balloons()
    st.success(f"🏆 GAME OVER! {game['winner']} wins the monopoly!")
    if st.button("Reset Game Server"):
        game.clear()
        game.update(get_game_state())
        st.rerun()

st.divider()

# The Board Visualizer
st.subheader("🗺️ The Board State")
board_display = ""
for idx, space in enumerate(game["board"]):
    owner_text = f"(Owned by {space['owner']})" if space['owner'] else f"(${space['price']})"
    if idx == 0: owner_text = ""
    
    # Show who is currently standing on this space
    players_here = []
    if game["players"]["Saurav"]["pos"] == idx: players_here.append("Saurav")
    if game["players"]["Intern"]["pos"] == idx: players_here.append("Intern")
    
    standing_text = f" 📍 **{' & '.join(players_here)} are here!**" if players_here else ""
    
    st.write(f"{space['icon']} **{space['name']}** {owner_text}{standing_text}")

# Action Logs
st.divider()
st.subheader("📜 Server Logs")
for log in game["logs"][:8]: # Show last 8 moves
    st.caption(log)
