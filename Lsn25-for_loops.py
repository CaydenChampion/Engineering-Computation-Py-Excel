#basic for loop structure

# friends= ['Bob', 'Julie', 'Sam']
# for x in friends:
#     print(x)

# numbers= [0,1,2,3]
# for value in numbers:
#     print(value)

# name = 'Jim'
# for letter in name:
#     print(letter, end = '-')

# print()

# x = [0,1,2]
# names = ['Jim', 'Bob', 'Sally']
# for values in range(0,3):
#     print(names[values])


# x = [0,1,2,3,4,5]
# y = [0,0,0,0,0,0]
# for i in range(len(x)):
#     y[i] = 4 * x[i]**2 - 2 * x[i] + 5

# print()
# print(f'The values of x are: {x}')
# print(f'The values of y are: {y}')
# print()

# for summary statistics
scores = [67, 72, 48, 77, 92]
sum = 0
max = scores[0]
min = scores[0]
for i in range(len(scores)):
    sum = sum + scores[i]
    if scores[i] > max:
        max = scores[i]
    if scores[i] < min:
        min = scores[i]

print()
print(f'Your scores are: {scores}')
print(f'Your sum of the scores is: {sum}')
print(f'Your average score is: {sum/len(scores):.1f}')
print(f'Your maximum score is: {max}')
print(f'Your minimum score is: {min}')
adj_ave = (sum - min) / (len(scores)-1)
print(f'Your adjusted average score is: {adj_ave:.1f}')
print()