''''''
marks = [6.3, 5, 7, 7, 7, 8,8]
print("first 2.5 yrs':", marks[ : 5])
marks.append(4)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.insert(3, 5)
print(marks)
marks.pop(2)
marks[4] = 6
print(marks) 


'''
# identify palindrome like racecar 
tup = (2, 1, 3)
print(tup[2])
stri = "abcba"
k = str.count(stri) / 2
str.index(k)
'''
'''
book = []
lst = list(map(str, input(f"enter strings:").split()))
'''

#identify palindrome like racecar

lst = input("Enter strings separated by space: ").split()
print(lst)
print(lst.reverse())
revrs = lst.reverse()
print(revrs)
revrs = lst.copy()
revrs.reverse()
print(revrs)
revrs = lst[::-1]
print("the reverse is:", revrs)
if (lst == revrs):
    print('palindrome')
else:
    print("not a palindrome") 

#new program, doesnt require space to b given
    # Input the string
s = input("Enter a string: ")

# Remove spaces and convert to lowercase for case-insensitive comparison
s = s.replace(" ", "").lower()

# Check if the string is a palindrome
revrs = s[::-1]
print("The reverse is:", revrs)

if s == revrs:
    print('Palindrome')
else:
    print("Not a palindrome")
