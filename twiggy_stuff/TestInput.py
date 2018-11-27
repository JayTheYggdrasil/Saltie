from inputs import get_key
from user_interface import TrainingUI
from actions.action_container import ActionContainer
import multiprocessing
import time
# keyboard.Key.name
def on_press(key):
    codes = "qwertyuiopasdfghjklzxcvbnm"

    for i in range(len(codes)):
        if keyboard.KeyCode(char=codes[i]) == key:
            print(i)

_ui = TrainingUI(ActionContainer())

def worker():
    t = time.time() + 15
    while t > time.time():
        events = get_key()
        for event in events:
            if event.code == 'a':
                return event.code

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker, args=(_ui,))
    process.start()
    while True:
        if not process.is_alive():
            process = multiprocessing.Process(target=worker)
            process.start()
        print(_ui.intended_index)
