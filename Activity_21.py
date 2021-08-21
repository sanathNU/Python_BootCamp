#There are two approcahes in solving this problem
#Both Have basic steps using calcluiton of days
import time

def GetEpochTime():
    return time.time()

def Diff(Seconds):
    #calculting minutes without seconds
    mins = Seconds//60
    #calcluting hours witohut minutes
    hours = mins//60
    #calculating days without hours
    Days = hours//24
    #here we reach an impasse, method 1 or method 2

D_in_y = 365
M_in_y = 12
D_in_m = 30
H_in_D = 24
Min_in_h = 60
S_in_min = 60

mins = cur//60
hours = mins//60
days = hours//24
day = days%30
months = days//30
years = months//12
months = months%12
# years = days//365
# left_over = days%365
# months = left_over//30
# days = left_over%30
print(years,months,day)

if __name__=='__main__':
    Time = GetEpochTime()
