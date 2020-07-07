def my_hash(s):
#     for c in s:
#         print(c)
# my_hash("parth")
# how to turn each character of the string into a number
#     sb = s.encode()
#     for b in sb:
#         print(b)
# my_hash("parth")
# how to turn the entire string into a single number
#by adding all the corresponding numbers for each character
#     sb = s.encode()
#     total = 0
#     for b in sb:
#         total += b
#     return total 
# total_1 = my_hash("parth") 
# print(total_1)   
      sb = s.encode()
      total = 0
      for b in sb:
          total =+ b
      return total %8
i = my_hash("parth")  
hash_table = [None]*8
hash_table[i] = "8months" 
#hash parth
# retrieve value at that hash 
def get_length_timeatlambda(e):
    curr_hash = my_hash(e)
    return hash_table[curr_hash]
length_parth = get_length_timeatlambda("parth")
print("Parth has worked at Lambda for " + length_parth)   

## hash parth ----> constant
## index into the list based on the hash ----> constant


