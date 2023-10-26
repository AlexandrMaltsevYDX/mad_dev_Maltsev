from itertools import product


def my_minify(msg):
    return " ".join(msg.split()).replace("> <", "><").replace(" >", ">").replace("\n","").replace("\t","")

def get_len_message(message):
    with open(message, "r", encoding="utf-8") as f:
        len_of_message = len(f.read())
        return len_of_message

def get_message(message):
    with open(message, "r", encoding="utf-8") as f:
        return f.read()
    
def generate_combinations(files, max_lens):
    combinations = list(product(files, max_lens))
    return combinations