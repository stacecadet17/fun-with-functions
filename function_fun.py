def odd_even():
  count = 1
  for num in range(1, 2000):
    if(num % 2 == 0):
      print str(num) + " " + "is an even number"
    else:
      print str(num) + " " + "is an odd number"
      count += 1
odd_even()


def multiply(list, num):
  new_list = []
  for item in list:
    item = item * num
    new_list.append(item)
  return new_list
print multiply([2, 4, 10, 16], 5)


def layered_multiples(list):
  new_list = []
  for item in range(len(list)):
    list[item] *= "1"
  return list
print layered_multiples(multiply([2, 4, 10, 16], 5))
