with open('pelican.txt', 'a') as pelican:
    pelican.write('A wonderful bird is the pelican,\nHis bill holds more than his belican.\n')

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
# \n required as part of each list item to make sure line breaks, otherwise all items get concatenated into single line

with open('pelican.txt', 'a') as pelican:
    pelican.writelines(lines)
