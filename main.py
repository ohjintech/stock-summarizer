from src.modules.text_to_speech_stream import text_to_speech_stream
from src.modules.text_to_speech_file import text_to_speech_file
from src.modules.perplexity import generate_answer
from src.modules.greet import greet

if __name__ == "__main__":
    print(greet('jin'))
    generate_answer('RKLB')
    text_to_speech_file('perplexity_response.txt')
    # text_to_speech_file()
    