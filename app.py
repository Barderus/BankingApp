# Run the program: python -m streamlit run client_app.py
import streamlit as st

# Set up the title and introductory message
st.title("Banking Application")
st.write("Welcome to the Bank Application! Please choose an option below.")

# Define the main menu options
menu = ["Login", "Create Account", "Close"]
choice = st.sidebar.radio("Select an option", menu)

# Handle user's choice
if choice == "Login":
    # Login functionality
    st.subheader("Login to your account")
    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")

    if st.button("Login"):
        # Placeholder for login logic
        st.write(f"Logged in as {username}")
        st.success("Login successful")

elif choice == "Create Account":
    # Create new account functionality
    st.subheader("Create a New Account")
    username_new = st.text_input("Enter username")
    password_new = st.text_input("Enter password", type="password")

    if st.button("Create Account"):
        # Placeholder for account creation logic
        st.write(f"Account created for {username_new}")
        st.success("Account creation successful")

elif choice == "Close":
    st.write("Goodbye! See you next time.")
    st.stop()
