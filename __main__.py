from pprint import pprint as pp
from bean.fight.AirCraft import AirCraftClass
from bean.fight.Flight import Flight

if __name__ == '__main__':
    craft = AirCraftClass("G-GUPT", "AirBus A319", number_row=22, number_seat_in_row=6);
    flight =Flight("SN390",craft);
    print(flight.getAirLineCode())
    print(flight.getNumber())
    print(flight.getAirCraftModel())
    print("\n >>>>>>>>>>>>>>>>>>>")
    pp(flight._seating)
    flight.allocate_seat("8C","Ankush")
    print("\n >>>>>>>>>>>>>>>>>>>")
    pp(flight._seating)
    pp(flight.getSeating())
