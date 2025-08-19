# This program leads you through the process of fixing
# a bad WiFi connection.

print('Reboot the computer and try to connect.')
print('Did that fix the problem?')
response = input()
if response == 'yes':
    print('Glad to be of help.')
else:
    print('Reboot the router and try to connect.')
    print('Did that fix the problem?')
    response = input()
    if response == 'yes':
        print('Glad to be of help.')
    else:
        print('Make sure the cables between the router and modem are plugged in firmly.')
        print('Did that fix the problem?')
        response = input()
        if response == 'yes':
            print('Glad to be of help.')
        else:
            print('Move the router to a new location and try to connect.')
            print('Did that fix the problem?')
            response = input()
            if response == 'yes':
                print('Glad to be of help.')
            else:
                print('Get a new router.')
