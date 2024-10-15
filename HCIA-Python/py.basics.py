#EXERCISE 1
number = int(input("Enter the number: "))
if number > 0 and number < 20:
    for _ in range(number):
        print("I just got started on Python. Looking forward to getting better with time!")   
else:
    print("Python conditions and loops are quite a task")

#EXERCISE 2
text= "ABgvddVICJSdkeprsmgn UTPDvndhtuwPOTNRSjfisuRNSUesajdsa"
lowercase_count = 0
uppercase_count = 0
for chr in text:
    if chr.islower():
        lowercase_count +=1
    elif chr.isupper():
        uppercase_count +=1

print(f"LOWERCASE: {lowercase_count}")
print(f"UPPERCASE: {uppercase_count}")

#EXERCISE 3
def is_triangle_possible(a, b, c):
    if (a + b > c) and (a + c > b) and (b+ c > a):
        return True
    else:
        return False
print(is_triangle_possible(13, 2, 3))

#EXERCISE 4
def  print_five_times(sentence):
    for _ in range(6):
        print (sentence)
def speak(sentence, repeat):
    if repeat == False:
        print(sentence)
    elif repeat == True:
        print_five_times(sentence)

speak("My name is bae", True)