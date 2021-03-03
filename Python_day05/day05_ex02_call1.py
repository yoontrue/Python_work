import hello as hel
import hello

from hello import say_hello

from hello import *

if __name__ == '__main__':
    hel.say_hello('gildong')
    hel.say_hello('gilsun')

    say_hello('Park')
    say_hello2('Cho')
