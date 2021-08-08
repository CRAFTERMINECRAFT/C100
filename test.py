class bankac(object) :
    def __init__ (self, acnumber, holdername, balance, ifsccode) :
        self.acnumber = acnumber
        self.holdername = holdername
        self.balance = balance
        self.ifsccode = ifsccode
    
    def printData(self) :
        print("AC No. is " + self.acnumber)
        print("AC holder name is " + self.holdername)
        print("AC balance is " + self.balance)
        print("AC IFSC Code of branch is " + self.ifsccode)

ACnumber1 = bankac("1098711607", "Aman", "100000", "9936TYUC5")
ACnumber1.printData()

class guildtournament(object) :
    def __init__ (self, organiser, time) :
        self.organiser = organiser
        self.time = time
        
    
    def printData(self) : 
        print("Organiser of Tournament is " + self.organiser)
        print("Time of the tournament is " + self.time)

tournament = guildtournament("Ankur", "5PM")
tournament.printData()