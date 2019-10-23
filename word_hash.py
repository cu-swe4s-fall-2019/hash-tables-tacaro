import argparse
import sys
import os
import hash_tables as ht
import hash_functions as hf
import time
from os import path
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')


def main():
    parser = argparse.ArgumentParser(
        description='open text file, hash it, graph output',
        prog='bay')

    parser.add_argument('-f',
                        '--file',
                        type=str,
                        help='file to read',
                        required=True)

    parser.add_argument('-hf',
                        '--hash_function',
                        type=str,
                        help='hash function desired. Choose ascii, rolling, \
                        or fletcher64',
                        required=True)

    parser.add_argument('-ht',
                        '--hash_table',
                        type=str,
                        help='hash table desired. Choose LP or CH',
                        required=True)
    parser.add_argument('-o',
                        '--out_file',
                        type=str,
                        help='desired output plot name',
                        required=True)

    args = parser.parse_args()
    in_file_name = args.file
    func_in = args.hash_function
    table_in = args.hash_table
    out_file_name = args.out_file
    x_label = "Input #"
    y_label = "Hashed value"

    if func_in == 'ascii':
        hfunc = hf.h_ascii
    elif func_in == 'rolling':
        hfunc = hf.h_rolling
    elif func_in == 'fletcher64':
        hfunc = hf.h_fletcher64
    else:
        raise ValueError("You must enter a valid hash function type")

    if table_in == 'LP':
        htable = ht.LinearProbe
    elif table_in == 'CH':
        htable = ht.ChainedHash

    if path.exists(in_file_name) is False:
        raise OSError("Input File not present in working directory!")
        sys.exit(1)

    if path.exists(out_file_name):
        raise OSError("Output file name already exists!")

    #  Here we go
    items = []
    for l in open(in_file_name):
        items.append(l.rstrip())
    N = len(items)
    HSH = htable(N, hfunc)
    for i in items:
        HSH.add(hfunc(i, N), i)

    # ---------------------------------------------------------------------------
    # print(HSH.table)
    X = []
    Y = []
    k = 1
    if table_in == 'LP':
        print(HSH.table)
        for l in HSH.table:
            # print(l)
            hv = l[0]  # pull the hashed value
            X.append(k)
            Y.append(hv)
            k += 1

    if table_in == 'CH':
        print(HSH.table)

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(X, Y, ".", ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig(out_file_name, bbox_inches='tight')


if __name__ == '__main__':
    main()


'''
python word_hash.py -f non_rand_words.txt -hf ascii -ht LP -o non_rand_words_ascii
python word_hash.py -f rand_words.txt -hf ascii -ht LP -o rand_words_ascii
python word_hash.py -f rand_words.txt -hf rolling -ht LP -o rand_words_rolling
python word_hash.py -f non_rand_words.txt -hf rolling -ht LP -o non_rand_words_rolling
python word_hash.py -f rand_words.txt -hf ascii -ht CH -o rand_words_ascii_CH
'''
