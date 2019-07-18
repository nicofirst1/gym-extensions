"""
Warning:
    Please note that running this test may use up your RAM, so that please carefully deal with this script.
    On my local, it used about 10GB RAM.
"""

# ALL envs included in gym-extensions
ALL_ENVS = [
"PusherMovingGoal-v0",
"PusherLeftSide-v0",
"PusherFullRange-v0",
"StrikerMovingStart-v0",
"AntGravityMars-v0",
"AntGravityHalf-v0",
"AntGravityOneAndHalf-v0",
"HopperGravityHalf-v0",
"HopperGravityThreeQuarters-v0",
"HopperGravityOneAndHalf-v0",
"HopperGravityOneAndQuarter-v0",
"Walker2dGravityHalf-v0",
"Walker2dGravityThreeQuarters-v0",
"Walker2dGravityOneAndHalf-v0",
"Walker2dGravityOneAndQuarter-v0",
"HalfCheetahGravityHalf-v0",
"HalfCheetahGravityThreeQuarters-v0",
"HalfCheetahGravityOneAndHalf-v0",
"HalfCheetahGravityOneAndQuarter-v0",
"HumanoidGravityHalf-v0",
"HumanoidGravityThreeQuarters-v0",
"HumanoidGravityOneAndHalf-v0",
"HumanoidGravityOneAndQuarter-v0",
"AntMaze-v0",
"HopperStairs-v0",
"HopperSimpleWall-v0",
"HopperWithSensor-v0",
"Walker2dWall-v0",
"Walker2dWithSensor-v0",
"HalfCheetahWall-v0",
"HalfCheetahWithSensor-v0",
"HumanoidWall-v0",
"HumanoidWithSensor-v0",
"HumanoidStandupWithSensor-v0",
"HumanoidStandupAndRunWall-v0",
"HumanoidStandupAndRunWithSensor-v0",
"HumanoidStandupAndRun-v0",
"HopperBigTorso-v0",
"HopperBigThigh-v0",
"HopperBigLeg-v0",
"HopperBigFoot-v0",
"HopperSmallTorso-v0",
"HopperSmallThigh-v0",
"HopperSmallLeg-v0",
"HopperSmallFoot-v0",
"Walker2dBigTorso-v0",
"Walker2dBigThigh-v0",
"Walker2dBigLeg-v0",
"Walker2dBigFoot-v0",
"Walker2dSmallTorso-v0",
"Walker2dSmallThigh-v0",
"Walker2dSmallLeg-v0",
"Walker2dSmallFoot-v0",
"HalfCheetahBigTorso-v0",
"HalfCheetahBigThigh-v0",
"HalfCheetahBigLeg-v0",
"HalfCheetahBigFoot-v0",
"HalfCheetahSmallTorso-v0",
"HalfCheetahSmallThigh-v0",
"HalfCheetahSmallLeg-v0",
"HalfCheetahSmallFoot-v0",
"HalfCheetahSmallHead-v0",
"HalfCheetahBigHead-v0",
"HumanoidBigTorso-v0",
"HumanoidBigThigh-v0",
"HumanoidBigLeg-v0",
"HumanoidBigFoot-v0",
"HumanoidSmallTorso-v0",
"HumanoidSmallThigh-v0",
"HumanoidSmallLeg-v0",
"HumanoidSmallFoot-v0",
"HumanoidSmallHead-v0",
"HumanoidBigHead-v0",
"HumanoidSmallArm-v0",
"HumanoidBigArm-v0",
"HumanoidSmallHand-v0",
"HumanoidBigHand-v0"
]

import gym, time
from gym_extensions.continuous import mujoco

for env_name in ALL_ENVS:
    print("Env: {}".format(env_name))
    env = gym.make(env_name)
    env.reset()
    for _ in range(10):
        env.render()
        s, r, d, i = env.step(env.action_space.sample()) # take a random action
        # print(s.shape, r, d, i)
    env.close()
    time.sleep(1) # since opening some env consumes a lot of RAM we should be sleeping a bit.