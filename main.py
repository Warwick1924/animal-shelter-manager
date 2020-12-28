from sys import exit

totalSeats = 10
seatsLeft = totalSeats
animals = []

# add new pet
print('''
Type:
- "status"            - to see all animal names  
- "pet_name"         - to check is there an animal in the shelter
- "left"             - to check is there any left seats in the shelter
- "add pet_name "    - to add new animal to the shelter
- "del pet_name "    - to delete an animal from the shelter
- "q"                - to quit 
''')

while True:
    u_inp = input('Enter: ').replace(' ', '')

    if u_inp == 'status':
        if animals:
            print(', '.join(animals))
            if not seatsLeft:
                print('Our shelter has been overcrowded!')
            else:
                print('There are {} seat/s left'.format(seatsLeft))
        else:
            print('Our shelter is empty')
    elif u_inp == 'left':
        print('There are {} seat/s left'.format(seatsLeft))
    elif u_inp[0:3] == 'add':
        if seatsLeft:
            animals.append(u_inp[3:].capitalize())
            seatsLeft -= 1
        else:
            print('Our shelter has been overcrowded!')
    elif u_inp[0:3] == 'del':
        try:
            del animals[animals.index(u_inp[3:].capitalize())]
            seatsLeft += 1
        except ValueError:
            print('There is not an animal with this name in our shelter :(')
    elif u_inp == 'q':
        print('See you next time :D')
        exit(0)
    else:
        print('There is {} animal/s in our shelter called {}'.format(animals.count(u_inp), u_inp))
    print()
