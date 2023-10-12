import gym
import minihack
from nle import nethack
MOVE_ACTIONS = tuple(nethack.CompassDirection)
NAVIGATE_ACTIONS = MOVE_ACTIONS + (
    nethack.Command.OPEN,
    nethack.Command.KICK,
    nethack.Command.SEARCH,
)
"""env = gym.make(
    "MiniHack-Corridor-R3-v0",
    actions=NAVIGATE_ACTIONS,
)"""
env = gym.make(
   "MiniHack-River-v0",
   observation_keys=("glyphs", "chars_crop", "colors", "pixel"),
   actions=NAVIGATE_ACTIONS,
)
print(env)
while(1):
	"""env.step(1)
	env.render()
	env.step(2)
	env.render()
	env.step(3)
	env.render()
	env.step(4)
	env.render()"""
	#MOVE_ACTIONS[0].N
	#MOVE_ACTIONS[0].S
	env.step(MOVE_ACTIONS[0].N)
	nethack.CompassDirection.E
	env.render()
	nethack.CompassDirection.S
	nethack.CompassDirection.S
	env.render()
	nethack.CompassDirection.W
	nethack.CompassDirection.W
	env.render()