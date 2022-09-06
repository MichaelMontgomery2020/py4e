import re

file_handle = input('Enter file name: ')

if len(file_handle) < 1:
    file_handle = open('regex_sum_42.txt')

else:
    try:
        file_handle = open(file_handle)
    except:
        print('Error - Cannot find file:', file_handle)
        quit()

numlist = []

for line in file_handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) < 1:
        continue
    num = [int(x) for x in x]
    together = sum(num)
    numlist.append(together)

print(sum(numlist))
