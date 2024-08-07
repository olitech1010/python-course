# print("haggith is pretty")
# print("clement is not being nice to me today")
# print("how can i complain to god about my heart")
# print("life will get better")
# print("never will i cry")


# print("if you come to school late i will punish you tomorrow i will go to the cinema")

# x = 3
# y = 7
# if x == 3:
#     print("x is 3")
#     print(x)
# elif x == 4 :
#     print("x is 4")


# prices = [10, 5, 3, 8, 11]
# highest = prices[0]
# for price in prices:
#     if price>highest:
#         highest = price
# print(highest)



# matrix = [
#     [0, 1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9, 10],
# ]
# check =0
# for row in matrix:
#     for item in row:
#         print(item)
# print()


my_list = [1,4,67,45,7,4,7,8,5,42,1,7,9]
#.append, .pop, .sort .reverse .copy .index .insert .remove .clear .count

# my_list.append(20)
# my_list.insert(0,20)
# my_list.remove(1)
# print(my_list)

# #remove duplicates in a list

# unique=[]
# for number in my_list:
#     if number not in unique:
#         unique.append(number)
# print(unique)
# unique.sort()
# unique.reverse()
# print(unique)

# #tuples
# coordianates = (3, 5, 7)
# x = coordianates[0]
# y = coordianates[1]
# z = coordianates[2]

# #unpacking
# x, y, z = coordianates
# print(coordianates)
# for values in coordianates:
#     print(values)
# print(x*y*z)

#Dictionary 

# custumer ={
#     "id": 123546,
#     "name": "Stephen Donkor",
#     "is_verified": True,
# }

# print(custumer.get("name"))

# #digits to word converter

# digits_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three"
# }

# output = ""
# number = input("Enter number: ")
# for ch in number:
#     output += digits_mapping.get(ch, "null") + " "
# print(output)

#split
message = input("Type message : ")
words = message.split(" ")
output = ""
emojis = {
    "sad" : "🥲",
    "happy" : "😅"
}

for word in words:
    output += emojis.get(word, word) + " "
print(output)