data_input = input("Enter a series of integers separated by space: ")
initial_list = [int(x) for x in data_input.split()]
my_tuple = tuple(initial_list)

print("a) Total number of items:", len(my_tuple))

if len(my_tuple) > 0:
    print("b) Last item:", my_tuple[-1])
    print("c) Elements in reverse order:", my_tuple[::-1])
else:
    print("b) Tuple is empty")
    print("c) Tuple is empty")

if 5 in my_tuple:
    print("d) Yes")
else:
    print("d) No")

if len(my_tuple) >= 2:
    temp_list = list(my_tuple)
    temp_list.pop(0)
    temp_list.pop(-1)
    temp_list.sort()
    print("e) Processed and sorted list:", temp_list)
else:
    print("e) Not enough elements to remove first and last")
  
