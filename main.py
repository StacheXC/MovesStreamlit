import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

moves = pd.read_csv("move_data.csv")
moves = moves[["name", "power", "accuracy", "pp", "damage_class.name", "type.name", "target.name"]]
moves = moves.rename(columns = {"damage_class.name": "damage class", "type.name": "type", "target.name": "target"})

st.title("Moves Streamlit App")

with st.sidebar:
    min_power = st.slider("Minimum Power", min_value = 0, max_value = 250, value = 0)
    max_power = st.slider("Maximum Power", min_value = 0, max_value = 250, value = 250)
    min_accuracy = st.slider("Minimum Accuracy", min_value = 0, max_value = 100, value = 0)
    max_accuracy = st.slider("Maximum Accuracy", min_value = 0, max_value = 100, value = 100)
    damage_class = st.radio("Damage Class", ["physical", "special", "both"])
    st.header("Move Type")
    options = [
    "normal",
    "fire",
    "water",
    "electric",
    "grass",
    "ice",
    "fighting",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dragon",
    "dark",
    "steel",
    "fairy"
    ]
    checked_items = []
    for option in options:
        if st.checkbox(option, value = True):
            checked_items.append(option)

tab1, tab2 = st.tabs(['Filter with Conditions', 'Filter by Name'])

with tab1:
    st.write("Use the sidebar to filter moves")
    moves_filtered = moves[(moves["power"] >= min_power) & (moves["power"] <= max_power) & (moves["accuracy"] >= min_accuracy) & (moves["accuracy"] <= max_accuracy)]
    if damage_class != "both":
        moves_filtered = moves_filtered[moves_filtered["damage class"] == damage_class]
    moves_filtered = moves_filtered[moves_filtered["type"].isin(checked_items)]
    st.dataframe(moves_filtered)
    st.write(f"Number of moves: {moves_filtered.shape[0]}")

with tab2:
    key_word = st.text_input('Enter a keyword (ex: punch)')
    if key_word:
        moves_filtered2 = moves[moves["name"].str.contains(key_word, case=False, na=False)]
        st.dataframe(moves_filtered2)
        st.write(f"Number of moves: {moves_filtered2.shape[0]}")
