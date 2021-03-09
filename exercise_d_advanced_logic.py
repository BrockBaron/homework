# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
nos= numbers 
even_num = [num for num in nos if num % 2 == 0]  #list comprehension method
print("Even Numbers : ",even_num)

# 2. Print the difference between the largest and smallest value:
smallest=min(numbers)
largest=max(numbers)
diff=largest-smallest
print(diff)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
# def checkList(List1):
#     for i in range(len(numbers - 1)):


# if List1[i] == 2 and List1[i+1] == 2:
#             return True
           

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







