import gym

from continuous.gym_navigation_2d import register_custom_envs
from gym_extensions.continuous.gym_navigation_2d.env_generator import EnvironmentGenerator, Environment, EnvironmentCollection, Obstacle
import numpy as np
import time

register_custom_envs()

env = gym.make('Limited-Range-Based-Navigation-2d-Map1-Goal1-v0')

observation = env.reset()
dt1 = []
dt2 = []

for t in range(100):
    env.render()

    start = time.time()
    action = env.action_space.sample()
    end = time.time()

    dt1.append(end-start)

    start = time.time()
    observation, reward, done, info = env.step(np.array([1., 1.]))
    end = time.time()

    print(observation)
    time.sleep(0.3)

    dt2.append(end-start)

    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break

print( sum(dt1)/len(dt1), sum(dt2)/len(dt2))
