import pyautogui as pg
import time as t
from art import *
import threading, typer, keyboard, colorama

print(colorama.Fore.CYAN + "-----------------------------------------------------------------------------")

tprint("AutoCliker")

print("-----------------------------------------------------------------------------" + colorama.Fore.RESET)
print(colorama.Fore.GREEN + "Press Q to stop" + colorama.Fore.RESET)
stop = False
app = typer.Typer()


def check(time: float, leftClick: bool):
    global stop
    while (not stop):
        if leftClick:
            pg.click()
        else :
            pg.rightClick()
        t.sleep(time)


@app.command()
def main(time: int, leftClick: bool = True):
    global stop

    th = threading.Thread(target=check, args=(time, leftClick))
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
