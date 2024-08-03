my_numbers = [2,4,6,8,10]
print("The given numbers are", my_numbers)
sum_of_obs = 0

for num in my_numbers:
    sum_of_obs = sum_of_obs + num 

mean = sum_of_obs / len(my_numbers)

print("The mean of given numbers is", mean)