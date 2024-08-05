my_numbers = [155, 158, 159, 161, 160, 162, 165]

heights_of_studs = sorted(my_numbers)
print("The given numbers are", my_numbers)
print ("The sorted numbers are", heights_of_studs)
sum_of_obs = 0

for num in heights_of_studs:
    sum_of_obs = sum_of_obs + num 

mean = sum_of_obs / len(heights_of_studs)

print("The mean of given numbers is", mean)

length_num = len(heights_of_studs)


if length_num % 2 == 0:
    median = (length_num//2) + ((length_num + 1)/2)
if length_num % 2 != 0:
    median = ((length_num +1)/2)

print("The median of the given numbers is" ,  heights_of_studs[int(median-1)])