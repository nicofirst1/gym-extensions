import gym

from continuous.gym_navigation_2d import register_custom_envs
from gym_extensions.continuous.gym_navigation_2d.env_generator import Environment, EnvironmentCollection, Obstacle
import numpy as np
import time
import timeit

register_custom_envs()

env = gym.make('State-Based-Navigation-2d-Map0-Goal2-v0')

observation = env.reset()
dt1 = []
dt2 = []
for t in range(300):
    env.render()

    start = time.time()
    action = env.action_space.sample()
    end = time.time()

    dt1.append(end - start)

    start = time.time()
    observation, reward, done, info = env.step(np.array([1., 1.]))
    end = time.time()

    dt2.append(end - start)

    print(observation)


    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break

print( sum(dt1)/len(dt1), sum(dt2)/len(dt2))
