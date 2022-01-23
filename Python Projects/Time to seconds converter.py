# Convert any unit of time into seconds

unit = int(input("""
Please enter the option number you want to convert:
1. Hours
2. Minutes
"""))

if unit == 1 :
    hrs = int(input('Enter the time in hours: '))
    print('Time in seconds:', hrs*3600)
elif unit == 2 :
    mins = int(input('Enter the time in minutes: '))
    print('Time in minutes:', mins*60)