# Copyright (C) 2016-2017 Jurriaan Bremer.
# See the file 'LICENSE.txt' for copying permission.

def rc4(data, key):
    """RC4 encryption and decryption method."""
    print(data)
    S, j, out = list(range(256)), 0, []

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for ch in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ch ^ S[(S[i] + S[j]) % 256]))

    return "".join(out)

