from argparse import ArgumentParser

from rarCracker.main import RarCracker


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="compressed file path")
    parser.add_argument('-s', '--start', help='minimum password length')
    parser.add_argument('-e', '--end', help='maximum password length')
    parser.add_argument('-w', '--worker', help='number of multi thread')
    parser.add_argument('-t', '--tool', help='decompressing tool')
    parser.add_argument('-o', '--output', help='output path')
    parser.add_argument('-c', '--charset', help='charset')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    cracker = RarCracker(args.file, start=args.start, stop=args.end, workers=args.worker, output=args.output,
                         charset=args.charset)
    cracker.crack()
