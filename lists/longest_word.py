default_filename = '20k.txt'

length = ''

filename = str(input('Enter filename or hit enter for default.\n'))
if filename == '':
    filename = default_filename
    print('Default: {}'.format(default_filename))
print()

with open(filename) as word_list:
    line = 0
    for word in word_list:
        line += 1
        if word[0] == '#': continue
        word = word.replace('\n', '')
        if len(word) >= len(length):
            length = word
            print(' '*(5-len(str(line)))+str(line), ' '*(20-len(str(length)))+str(length), ' '*(20-len(word))+word)
print()
print('END')
