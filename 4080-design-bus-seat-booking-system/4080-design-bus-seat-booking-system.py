class BusBooking:

    def __init__(self, n: int):
        self.rows=n+1
        self.booked={}
        self.time=0
        

    def toggle(self, seat: str) -> None:
        if seat in self.booked:
            self.time-=self.booked[seat]
            del self.booked[seat]
            return
        if seat[0] in ("B","C"):
            self.time+=1
            self.booked[seat]=1
        else:
            if seat[0]=="A":
                if "B"+seat[1:] in self.booked:
                    self.time+=3
                    self.booked[seat]=3
                else:
                    self.time+=1
                    self.booked[seat]=1
            else:
                if "C"+seat[1:] in self.booked:
                    self.time+=3
                    self.booked[seat]=3
                else:
                    self.time+=1
                    self.booked[seat]=1
        

    def getTotalTime(self) -> int:
        return self.time

    def getMinTime(self) -> int:
        return len(self.booked)


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()