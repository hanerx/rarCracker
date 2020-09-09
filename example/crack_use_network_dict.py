from rarCracker import RarCracker, NetworkProvider

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', provider=NetworkProvider('https://hanerx.top/rarCracker/dict.json',
                                                                method=NetworkProvider.GET))
    print(cracker.crack())
