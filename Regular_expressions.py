##Week 2 Assignment Extracting data with regular expressions##
##Finding Numbers in a Haystack

import re
file =open("/Users/welcome/Cookbook/regular_expressions.txt")
sum=0
for line in file:
    #print(line)
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)
print(sum)
