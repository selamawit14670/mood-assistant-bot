import streamlit as st

st.title("🤖 Mood Assistant Bot")

mood = st.text_input("How are you feeling today? (happy, sad, angry, tired)").strip().lower()

if st.button("Get Response"):
    if mood == "happy":
        st.success("That's great! Keep smiling and spreading positive vibes 🌟")
    elif mood == "sad":
        st.info("It's okay to feel sad sometimes. Take care of yourself ❤️")
    elif mood == "angry":
        st.warning("Take a deep breath... It will pass. Try relaxing for a bit 😌")
    elif mood == "tired":
        st.info("Make sure you rest and hydrate. You deserve it! 💧")
    elif mood:
        st.write("Hmm, I don't recognize that mood, but I'm here for you! 💙")
    else:
        st.write("Please type your mood to get a response.")
