class computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("Config is: ",self.cpu,self.ram)


comp1=computer("i4","16gb")
comp2=computer("Ryzen 3","8gb")

comp1.config()
comp2.config()