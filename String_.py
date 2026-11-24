from timeit import default_timer as timer

my_string = 'how,are,you,doing?'
my_list = my_string.split(',')
# print(my_list)
new_string = ' '.join(my_list)
# print(new_string)


my_list = ['a']*6
# bad
start = timer()
my_String = ''
for i in my_list:
    my_String+=i
stop = timer()
# print(stop - start)


# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
# print(stop - start)


# %, .format, f-strings
var = "Shibu"
my_string = "the variable is %s" %var
# print(my_string)

var = 7
my_string = "the variable is %d" %var
# print(my_string)

var = 7.2458886
my_string = "the variable is %f" %var
# print(my_string)

var = 7.2458886
my_string = "the variable is %.4f" %var
# print(my_string)

my_string = "the variable is {}".format(var)
# print(my_string)

my_string = "the variable is {:.3f}".format(var)
# print(my_string)

var1 = 3.4324
var2 = 3
my_string = "the variable is {:.1f} and {}".format(var1,var2)
print(my_string)


#we can perform operations in it
my_string = f"The variable is {var1} and {var2} "
print(my_string)
