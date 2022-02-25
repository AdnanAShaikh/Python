blockchain = [142]
print(blockchain)
def add_value(transaction_amount):
   blockchain.append(transaction_amount)
   print(blockchain)
 
add_value(12)
add_value(13.90)
add_value(313)

print("_"*50)

blockchain1 = [0]
def add_value(total_amount):
    blockchain1.append([blockchain1[-1], total_amount]) #.append() adds things in  the list. here we want to add the blockchain last value
    print(blockchain1)                                  # and the total amount which is equal to the input when calling the function.

add_value(100)
add_value(150)
add_value(200)

for block in blockchain1:
    print("This is a new block")
    print(block)
print("This is our blockchain")

#Hence if the blockchain contains a value it will count and print it as we 
#programmed it to do. It basically counts each element in the given list 
# here we chose the blocklist1


