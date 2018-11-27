import torch
import math
torch.set_default_tensor_type(torch.DoubleTensor)

class InputFormatter:
    def __init__(self, index, team):
        self.index = index
        self.team = team
        self.normilization = torch.Tensor([[4096, 5120, 2044],  # car pos
                                           [2300, 2300, 2300],  # car velocity
                                           [math.pi, math.pi, math.pi],  # car rotation
                                           [5.5, 5.5, 5.5],  # car angular velocity
                                           [4906, 5120, 2044],  # ball pos
                                           [4500, 4500, 4500],  # ball velocity
                                           [6, 6, 6]])  # ball angular velocity

    def create_input_array(self, input_data, gameTick=True):
        if gameTick:
            car = input_data.game_cars[self.index].physics
            d = car.location
            car_pos = torch.Tensor([d.x, d.y, d.z])
            d = car.velocity
            car_vel = torch.Tensor([d.x, d.y, d.z])
            d = car.rotation
            car_rot = torch.Tensor([d.roll, d.yaw, d.pitch])
            d = car.angular_velocity
            car_avel = torch.Tensor([d.x, d.y, d.z])

            ball = input_data.game_ball.physics
            d = ball.location
            ball_pos = torch.Tensor([d.x, d.y, d.z])
            d = ball.velocity
            ball_vel = torch.Tensor([d.x, d.y, d.z])
            d = ball.angular_velocity
            ball_avel = torch.Tensor([d.x, d.y, d.z])

            #Other stats
            other = input_data.game_cars[self.index]

            stats = torch.Tensor([
                other.boost/100,
                1 if other.has_wheel_contact else -1,
                1 if other.is_super_sonic else -1,
                1 if other.jumped else -1,
                1 if other.double_jumped else 1,
            ])
        else:
            raise NotImplementedError

        spatial = torch.stack([car_pos, car_vel, car_rot, car_avel, ball_pos, ball_vel, ball_avel])
        if self.team == 1:
            spatial[:, 1] *= -1
        if car_pos[0] < 0:
            spatial[:, 0] *= -1

        spatial = spatial/self.normilization

        flat_spatial = spatial.view(21)

        output = torch.cat( [flat_spatial, stats] )

        return output

    def get_input_state_dimension(self):
        return 26
