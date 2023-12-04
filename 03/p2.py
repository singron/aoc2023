#! /usr/bin/env python3
import sys
import collections

with open(sys.argv[1]) as f:
    lines = [l.rstrip() for l in f]

def isdigit(s):
    return '0' <= s <= '9'

def clip(x, mn, mx):
    x = max(x, mn)
    x = min(x, mx)
    return x

def _find_gears(sx, sy, end):
    if sy < 0 or sy >= len(lines):
        return False
    line = lines[sy]
    sx = clip(sx, 0, len(line))
    end = clip(end, sx, len(line))
    s = line[sx:end]
    for x in range(sx, end):
        c = line[x]
        if c == '*':
            yield (x, sy)

def find_gears(sx, sy, end):
    yield from _find_gears(sx-1, sy, sx)
    yield from _find_gears(end, sy, end+1)
    yield from _find_gears(sx-1, sy-1, end+1)
    yield from _find_gears(sx-1, sy+1, end+1)


def main():
    gears = collections.defaultdict(list)
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
                for gx, gy in find_gears(x, y, end):
                    g = (gx, gy)
                    number=int(line[x:end])
                    gears[g].append(number)
                x = end
            else:
                x += 1
    total = 0
    for parts in gears.values():
        if len(parts) == 2:
            total += parts[0] * parts[1]

    print(total)

main()
