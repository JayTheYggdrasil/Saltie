from actions.movement import atba, ATBF

class ActionContainer:
    def __init__(self):
        self.atbf = ATBF()
        self.action_dict = {
            "ATBA": atba,
            "Flip To Ball": self.atbf.get_controls
        }
        self.action_list = [self.action_dict[key] for key in self.action_dict]

    def index_of(self, action):
        self.action_list.index(action)

    def get_action(self, key=None, index=None):
        if type(key) != type(None):
            return self.action_dict[key]
        elif type(index) != type(None):
            return self.action_list[index]

    def get_names(self):
        names = []
        for name in self.action_dict:
            names.append(name)
        return names

    def num_actions(self):
        return len(self.action_list)
