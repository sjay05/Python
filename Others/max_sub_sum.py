import time
input = [1] * 1000

max_sum = curr_sum = input[0]
start = end = 0

i = 1
start_time = time.time()
while i < len(input):
    curr_sum += input[i]
    if input[i] > curr_sum and input[i] > input[start]:
        start = end = i
        max_sum = input[i]
        curr_sum = max_sum

    if curr_sum > max_sum:
        end = i
        max_sum = curr_sum

    i += 1

print "max_sub_sum: %s" % max_sum
end_time = time.time()
print(end_time - start_time)