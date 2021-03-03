def say_hello(name):
    print('hello', name)


def say_hello2(name):
    print('good morning', name)


print('__name__==>', __name__)
if __name__ == '__main__':
    say_hello2('Kim')
    say_hello('Hong')
