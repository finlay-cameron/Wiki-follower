from collections import Counter
from json import load

fileName = "data.json"

print(f"Interpreting data from {fileName}.")

with open(fileName, "r") as f:
    data = load(f)

iters = len(data)
lengths = [len(part) for part in data]
full = []
first = []
last = []
for part in data:
    first.append(part[0][-1])
    last.append(part[-1][-1])
    for page in part:          
        full.append(page[-1])

countFull = Counter(full)
countFirst = Counter(first)
countLast = Counter(last)

comPages = countFull.most_common(3)
comLasts = countLast.most_common(3)
comFirsts = countFirst.most_common(3)

final = f"Over {iters} loops, the longest loop was {max(lengths)} pages long, the shortest {min(lengths)} pages long and the average {round(sum(lengths)/len(lengths))}.\nMost common pages:\n"
for i in range(3):
    final += f"{comPages[i][0]}: {comPages[i][-1]}\n"
if countFirst.most_common(1)[0][-1] > 1:
    final+="Most common first pages:\n"
    for i in range(3):
        final += f"{comFirsts[i][0]}: {comFirsts[i][-1]}\n"
else:
    final+="All first pages were different.\n"
final+="Most common final pages:\n"
for i in range(3):
    final += f"{comLasts[i][0]}: {comLasts[i][-1]}\n"
print(final)