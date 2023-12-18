

#1. Write code that gets three words from a user and inputs them into a sentence using F-Strings.
#made a function by mistake, added nofunction semple:

def gets_three_words():
    w_list=[]
    while len(w_list) < 3:
        word = input("enter you word:")
        w_list.append(word)
    sentence=f"{w_list[0]} {w_list[1]} {w_list[2]}!"
    print(sentence)
gets_three_words() #to run func

# without func:
_____________________
word1=input("enter you 1st word:")
word2=input("enter you 2nd word:")
word3=input("enter you 3rd word:")
sentence=f"{word1} {word2} {word3}!"
print(sentence)


#2. Exercise: Write a list that contains 2 strings. Print the second string in uppercase and then the first string backwards.
list=['first','second']
print(list[1].upper())
print(list[0][::-1])


#____loops
############Almost correct, but it will print numbers from 10 to 19. To include 20, the condition should be while number <= 20:
#8 Exercise: Write a loop to print every number between 10 and 20.
number=10
while number <20:
    print(number)
    number += 1

#########Incorrect. The initial value of number is set to 10, which is even. It should start at 1. Also, it should be while number <= 20: to include 20 if it was odd.
#9. Exercise: Write a loop to print every odd number between 1 and 20

number = 10
while number <20:
    if number % 2 !=0:
        print(number)
    number += 1

#Functions

#13 Exercise: Write a function that takes a string as input and prints its length:


def length_func():
    user_input= input('Enter your string : ')
    length=len(user_input)
    print(length)
length_func()

############Incorrect. The function's name (gets_sum) and implementation suggest that it sums three numbers, not calculates their average. To calculate the average, the sum of the numbers should be divided by 3: average = result / 3.
#14. Exercise: Define a function that takes three numbers and prints their average

def gets_sum():
    num_list=[]
    while len(num_list) < 3:
        num = int(input("enter you number:"))

        num_list.append(num)
    result=sum(num_list)
    print(result)
gets_sum()

