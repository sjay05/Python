import time
list = [1] * 1000
i = len(list)-1
new_list = []
"""
First I take [-2] as the last index and as the starting
number. Next I see all the pairs possible with this number, 
and since this is the last number the greatest sum possible
is the number itself: -2. So -2 goes into my new list. 
Moving on to the next number [4], the largest sum could 
either be the number itself or the previous greatest sum,
we can access this by referring to the last value of the 
new list which now contains -2. This gives us 4 > -2. So 
we append 4 to the new list. New list = [-2, 4]. Moving on
to 5, I check whether 5 is bigger than the most recently
inputted value to the new list. 5 < 5 + 4. So 9 gets appended
to the new list. Continuing this process the new list 
becomes [-2, 4, 9, 6, 7]. Now to find the greatest sum 
I just have to sort this list. Answer becomes 9.               
"""
start_time = time.time()
while i >= 0:
    if i == len(list)-1:
        new_list.append(list[i])
    else:
        if list[i] > list[i] + new_list[len(new_list)-1]:
            new_list.append(list[i])
        else:
            new_list.append(list[i] + new_list[len(new_list)-1])
    i -= 1

final = sorted(new_list)

#print new_list
print + final[len(final)-1]
end_time = time.time()
print(end_time - start_time)









