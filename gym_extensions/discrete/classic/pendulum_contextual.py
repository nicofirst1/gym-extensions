import logging
import math
import gym
from gym import spaces
from gym.envs.classic_control.pendulum import PendulumEnv
from gym.utils import seeding
import numpy as np
#from os import path
logger = logging.getLogger(__name__)

def register_custom_cartpole(tag, max_speed = 8, max_torque = 2.0):
    """
    Tag - What to call your env (e.g. CustomCartpoleLongPole-v0, CustomCartpoleLongPole-v1)
    gravity - if you want to modify the gravity factor (default 9.8)
    masscart - the mass of the cartpole base
    masspole - the mass of the pole
    length - the length of the pole
    force_mag - the magnitude of the exerted action force
    """
    return gym.envs.register(
        id=tag,
        entry_point="envs.transfer.classic.pendulum_contextual:PendulumContextualEnv",
        max_episode_steps=200,
        reward_threshold=195.0,
        kwargs= dict(max_speed = max_speed, max_torque = max_torque)
    )

class PendulumContextualEnv(PendulumEnv):
    def __init__(self,max_speed=8, max_torque=2.0):
        super(PendulumContextualEnv, self).__init__()
        self.context    = [max_speed, max_torque]
        self.max_speed  = self.context[0]
        self.max_torque = self.context[1]

        # our own responsibility to define the range of the context, since we define it
        context_high = np.array([
            self.max_speed  * 10,
            self.max_torque * 10])
        
        context_low = np.array([ 0.1, 0.1]) # the params in the context can't be less or equal to zero!

        self.context_space = spaces.Box(context_low, context_high)


    def _step(self, action):
        state, reward, done, _  = super(PendulumContextualEnv, self)._step(action)
        return state, reward, done, {'max_speed':self.max_speed, 'max_torque':self.max_torque}


    def change_context(self, context_vector):
        self.context    = context_vector
        self.max_speed  = self.context[0]
        self.max_torque = self.context[1]
