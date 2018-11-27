from actions.action_container import ActionContainer
import threading
from inputs import get_key
# from inputs import get_gamepad
class Reader:
    def __init__(self, action_num):
        self.codes = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.intended_index = 0
        self.action_num = action_num

    def update_key(self):
        prefix = "KEY_"
        while True:
            events = get_key()
            for event in events:
                for c in self.codes:
                    if prefix + c == event.code:
                        self.intended_index = min(self.codes.index(c), self.action_num-1)
                        print(self.intended_index)
reader = Reader(ActionContainer().num_actions())
threading.Thread(target=reader.update_key).start()
