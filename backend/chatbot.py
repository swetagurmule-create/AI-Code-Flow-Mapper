def get_ai_response(question):

    question = question.lower()

    if "add" in question:
        return "The add() function takes two inputs and returns their sum."

    elif "class" in question:
        return "A class is a blueprint used to create objects."

    elif "function" in question:
        return "A function is a reusable block of code."

    else:
        return "Sorry, I don't know the answer yet."