from attr.validators import max_len


def length_of_longest_substring(s):
    start = max_len =0
    used = {}
    for i, char in enumerate(s):
        if char in used and start < used[char]:
            start = used[char]
        else:
            max_len = max(max_len, i - start + 1)
        used[char] = i
    return max_len

print(length_of_longest_substring("hello world"))