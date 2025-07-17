def mood_assistant_bot(mood):

    if mood == "happy":
        print("That's great! keep smiling")
    elif mood == "sad":
        print("I'm here for you. Take a short break and breathe.")
    elif mood == "tired":
        print("Rest is important. Be kind to yourself.")
    else:
        print("Thanks for sharing. Wishing you a good day!")
mood = input("How are you feeling today?")
mood = mood.lower()
mood_assistant_bot(mood)
