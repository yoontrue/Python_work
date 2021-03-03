from day03ex104_whasher import Washer


class SamsungWasher(Washer):
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name

    def info(self):
        print(self.__str__())

    def __str__(self):
        return f'{self.maker},{self.name},{self.size}'

samsungWasher = SamsungWasher(10,'Samsung', '그랑데')
print(samsungWasher)
samsungWasher.washing()