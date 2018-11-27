import torch
torch.set_default_tensor_type(torch.DoubleTensor)
class OutputFormatter:
    def __init__( self, num_actions ):
        self.num_actions = num_actions
    def format_model_output( self, output ):
        action_index = torch.argmax(output)
        return action_index

    def get_model_output_dimension( self ):
        return self.num_actions

    def create_array_for_training(self, target_action_index):
        target_action = torch.zeros(self.num_actions)
        target_action[target_action_index] = 1
        return target_action
