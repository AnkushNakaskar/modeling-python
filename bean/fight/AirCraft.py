class AirCraftClass :
    def __init__(self,registration,model,number_row,number_seat_in_row):
        self._registration=registration;
        self._model=model;
        self._number_row=number_row;
        self._number_seat_in_row=number_seat_in_row;

    def getRegistration(self):
        return self._registration;
    def getModel(self):
        return self._model;
    def getSeating_plan(self):
        return (range(1,self._number_row+1),"ABCDEFGH"[:self._number_seat_in_row]);

