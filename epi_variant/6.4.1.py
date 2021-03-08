
telex_exp = {
    '.': 'DOT',
    ',': 'COMMA',
    '?': 'QUESTION MARK',
    '!': 'EXCLAMATION MARK'
}


# Time O(n), Space O(1)
def telex_encoding(s, size):
    reader = size - 1
    writer = len(s)-1

    while reader >= 0:
        c = s[reader]
        if c in telex_exp:
            exp = telex_exp[c]
            s[writer - len(exp) + 1:writer + 1] = exp
            writer -= len(exp)
        else:
            s[writer] = s[reader]
            writer -= 1
        reader -= 1

    final_len = len(s) - writer - 1

    for i in range(final_len):
        s[i] = s[-final_len + i]

    return final_len


def main():
    s = 'Hello World! How are you doing? Long time, no see.'
    size = len(s)
    s = list(s) + [''] * (len(s) * 15)

    res_len = telex_encoding(s, size)

    print(''.join(s[:res_len]))


if __name__ == '__main__':
    main()
