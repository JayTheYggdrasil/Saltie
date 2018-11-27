from RLUtilities.Maneuvers import Drive, AirDodge, Wavedash
from RLUtilities.GameInfo import GameInfo
from rlbot.agents.base_agent import SimpleControllerState
from actions.utilities.basic_utils import magnitude
import time

class DriveDodge:
    def __init__(self, car, target, end_velocity, end_flip=False):
        self.car = car
        self.am_dodging = False
        self.target = target
        self.driver = Drive(car, target_pos=target, target_speed=end_velocity)

    def get_time(self):
        pass

    def should_dodge(self):
        # if magnitude(car.pos - target) >
        pass

    def should_slow(self):
        pass

    def step(self):
        if self.should_dodge() or self.am_dodging:
            pass

def atba(info: GameInfo):
    act = Drive(info.my_car, target_pos=info.ball.pos, target_speed=1800)
    act.step(1/60)
    if act.finished:
        return SimpleControllerState()
    return act.controls

class ATBF:
    def __init__(self):
        self.flipping = False
        self.time = time.time()
    def get_controls(self, info: GameInfo):
        if self.time + 3/60 < time.time():
            self.make_new(info)
        self.act.step(1/60)
        return self.act.controls

        self.time = time.time()
    def make_new(self, info: GameInfo):
        self.act = AirDodge(info.my_car, duration=0.5, target=info.ball.pos, dodge_time=0.1)
