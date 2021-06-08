import re

### Global Variables 
dark_and_storm_path = "assets/dark_and_stormy_night_template.txt"
make_me_path = "assets/make_me_a_video_game_template.txt"
path = "missing.txt"

def read_template(file_path):
    """
    Function to read txt files, and return it is content.
    """
    try:
        with open(file_path,'r') as reader:
            file_content = reader.read()
            return file_content
    except FileNotFoundError:
        return('file not found')

def parse_template(parsed_template):
    """
    Function to return the content stripped from the placeholders, and return the place holders.
    """
    searched_regex = re.findall(r'({.+?})', parsed_template)
    for i,j in enumerate(searched_regex):
        j_subbed = re.sub(r'[{}]', '', j)
        searched_regex[i] = j_subbed
    empty_template = re.sub(r'({.+?})', '{}', parsed_template)
    searched_regex = tuple(searched_regex)
    return [empty_template,searched_regex]

def ask_user(questions):
    """
    Function to return user answers.
    """
    user_answers = []
    for i in questions:
        answer = input(f"May I ask you to provide me {i} ? ")
        user_answers.append(answer)
    return user_answers
    

def merge(actual_stripped,user_answers):
    """
    Function to return user answers merged with the sripped template.
    """
    print(user_answers)
    new_text = actual_stripped.format(*user_answers)
    print(new_text)
    return new_text


if __name__ == '__main__':  
    parsed_template = read_template(make_me_path)
    # parsed_template = read_template(path)
    actual_stripped, actual_parts = parse_template(parsed_template)
    user_answers = ask_user(actual_parts)
    merge(actual_stripped,user_answers)
