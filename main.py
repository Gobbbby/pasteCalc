
import re
import pyperclip


# getting the formula from the clipboard, and prining it for clarity
thing = pyperclip.paste()
print('in:', thing)

# support for '^' as a way of saying "to the power of", since '^' works different/less than '**'
if '^' in set(thing): thing.replace('^', '**')


# BREAKDOWN: regex for float or integer: [-]?([0-9]*[.])?[0-9]+
# [-]? means it will include the negative sign if it has one
# ([0-9]*[.])? means it will return any amount of numbers before a decimal point, if it has one (meaning, if it doesn't have a decimal point, it won't include this)
# [0-9]+ means it will return the "final" numbers (one or more) in the float, whether they're after a decimal or completely alone (that's dependant on the previous part)

# support for coefficients in front of bracketes ( ex. 2(4 + 3) ) by refactoring for eval()
while re.search(r'[-]?([0-9]*[.])?[0-9]+[(].*[)]', thing):
    startEnd = re.search(r'[-]?([0-9]*[.])?[0-9]+[(].*[)]', thing).span()
    numEndPos = re.search(r'[-]?([0-9]*[.])?[0-9]+', thing[startEnd[0]:startEnd[1]]).span()[1] + startEnd[0]
    thing = thing[:startEnd[0]] + str(f'({thing[startEnd[0]:numEndPos]} * {thing[numEndPos:startEnd[1]]})') + thing[startEnd[1]:]


# evaluating with the python function, copying the answer to the clipboard, and printing it
try:
    pyperclip.copy(eval(thing))
    print('out:', eval(thing))
except:
    print('please input valid formula')
