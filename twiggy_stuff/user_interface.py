from actions.action_container import ActionContainer

class TrainingUI:
    def __init__(self, action_container: ActionContainer):
        self.action_names = action_container.get_names()
        self.codes = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.intended_index = 0
        self.current_index = 0

    def render(self, renderer):
        for i in range(len(self.action_names)):
            color = renderer.white()
            if self.current_index == i:
                color = renderer.red()
            if self.intended_index == i:
                color = renderer.lime()
            renderer.draw_string_2d(10, i * 20, 2, 2, self.codes[i] + " - " + self.action_names[i], color)

    def update_tick(self, current, intended):
        self.current_index = current
        self.intended_index = intended
