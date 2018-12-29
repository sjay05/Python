values = [10, 5, 7, 3, 2, 1]
sorted_values = []
#Optimize this code for next class 

for i in range(len(values)):
    last_min = sorted_values[-1] if len(sorted_values) else None
    current_min = None if last_min else values[0]

    for v in values:
        if last_min is None and v < current_min:
            current_min = v
        elif last_min:
            if current_min is None and v > last_min:
                current_min = v
            elif last_min < v < current_min:
                current_min = v

    sorted_values.append(current_min)

print sorted_values













