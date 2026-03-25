# Write a Python program (named Lsn27-candy.py) that simulates a young child 
# asking a parent for a piece of candy. The question is repeated until the 
# answer is yes, after which a Thank you!

print("Welcome to the child simulator!")

# child_q = input("Can I have peice of candy? ").capitalize

count= 0
child_q = "initialize"

while child_q != "Yes":
    child_q = input("Can I have peice of candy? ").capitalize()
    if child_q != "Yes":
        count += 1
    else:
        print(f"You have said no {count} times before saying yes.")