def read_template(path):
    with open(path, 'r') as file:
        contents = file.read().strip()
    return contents

def parse_template(template):
    stripped = template
    parts = []

    while '{' in stripped:
        start = stripped.index('{')
        end = stripped.index('}') + 1
        parts.append(stripped[start + 1:end -1])
        stripped = stripped[:start] + '{}' + stripped[end:]
    
    return stripped, tuple(parts)

def merge(stripped, words):
    return stripped.format(*words)


def save_to_file(text, filename="completed_madlib.txt"): #perhaps I can make this to be saved in another folder?
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Your completed Madlib has been saved to {filename}")

def welcome_message():
    print("Welcome to the 'Make Me A Video Game' MadLib!")
    print("In this game, you'll be asked to provide various words like nouns, adjectives, verbs, and names.")
    print("These words will be used to fill in the blanks of a story, creating your own unique video game narrative!")
    print("Follow the prompts or else... well, the program won't do it for you")
    # print('Wanna check what happens if you type "start"')

def fetch_user_inputs(prompt):
    return input(prompt + ": ").strip()

def main():
    welcome_message()

    start = input('Please type "start" when ever you are ready')
    if start.lower() != 'start':
        print('you had one job! type "start" already')
        return
    

    template = read_template("assets/dark_and_stormy_night_template.txt")

    stripped, parts = parse_template(template)

    user_responses = [fetch_user_inputs(f"Enter a {part}") for part in parts]
    madlib = merge(stripped, user_responses)

    prompts = {
        "Adjective1": "Enter an adjective",
        "Adjective2": "Enter another adjective",
        "A First Name1": "Enter a first name",
        "Past Tense Verb": "Enter a past tense verb",
        "A First Name2": "Enter a first name",
        "Adjective3": "Enter another adjective",
        "Adjective4": "Enter another adjective",
        "Plural Noun1": "Enter a plural noun",
        "Large Animal": "Enter a large animal",
        "Small Animal": "Enter a small animal",
        "A Girl's Name": "Enter a girl's name",
        "Adjective5": "Enter another adjective",
        "Plural Noun2": "Enter a plural noun",
        "Adjective6": "Enter another adjective",
        "Plural Noun3": "Enter a plural noun",
        "Number 1-50": "Enter a number between 1 and 50",
        "A First Name3": "Enter a first name",
        "Number1": "Enter a number",
        "Plural Noun4": "Enter a plural noun",
        "Number2": "Enter a number",
        "Plural Noun5": "Enter a plural noun"
    }


    user_responses = {}

    for key in prompts:
        user_responses[key] = fetch_user_inputs(prompts[key])

    madlib_template = (
        "I the {Adjective1} and {Adjective2} {A First Name1} have {Past Tense Verb} "
        "{A First Name2}'s {Adjective3} sister and plan to steal her {Adjective4} {Plural Noun1}!\n"
        "What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, "
        "you'll have to collect the {Adjective5} {Plural Noun2} and {Adjective6} {Plural Noun3} that open up the "
        "{Number 1-50} worlds connected to A {A First Name3}'s Lair. There are {Number1} {Plural Noun4} and "
        "{Number2} {Plural Noun5} in the game, along with hundreds of other goodies for you to find."
    )

    for key, value in user_responses.items():
        madlib_template = madlib_template.replace("{" + key + "}", value, 1)

    print("\nI take no responsibility for what you came up with:\n")
    print(madlib_template)
    save_to_file(madlib_template)
    save_to_file(madlib)


if __name__ == "__main__":
    main()
