import streamlit as st
import pandas as pd
# Title
st.title("Al Barakah Homes🏢")

# Sidebar Info
st.sidebar.header("Directions")
st.sidebar.write("🔢select a *room number (1–9)* to check its status.")

# Input
room = st.number_input("Enter Room Number🔢:", min_value=1, max_value=20, step=1)

# Logic
def get_room_status(Room):
    if Room == 1:
        return "Furnished✨"
    elif Room == 2:
        return "Rental💵"
    elif Room == 3:
        return "Renovation🛠"
    elif Room == 4:
        return "For sale🔑"
    elif Room == 5:
        return "Rental💵"
    elif Room == 6:
        return "Apartment electrical installation⚡👨🏻‍🔧"
    elif Room == 7:
        return "Rental💵"
    elif Room == 8:
        return "Owned by myself👤"
    elif Room == 9:
        return "Top coat to be done🎨🖌"
    else:
        return "❌ ERROR: Room not found"

# Button
if st.button("Check Room Status"):
    status = get_room_status(room)
    st.success("🏡 Room {room}: {status}