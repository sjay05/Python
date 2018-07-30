x = input('Enter the speed limit: ')
y = input('Enter recorded speed of the car: ')

if y <= x:
    print "Congratulations, you are whitin the speed limit!"
elif y > x and y - x in range(1, 21):
    f = '$100'
    print 'You are speeding and your fine is %s' %f
elif y > x and y - x in range(21, 31):
    f = '$270'
    print 'You are speeding and your fine is %s' %f
elif y > x and y - x >= 31:
    f = '$500'
    print 'You are speeding and your fine is %s' %f
