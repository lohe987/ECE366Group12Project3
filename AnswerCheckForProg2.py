patterns = []
with open('patternB.txt', 'r') as f:
    for i, j in enumerate(f):
        if i == 3:
            ta = j
        if i < 8 or i > 107:
            continue
        patterns.append(j.strip())

best_score = 0
counter = 0

for pa in patterns:
    score = 0
    for i in range(16):
        if pa[i] == ta[i]:
            score += 1
    if score > best_score:
        best_score = score
        print("best pattern:", pa)
        counter = 1
    elif score == best_score:
        counter += 1

print("score:", best_score)
print("counter:", counter)
