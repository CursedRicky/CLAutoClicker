import pyautogui as pg
import time as t
from art import *
import threading, typer, keyboard, colorama

print("-----------------------------------------------------------------------------")

tprint(colorama.Fore.BLUE + "AutoCliker")

print("-----------------------------------------------------------------------------")
print("Press Q to stop")
stop = False
app = typer.Typer()


def check(time: float):
    global stop
    while (not stop):
        pg.click()
        t.sleep(time)


@app.command()
def main(time: float):
    global stop

    th = threading.Thread(target=check, args=(float,))
    th.start()
    while True:
        try:
            if keyboard.is_pressed('q'):
                stop = True
                break
        except:
            pass


if __name__ == "__main__":
    app()
