import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!(precisely chatgpt cause its better than me)"
R_GOOD = "You're Awesome!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"
                "Shut up!"][
        random.randrange(4)]
    return response