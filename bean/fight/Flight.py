from pprint import  pprint as pp
from bean.fight.AirCraft import AirCraftClass
class Flight :
    def __init__(self,number,airCraft:AirCraftClass):
        self._number =number;
        self._airCraft=airCraft;
        rows, seat = self._airCraft.getSeating_plan();
        self._seating =[{letter : None for letter in seat}  for _ in  rows]

    # @classmethod : Need to check what this annotation does.
    def getAirCraftModel(self):
        return self._airCraft.getModel();

    def getNumber(self):
        # Need to add validations for number
        return self._number;
    def getAirLineCode(self):
        return self._number[:2];

    def getSeating(self):
        rows,seat =self._airCraft.getSeating_plan();
        return rows,seat;

    def allocate_seat(self,seat,passagerName):
        """
        :param seat: This param like 12C
        :param passagerName: Name of passenger
        :return: Message Success when booking is done.
        :exception : Throw ValueError when seat is already occupied
        """
        if passagerName is None and len(str(passagerName))==0:
            raise ValueError("Passenger name should not be empty or none")
        if(seat is None):
            raise ValueError("Seat should not be None")
        rows,letter =self.getSeating();
        input_letter =seat[-1]
        if(input_letter not in letter):
            raise ValueError("Invalid row in input")
        input_row=seat[:-1]
        try:
            row =int(input_row);
        except Exception as e:
            print("Exception while casting the letter into int while booking",e);
            raise ValueError("Exception while casting the letter into int while booking")
        if(self._seating[row][input_letter] is not None):
            raise ValueError("Seat is already booked")
        self._seating[row][input_letter]=passagerName;
        return "Success!!!"


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
