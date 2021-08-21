import time

def GetEpochTime():
    return time.time()

def meth1(D):
    monthsTot = D//30
    days   = D%30
    years  = monthsTot//12
    months = monthsTot%12
    print(years,months,days)

def meth2(D):
    years = D//365
    months = (D%365)//30
    days   = D%30
    print(years,months,days)

def Diff(Seconds):
    #calculting minutes without seconds
    mins = Seconds//60
    #calcluting hours witohut minutes
    hours = mins//60
    #calculating days without hours
    Days = int(hours//24)
    #here we reach an impasse, method 1 or method 2
    print(Days)
    meth1(Days)
    meth2(Days)


if __name__=='__main__':
    Time = GetEpochTime()
    Final = Diff(Time)
