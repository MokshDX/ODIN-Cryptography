morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


def encrypt(text_e):
    s = ''
    x = text_e.split()
    k = list(morse_dict.keys())
    v = list(morse_dict.values())
    for i in x:
        for j in i:
            j = j.upper()
            if j in k:
                a = k.index(j)
                s += str(v[a])
                s += ' '
        s += ' '
    s.lstrip()
    return s


def decrypt(text_d):
    s = ''
    x = text_d.split(' ')
    k = list(morse_dict.keys())
    v = list(morse_dict.values())
    for i in x:
        if ' ' in i:
            line = i.split(' ')
            for j in line:
                if j in v:
                    a = v.index(j)
                    s += str(k[a])
        else:
            if i in v:
                a = v.index(i)
                s += str(k[a])
        s += ' '
    return s
