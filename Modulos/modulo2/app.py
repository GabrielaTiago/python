from car import turn_on_car
from moto import turn_on_moto

if __name__ == '__main__': # this line is necessary to avoid the code to run when the module is imported
    print('Turning on the vehicles')
    turn_on_car()
    turn_on_moto()
    print(f'This is the app module {__name__}')