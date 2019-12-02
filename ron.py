import codecs
listi1 = []
listi2 = []

with codecs.open('a.txt', 'r', encoding="utf-8") as filea:
    for line in filea:
        listi1.append(line)

with codecs.open('b.txt', 'r', encoding="utf-8") as fileb:
    for line2 in fileb:
        listi2.append(line2)

k = 0
for i in listi1:
    for j in listi2:
        if str(i.replace("\r\n", "")) not in str(j.replace("\r\n", "")):
            k = 1
        else:
            k = 0
            break
    if k == 1:
        print("Not All names in A exist in B")
        exit()
print("All names in A exist in B")