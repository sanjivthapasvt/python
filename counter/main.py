import time
def countdown(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins ,sec)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Time's up")

seconds = int(input("Enter time in seconds: "))

countdown(seconds)