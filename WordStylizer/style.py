word = input('Give me a word: ')
spacer = input('How much do you want to space it by? ')

try:
    spacer = int(spacer)

    length_of_word = len(word)
    space_counter = 0
    i = 0
    for letter in word:
        if (i >= 1):
            for space in range(space_counter):
                print(' ', end='')
        print(letter)
        i += 1
        space_counter += spacer
except:
    print('Must be a number.')

