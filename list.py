# list = ["Faizan",24,"Rampur",34.43]
# list = [ 2,5,1,7,9,3,4,6,8,3,1 ]
# print(list)
# list.sum()
# print(list)
# list.sort()
# print(list)


# str = "faizan"
# str[0] ="f"
# print(str)

# Practice list based questions
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# list = []
# movie1 = input("Enter you 1st movie")
# movie2 = input("Enter you 2nt movie")
# movie3 = input("Enter you 3dt movie")

# list.append(movie1)
# list.append(movie2)
# list.append(movie3)

# print(list)

# Write a program to check if a list contain palindrom or not

# list = [1,2,3,4,5]
# string = list.copy()
# string.reverse()
# print(string[0])
# if list == string:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# list = [ 1,2,3,4,5]
# for i in range(len(list)):
#    for j in range(j+1,len(list)):
#       print(list[i])


    


def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least 2 elements"
    
    first =second =  float('-inf')  # Initialize to negative infinity
              

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    if second == float('-inf'):
        return "No second largest element found (all elements are same)"
    return second



# Example usage
arr = [99, 23, 919, 56, 99, 29]
print("Second largest:", second_largest(arr))

