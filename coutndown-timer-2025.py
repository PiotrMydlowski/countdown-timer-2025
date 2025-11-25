"""
2025 by PM
Based on a web tutorial
----------------------------------------------
"""
import time


def timer(t):
    #Countdown timer function
    while t:
        print(str(t) + " seconds left.", end='\r\n')
        time.sleep(1)
        t -= 1
    print("End of timer...")

def main():
    #Main function
    sec = input("Enter the seconds amount: ")
    sec = int(sec)
    timer(sec)

if __name__ == '__main__':
    main()