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
    for line in lines:
        matches = [word for word in wordlist if word in line]
        if matches:
            print(matches, line)
    return


def main():
    '''Parse commandline arguments and run program'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wordsearch',
                        help='File location of wordsearch, is required',
                        required=True)
    parser.add_argument('-l', '--wordlist',
                        help='File location of wordlist, is required',
                        required=True)
    args = parser.parse_args()
    wordsearch = list()
    with open(args.wordsearch) as file:
        for line in file.read().splitlines():
            wordsearch.append(''.join(line.split()).lower())
    with open(args.wordlist) as file:
        wordlist = file.read().lower().split()
        wordlist = set(word for word in wordlist if len(word) > 3)
    solve(wordsearch, wordlist)
if __name__ == '__main__':
    main()
