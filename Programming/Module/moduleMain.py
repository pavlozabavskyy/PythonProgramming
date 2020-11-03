from classCollection import MyCollection
from decorator import Validation as v
from classBookingBlablacar import BlablacarBooking






def main():
    collect = MyCollection()
    option = '1 - insert from file\n2 - add new obj\n3 - more blablacar (hour)\n4 - driver with...\n5 - print collection\n6 - exit\n'
    while True:
        print(option)
        try:
            choice = v.enterIntInRange(0, 'Your choice: ', 1, 6)
            if choice == 1:
                collect.readJsonFile('data.json')
            elif choice == 2:
                collect.addNewObj()
            elif choice == 3:
                collect.hourMoreTrips()
            elif choice == 4:
                collect.UserWithMoreTrips()
            elif choice == 5:
                print(collect)
            elif choice == 6:
                break
            
        except Exception as e:
            print('Error: ', '-'*30, e)


main()