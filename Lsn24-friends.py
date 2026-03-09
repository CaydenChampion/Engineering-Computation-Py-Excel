friends = ["Bob","Sally","Jill"]
print(f'Your current friends are: {friends}.')

print('\nWhat would you like to do?')
print('Option 1. Add a friend')
print('Option 2. Remove a friend')
print('Option 3. Sort friends')
print('Option 4. Count friends')
print('Option 5. Quit')

select = int(input('Enter your selection: '))

if select == 1:
    new_friend = input('Enter the name of the friend you would like to add: ')
    friends.append(new_friend)
    print(f'Your current friends are: {friends}.\n')
elif select == 2:
    remove_friend = int(input('Enter the number of the friend you would like to remove: '))
    friends.pop(remove_friend - 1)
    print(f'Your current friends are: {friends}.')
elif select == 3:
    friends.sort()
    print(f'Your current friends (sorted) are: {friends}.')
elif select == 4:
    print(f'You have {len(friends)} friends.')
elif select == 5:
    print('Goodbye!')