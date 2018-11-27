from actions.action_container import ActionContainer
from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
from user_interface import TrainingUI
from keyboard_interface import reader
import time
from inputs import get_key
from RLUtilities.GameInfo import GameInfo

from model_box import ModelBox

class DefaultAgent(BaseAgent):
    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        """
        if playing normally:
            set the model1_path to the path of the saved model

        If training:
            set the train and render flags to True, transfer flag to False
            specify a save_path for the model to be saved at
            optionally specify a model1_path to load a semi-trained model to

        if transfering:
            set transfer flag to True, train flag to False
            set the model1_path to the previously trained network
            optionally set the model2 path to use a semi-trained network
            optionally set rendering to True
        """

        self.save_path = None
        model1_path = None  # Agent to play the game
        model2_path = None  # Agent to copy current agent

        model2_action_num = 0

        self.flags = {
            "render": True,
            "train": False,
            "transfer": False
        }

        self.info = GameInfo(index, team)
        self.actions = ActionContainer()
        self.ui = TrainingUI(self.actions)
        self.model = ModelBox(self.actions.num_actions(), index, team)
        self.controls = SimpleControllerState()

        if model1_path != None:
            self.model.load(model1_path)

        if self.flags["transfer"]:
            self.model2 = ModelBox(model2_action_num, index, team)
            if model2_path != None:
                self.model2.load(model2_path)

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        self.info.read_packet(packet)
        events = get_key()
        action = self.model.predict(packet=packet)

        if self.flags["train"]:
            self.ui.update_tick(action, reader.intended_index)
            self.model.fit(self.ui.intended_index, packet=packet)

        if self.flags["transfer"]:
            self.model2.fit(action, packet=packet)

        self.renderer.begin_rendering()
        if self.flags["render"]:
            self.ui.render(self.renderer)
        self.renderer.end_rendering()

        return self.actions.get_action(index=action)(self.info)
