import gym
import minihack
from nle import nethack
MOVE_ACTIONS = tuple(nethack.CompassDirection)
NAVIGATE_ACTIONS = MOVE_ACTIONS + (
    nethack.Command.OPEN,
    nethack.Command.KICK,
    nethack.Command.SEARCH,
)
env = gym.make(
    "MiniHack-Corridor-R3-v0",
    actions=NAVIGATE_ACTIONS,
)
"""env = gym.make(
   "MiniHack-River-v0",
   observation_keys=("glyphs", "chars_crop", "colors", "pixel"),
)"""
print(env)
env.reset() # each reset generates a new environment instance
env.render()
env.step(1)  # move agent '@' north
env.render()
env.step(1)
env.render()
env.step(1)
env.render()
env.step(1)
env.render()
env.step(1)
env.render()
env.step(1)
env.render()
env.step(2)
env.render()
env.step(2)
env.render()
env.step(2)
env.render()
env.step(2)
env.render()
env.step(3)
env.render()
env.step(3)
env.render()
env.step(3)
env.render()
env.step(3)
env.render()
env.step(3)
env.render()
env.step(4)  # move agent '@' north
env.render()
env.step(4)
env.render()
env.step(4)
env.render()
while(1):
	env.step(1)
	env.render()
	env.step(2)
	env.render()
	env.step(3)
	env.render()
	env.step(4)
	env.render()
	"""MOVE_ACTIONS[0].N
	env.render()
	MOVE_ACTIONS[0].S
	env.render()"""
	"""env.render()
	nethack.CompassCardinalDirection.E
	nethack.CompassCardinalDirection.E
	env.render()
	nethack.CompassCardinalDirection.S
	nethack.CompassCardinalDirection.S
	env.render()
	nethack.CompassCardinalDirection.W
	nethack.CompassCardinalDirection.W
	env.render()"""
	

