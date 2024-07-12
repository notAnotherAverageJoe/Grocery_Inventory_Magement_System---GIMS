import streamlit as st
from dotenv import load_dotenv
from models.grocery import Grocery
from models.meat import Meat
from models.produce import Produce
import datetime
import os

# Load environment variables from .env file
load_dotenv()

# SessionState class definition
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Create a session state instance
session_state = SessionState(selected_category=None, item_name="", stock=0, harvest_date=None, expiration_date=None, cut_type="")

# Function to add items based on category
def add_item(category):
    if category == 'grocery':
        expiration_date = st.date_input("Enter expiration date:", datetime.date.today())
        item = Grocery(session_state.item_name, session_state.stock, expiration_date)
    elif category == 'meat':
        cut_type = st.text_input("Enter cut type:")
        item = Meat(session_state.item_name, session_state.stock, cut_type)
    elif category == 'produce':
        in_season = st.text_input("Is in season? (yes/no)")
        item = Produce(session_state.item_name, session_state.stock, in_season)

    if st.button(f"Add {category.capitalize()}"):
        try:
            item.add_to_db()
            st.success(f"{category.capitalize()} item added successfully!")
        except Exception as e:
            st.error(f"Error adding {category.capitalize()} item: {str(e)}")

# Function to display inventory based on selected category
def display_inventory():
    st.header("Inventory Management System")

    categories = ['grocery', 'meat', 'produce']
    selected_category = st.sidebar.selectbox("Select Category", categories)

    # Store selected category in session state
    session_state.selected_category = selected_category

    # Input fields for item details
    session_state.item_name = st.text_input(f"Enter {selected_category} name:", session_state.item_name)
    session_state.stock = st.number_input(f"Enter stock quantity:", min_value=0, value=session_state.stock)

    if selected_category == 'grocery':
        add_item('grocery')
    elif selected_category == 'meat':
        add_item('meat')
    elif selected_category == 'produce':
        add_item('produce')

    st.subheader(f"{selected_category.capitalize()} Inventory:")
    
    if selected_category == 'grocery':
        items = Grocery.get_all_items()
    elif selected_category == 'meat':
        items = Meat.get_all_items()
    elif selected_category == 'produce':
        items = Produce.get_all_items()
    
    num_columns = 3  # Number of columns in the grid
    columns = st.columns(num_columns)
    
    for index, item in enumerate(items):
        col = columns[index % num_columns]
        with col:
            st.write(f"**Item:** {item.item_name}")
            st.write(f"**Stock:** {item.stock}")
            if selected_category == 'grocery':
                st.write(f"**Expiration Date:** {item.expiration_date}")
            elif selected_category == 'meat':
                st.write(f"**Cut Type:** {item.cut_type}")
            elif selected_category == 'produce':
                st.write(f"**In Season:** {item.in_season}")
            if st.button(f"Delete {item.item_name}", key=f"delete_{item.item_name}"):
                if selected_category == 'grocery':
                    Grocery.delete_item(item.item_name)
                elif selected_category == 'meat':
                    Meat.delete_item(item.item_name)
                elif selected_category == 'produce':
                    Produce.delete_item(item.item_name)
                st.success(f"{item.item_name} deleted successfully!")
                st.experimental_rerun()
            st.markdown("---")

# Function to update inventory
def update_inventory_page():
    st.header("Update Inventory")
    categories = ['grocery', 'meat', 'produce']
    selected_category = st.selectbox("Select Category to Update", categories)

    if selected_category == 'grocery':
        items = Grocery.get_all_items()
        for item in items:
            new_stock = st.slider(f"Update Stock for {item.item_name}", 0, 1000, item.stock)
            if st.button(f"Update {item.item_name} Stock"):
                Grocery.update_stock(item.item_name, new_stock)
                st.success(f"{item.item_name} stock updated successfully to {new_stock}")
                
    elif selected_category == 'meat':
        items = Meat.get_all_items()
        for item in items:
            new_stock = st.slider(f"Update Stock for {item.item_name}", 0, 1000, item.stock)
            if st.button(f"Update {item.item_name} Stock"):
                Meat.update_stock(item.item_name, new_stock)
                st.success(f"{item.item_name} stock updated successfully to {new_stock}")
                
    elif selected_category == 'produce':
        items = Produce.get_all_items()
        for item in items:
            new_stock = st.slider(f"Update Stock for {item.item_name}", 0, 1000, item.stock)
            if st.button(f"Update {item.item_name} Stock"):
                Produce.update_stock(item.item_name, new_stock)
                st.success(f"{item.item_name} stock updated successfully to {new_stock}")

# Function to add custom CSS
def add_custom_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main application entry point
if __name__ == "__main__":
    add_custom_css()
    pages = {
        "Display Inventory": display_inventory,
        "Update Inventory": update_inventory_page
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()
