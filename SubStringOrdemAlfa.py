def obter_mais_longa_substring(s):
    substrings = []
    substring = s[0]

    i = 0
    j = 1

    while j < len(s):
        if ord(s[j]) >= ord(s[i]):
            substring = substring + s[j]
            i += 1
            j += 1

            if j == len(s):
                substrings.append(substring)

        else:
            substrings.append(substring)
            substring = s[j]
            i += 1
            j += 1

    substrings = sorted(substrings, key=len)

    return substrings[-1]