import time
'''
This is a simple countdown timer that takes in a number of seconds and counts down to zero.
'''
def countdowm_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

seconds = int(input("Enter the in seconds: "))
countdowm_timer(seconds)