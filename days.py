with open('the_file.txt', 'x')as the_file:
    the_file.write('im writing to this file')
    the_file.write('this is the next line of shit im writing to this file')
    for line in the_file:
        print(line)
