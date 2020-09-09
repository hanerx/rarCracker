from rarCracker import RarCracker, LocalProvider

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', provider=LocalProvider('./dict.txt'), unrar_tool='unrar')
    print(cracker.crack())
