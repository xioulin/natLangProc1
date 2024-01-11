# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


fruits = ['apple', 'corn','tomato','strawberry']
appleCorn =fruits[0]+' '+fruits[1]

#find items ending in 'ly'


wordList = ['joshua', 'singsing', 'conversational', 'inveterate', 'badly', 'ingenius', 'conversely']

for word in wordList:
    if word[len(word)-2:len(word)] =='ly':
        print(word)



def makePossAdverbList(list):
    adverbalList = []
    for word in list:
        if word[len(word)-2:len(word)] =='ly':
            adverbalList.append(word)
    return print(adverbalList)


easyCheese = 'easychees234e'

# print(easyCheese[11:13])
# print(easyCheese[len(easyCheese)-2:len(easyCheese)])

# makePossAdverbList(wordList)


stringerBell = "thou wast all that too me, love for which my sould did pine a green isle in the sea,love"

print(stringerBell.index('pine'))

print(stringerBell[45:80])