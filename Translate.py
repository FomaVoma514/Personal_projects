from colorama import init
init()
from colorama import Fore, Back, Style
Back.YELLOW
while True:
    input_string = input()
    Ru_En = dict(zip(map(ord,
                         "qwertyuiop[]asdfghjkl;'zxcvbnm,.`&"
                         'QWERTYUIOP{}ASDFGHJKL;"ZXCVBNM<>~&'),
                         "йцукенгшщзхъфывапролджэячсмитьбюё?"
                         'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ?'))
    print(Back.GREEN +  input_string.translate(Ru_En))
  
