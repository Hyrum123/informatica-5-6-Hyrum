import time

def main():
    bench = 10
    squats = 10
    ab = 0
    while bench < 500 or squats < 800:
        time.sleep(0.01)
        bench += 0.5
        squats += 0.8
        while bench % 62.5 == 0:
            ab += 1
            print(f"You currently have a {ab} pack")
            print(f"You can currently bench {bench}")
            print(f"You can currently squat {squats:.1f}")
            break
    
main()