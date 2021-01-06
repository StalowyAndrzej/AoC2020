from find_first_invalid import find_first_invalid

with open('09-data.txt') as file:
    tab = []
    for line in file:
        tab.append(int(line.strip()))


print(find_first_invalid(tab))