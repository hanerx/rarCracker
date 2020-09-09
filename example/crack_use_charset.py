from rarCracker import RarCracker

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', 3, 3, charset='1234567890')
    print(cracker.crack())
