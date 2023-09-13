import collections
import string


def encrypt(text_e, shift_e):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    upper.rotate(shift_e)
    lower.rotate(shift_e)
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    return text_e.translate(''.maketrans(string.ascii_uppercase, upper)).translate(
        ''.maketrans(string.ascii_lowercase, lower))


def decrypt(text_d, shift_d):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    upper.rotate(-shift_d)
    lower.rotate(-shift_d)
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    return text_d.translate(''.maketrans(string.ascii_uppercase, upper)).translate(
        ''.maketrans(string.ascii_lowercase, lower))


def brute_force(text_b):
    print('')
    print('All values:- ')
    print('')
    for i in range(len(string.ascii_uppercase)):
        print(i, '|', encrypt(text_b, i))
