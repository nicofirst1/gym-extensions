import gym
import numpy as np
import time
import matplotlib.pyplot as plt

from continuous.gym_navigation_2d import register_custom_envs

register_custom_envs()
env = gym.make('Image-Based-Navigation-2d-Map0-Goal0-v0')
observation = env.reset()
img = plt.imshow(observation, interpolation="None", origin='lower')

for t in range(500):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(np.array([1.,1.]))
    print(reward)
    if not t%5:
        img.set_data(observation)
        plt.pause(1e-15)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
