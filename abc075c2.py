def reachable(lines, through, a, b):
    if a == b:
        return True
    lines = lines[:]
    lines.remove(through)
    for line in lines:
        if b in line and reachable(lines, line, a, line[line.index(b) - 1]):
            return True
    return False

N, M = map(int, input().split())
lines = [input().split() for _ in range(M)]
print(M - sum(reachable(lines, line, *line) for line in lines))