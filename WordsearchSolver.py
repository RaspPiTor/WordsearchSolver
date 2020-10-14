'''Wordsearch Solver'''
import argparse


def solve(wordsearch, wordlist):
    '''Returns list of all found words in wordsearch using wordlist'''
    lines = list()
    lines.extend(wordsearch)
    lines.extend([i[::-1] for i in wordsearch])
    for i in range(len(lines[0])):
        down = ''.join(line[i] for line in wordsearch)
        lines.append(down)
        lines.append(down[::-1])
    yline = [[0, i] for i in range(len(wordsearch))]
    xline = [[i, 0] for i in range(len(wordsearch[0]))]
    for xvar, yvar in xline + yline:
        line = []
        try:
            while True:
                line.append(wordsearch[yvar][xvar])
                xvar += 1
                yvar += 1
        except IndexError:
            pass
        lines.append(''.join(line))
        lines.append(''.join(line)[::-1])
    for xvar, yvar in xline + yline:
        line = []
        try:
            while True and yvar >= 0:
                line.append(wordsearch[yvar][xvar])
                xvar += 1
                yvar -= 1
        except IndexError:
            pass
        lines.append(''.join(line))
        lines.append(''.join(line)[::-1])
    for line in lines:
        matches = [word for word in wordlist if word in line]
        if matches:
            print(matches, line)
    return


def main():
    '''Parse command-line arguments and run program'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word-search',
                        help='File location of word search, is required',
                        required=True)
    parser.add_argument('-l', '--word-list',
                        help='File location of word list, is required',
                        required=True)
    parser.add_argument('-m', '--minimum-len',
                        help='Minimium length of used words, defaults to 2',
                        default=2, type=int)
    args = parser.parse_args()
    wordsearch = list()
    with open(args.word_search) as file:
        for line in file.read().splitlines():
            wordsearch.append(''.join(line.split()).lower())
    with open(args.word_list) as file:
        wordlist = file.read().lower().split()
        wordlist = set(i for i in wordlist if len(i) > args.minimum_len)
    solve(wordsearch, wordlist)
if __name__ == '__main__':
    main()
