user_input = ''
data = []

def instruction():
    print('Menu:\n'
    '1. Add an item\n'
    '2. Mark as done\n'
    '3. View the to do items\n'
    '4. Exit')


while user_input != '4':
    try:
        instruction()
        user_input = input('Enter the number: ')

        if user_input == '1':
            task = input('What is to be done? ')
            data.append(task)
            print('Task added to the list: ', task)
        elif user_input == '2':
            task = input('What has been done? ')
            if task in data:
                data.remove(task)
                print('Task', task, 'removed from the list')
            else:
                print('List does not contain this task')
        elif user_input == '3':
            print('List of deals:')
            for task in data:
                print(task)
        elif user_input == '4':
            print('See you!')
        else:
            raise ValueError
    except ValueError:
        print("Error: Please enter any number from 1 to 4")