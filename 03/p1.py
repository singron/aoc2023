#! /usr/bin/env python3
import sys

with open(sys.argv[1]) as f:
    lines = [l.rstrip() for l in f]

def isdigit(s):
    return '0' <= s <= '9'

def clip(x, mn, mx):
    x = max(x, mn)
    x = min(x, mx)
    return x

def hassymbols(x, y, end):
    if y < 0 or y >= len(lines):
        return False
    line = lines[y]
    x = clip(x, 0, len(line))
    end = clip(end, x, len(line))
    s = line[x:end]
    for c in s:
        if c != '.' and not isdigit(c):
            return True
    return False

def isadj(sx, sy, end):
    return (hassymbols(sx-1, sy, sx)
            or hassymbols(end, sy, end+1)
            or hassymbols(sx-1, sy-1, end+1)
            or hassymbols(sx-1, sy+1, end+1))


def main():
    total = 0
    for y in range(len(lines)):
        line = lines[y]
        x = 0
        while x < len(line):
            while x < len(line) and not isdigit(line[x]):
                x += 1
            end = x
            while end < len(line) and isdigit(line[end]):
                end += 1
            if end != x:
                if isadj(x, y, end):
                    number=int(line[x:end])
                    total += number
                x = end
            else:
                x += 1
    print(total)

main()
