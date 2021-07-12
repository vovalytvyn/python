string = str(input("\nWrite: \n"))
print("\ntext:", string)
finalString = ""
num = []
maxInt = 0
Numbers = []

flag = False
for letter in string:
    if letter.isdigit():
        if flag:
            num[len(num) - 1] += str(letter)
        else:
            num.append(letter)
        flag = True
    else:
        flag = False

num = [int(x) for x in num]

string = string.replace('0', '')
string = string.replace('1', '')
string = string.replace('2', '')
string = string.replace('3', '')
string = string.replace('4', '')
string = string.replace('5', '')
string = string.replace('6', '')
string = string.replace('7', '')
string = string.replace('8', '')
string = string.replace('9', '')
print("removed numbers:", string, num)

dst = string.split(' ')



for word in dst:
    if word:
        word = str(word).upper()[0] + word[1:]
        word = word[:len(word) - 1] + str(word).upper()[len(word) - 1]
        finalString += word + ' '

print()
print("final string:", finalString)


maxInt = max(num)
print("\nMax number is", maxInt)



for i in range(len(num)):
    if num[i] != maxInt:
        Numbers.append(int(num[i]) ** i)
    else:
        Numbers.append(num[i])


print("final numbers array:", Numbers)
print("\n\n")
