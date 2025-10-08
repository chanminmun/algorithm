#https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    n %= 26
    res = []
    for ch in s:
            if ch == ' ':

                res.append(' ')
            elif 'A' <= ch <= 'Z':

                base = ord('A')
                offset = ord(ch) - base
                shifted = (offset + n) % 26
                res.append(chr(base + shifted))
            elif 'a' <= ch <= 'z':

                base = ord('a')
                offset = ord(ch) - base
                shifted = (offset + n) % 26
                res.append(chr(base + shifted))


    return ''.join(res)