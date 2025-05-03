import time


def main():
    def countDown(seconds):
        while seconds:
            min, sec = divmod(seconds, 60)
            timer = f"{min:02d}:{sec:02d}"
            print(timer, end="\r")
            time.sleep(1)
            seconds = seconds - 1
        print("00:00\nTime's up!")

    countDown(5)


if __name__ == "__main__":
    main()
