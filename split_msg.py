import argparse

from html.parser import HTMLParser
from exceptions import LowLimitOfLengthsMessage
from utils import my_minify, get_message, get_len_message


class MyHTMLParser(HTMLParser):
    def __init__(self, max_len ):
        super().__init__()
        self.max_len: int = max_len
        self.stack_opend_tags_with_attrs: list[list] = []
        self.stack_opend_tags: list = []
        self.message: list = []
        self.message_count: int = 0
        self.messages: list = []
        self.lst_of_lengths: list = []

    def handle_starttag(self, tag, attrs):
        self.stack_opend_tags.append(tag)
        self.stack_opend_tags_with_attrs.append([tag, attrs])
        self.message.append(f"<{tag}")                           # формирование сообщения
        for attr in attrs:                                       # формирование сообщения
            self.message.append(f"{attr[0]}={attr[1]}".strip())  # формирование сообщения
        self.message[-1] = self.message[-1] + ">"                # формирование сообщения


    def handle_data(self, data):
        self.message.append(f"{data}")                           # формирование сообщения

    def handle_endtag(self, tag):
        if self.stack_opend_tags[-1] == tag:
            self.stack_opend_tags.pop()
            self.stack_opend_tags_with_attrs.pop()
            self.generate_message(tag)

    def generate_message(self, tag):
        _message = self.render_closing_tag_in_message(tag)
        if len(_message) >= self.max_len :
            self.message = []
            self.render_opening_tag_in_message(_message)
        if not self.stack_opend_tags: 
            self.render_opening_tag_in_message(_message)


    def render_closing_tag_in_message(self, tag):
        self.message.append(f"</{tag}>") 
        _message = " ".join(self.message) + "".join(
            [f"</{tag}>" for tag in reversed(self.stack_opend_tags)]
        )
        return _message
    
    def render_opening_tag_in_message(self, message):
        self.messages.append(message)
        for tag in self.stack_opend_tags_with_attrs:
            self.message.append(self.render_tag(tag))

    
    def render_tag(self, tag):
        render_tag = f"{tag[0]}"
        render_attrs = " ".join([f"{attr[0]}={attr[1]}" for attr in tag[1]])
        render_new_open_tag = f"<{render_tag} {render_attrs.strip()}>"
        return render_new_open_tag


    def feed(self, file):
        str = my_minify(get_message(file))
        super().feed(str)
        self.messages = [my_minify(msg) for msg in self.messages]
        self.lst_of_lengths = [len(msg) for msg in self.messages]


def get_optimal_messages(file, max_len, max_float_len ):
    if max_len < 1 or max_float_len < 10:
        raise LowLimitOfLengthsMessage
    parser = MyHTMLParser(max_float_len)
    parser.feed(file)
    if max(parser.lst_of_lengths) < max_len:
        if len(parser.messages) == 1:           # увидел эту ошибку перед отправкой, 
            return parser.messages              # увидел эту ошибку перед отправкой, 
        return parser.messages[:-1]             # увидел эту ошибку перед отправкой, 
    else:
        return get_optimal_messages(file, max_len, int(max_float_len - 5) )
    

def split_message(source, max_len):
    messages = get_optimal_messages(source, max_len, max_len)
    for message in messages:
        yield message


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Split and process HTML messages.")
    arg_parser.add_argument("source_file", help="Path to the source HTML file")
    arg_parser.add_argument("--max-len", type=int, required=True, help="Maximum length for each fragment")

    args = arg_parser.parse_args()
    file = args.source_file
    max_len = args.max_len

    ''' shell comands
    python split_msg.py --max-len=120 ./msg/test-1.html
    python split_msg.py --max-len=150 ./msg/test-2.html
    python split_msg.py --max-len=200 ./msg/test-3.html
    python split_msg.py --max-len=20  ./msg/test-1.html
    '''

    for i in split_message(file, max_len):
        print(i)
        print("<hr>")
       
