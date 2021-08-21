#There are two approcahes in solving this problem
#Both Have basic steps using calcluiton of days
import time

def GetEpochTime():
    return time.time()

def meth1(D):
    monthsTot = D//30
    days   = D%30
    years  = monthsTot//12
    months = monthsTot%12
    print("It's been %d years,%d months and %d days since Unix Epoch"%(years,months,days))
    #Kind of gives an difference of 4 months. I guess some things are getting clipped off when using mod function

def meth2(D):
    years = D//365
    months = (D%365)//30
    days   = D%30
    print("It's been %d years,%d months and %d days since Unix Epoch"%(years,months,days))
    return years,months,days

def CurrentDate(Years,Months,Days):
    Year = 1970+Years
    Month = Months
    Day = 1+Days
    print("The Current Date is %d/%d/%d"%(Day,Month,Year))

def Diff(Seconds):
    #calculting minutes without seconds
    mins = Seconds//60
    #calcluting hours without minutes
    hours = mins//60
    #calculating days without hours
    Days = int(hours//24)
    #here we reach an impasse, method 1 or method 2
    y,m,d = meth2(Days)
    return y,m,d


if __name__=='__main__':
    Time = GetEpochTime()
    Y,m,d = Diff(Time)
    CurrentDate(Y,m,d)
