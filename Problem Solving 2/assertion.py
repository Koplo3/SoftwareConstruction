def number_sum(list):
  #Check if the list given is an empty list, if it's give error message "The submitted list is empty"
  assert len(list) != 0, "The submitted list is empty"
  sum = 0
  for x in list:
    sum += x
  return sum

num_list = [1, 2, 3, 4]
print(number_sum(num_list))

num_list_2 = []
print(number_sum(num_list_2))