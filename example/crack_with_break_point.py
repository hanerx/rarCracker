from rarCracker import RarCracker, LocalProvider, LocalBreakPoint

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', provider=LocalProvider('./dict.txt'), unrar_tool='unrar',
                         break_point=LocalBreakPoint(breakpoint_count=1))
    print(cracker.crack())
