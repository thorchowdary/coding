# input array- [2,3,0,6,77,0,8,0,0,0,8,9,7]
# All zeroes should go to end
# output array- [2,3,6,77,8,8,9,7,0,0,0,0,0

#method 1
bag = []
bag2 = []
array = [2,3,0,6,77,0,8,0,0,0,8,9,7]
for i in array:
    if i == 0 :
        bag.append(i)
    else:
        bag2.append(i)

print(bag2+bag)

#method2
bag3 = []
count = 0
for i in array:
    if i!=0:
       bag3.append(i)
    else:
        count+=1
    
print(bag3+[0]*count)

#Find the matching elements present in two arrays.
array1 = [1,2,3]
array2 = [2,1,5]

bag =[]
flag = False
for i in array1:
    if i in array2:
        bag.append(i)
        flag=True
        
if(flag==True):
    print("yeah we have comment elementsin both the array",bag)
else:
    print("we don't have any comman elements")
        
# Given an array of n integers and a number k, find  thepairsofnumbers  in the array such
# that the difference between the pair is k. Find the optimal solution with and without extra
# storage

array = [1,2,3,4]
k = 1
bag =[]
for i in array:
    diff = i-k
    if diff in array:
        bag.append([i,diff])
        #print("the pairs are", [i,diff])
    
print("the pairs are",bag)

# input string- modi is a good man
# All 4 lettered words should get capitalized
# output string- MODI is a GOOD man

input_string = "modi is a good man"
words = input_string.split()
output_string = ""

for word in words:
    if len(word) == 4:
        word = word.upper()
    output_string += word + " "

output_string = output_string.strip()
print(output_string)

# Given a List of integers (List<Integer>), write code in Java 8 style to get the sum of the
# squares of all the odd numbers in the array

bag = [1,2,3,4,5] #1+9+25
sum_ = 0
for i in bag:
    if i%2!=0:
        sum_+=i**2
        
print(sum_)
        
#Given an array, find all the pairs of integers whose sum is 10.
array = [1,9,8,2,7,3]
sum_ = 10
bag = []
for i in array:
    diff = sum_-i
    if diff in array:
        bag.append([diff,i])
print(bag)

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

candies = [4,2,1,1,]
extraCandies = 1
bag = []
def func(candies,extraCandies):
    for i in range(0,len(candies)):
        add_ = candies[i] + extraCandies
        if add_ >= max(candies):
            bag.append(True)
        else:
            bag.append(False)
    print(bag)
print(func(candies,extraCandies))


# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

def string_combinations(s, k):
    result = []
    vowels = "aeiou"
    count = 0
    bag = []
    for i in range(len(s) - k + 1):
        combination = s[i:i+k]
        result.append(combination)

    for i in result:
        print(i)
        for j in i:
            print(j)
            if j in vowels:
                count+=1
        print(count)
        bag.append(count)
        count = 0
    return max(bag)
    
print(string_combinations("abciiidef",3))

