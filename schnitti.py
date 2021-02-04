f = open("noten.html")
pruefinfo = False
tr = False
tdcount = 0
filteredstr = []

for line in f:
    if "Prüfungsdatum" in line:
        pruefinfo = True
    if pruefinfo:
        if "<tr>" in line:
            tr = True
        if "</tr>" in line:
            tr = False
            tdcount = 0
        if "<td" in line:
            tdcount += 1
        if (5 < tdcount < 7 or 1 < tdcount < 3 or tdcount == 4) and "<" not in line:
            newline = line
            remove = newline.replace('\t', '')
            remove = remove.replace("                         ", "")
            remove = remove.replace('\n', '')
            if remove:
                filteredstr.append(remove)
    if "Zusatzleistung" in line:
        break

num = 0
noteges = 0
ectsges = 0
fact = 0
for line in filteredstr:
    if line[0] != " ":
        print(line)
        if num % 3 == 1:
            line = line.replace(',', '.')
            fact = float(line)
        if num % 3 == 2:
            line = line.replace(',', '.')
            ects = float(line)
            ectsges += ects
            noteges += ects * fact
        num += 1
print()
print("ECTS insgesamt: " + str(ectsges))
#print(noteges)
print("Durchschnittliche Note: " + str(noteges/ectsges))

