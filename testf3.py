"""import gym
from nle import nethack

# Create a MiniHack environment using the gym interface
env = gym.make("NetHackScore-v0")

# Reset the environment to start a new episode
obs = env.reset()

# Define the action index for moving up (North)
action = env.action_space.index(nethack.CompassDirection.N)

# Take the action
observation, reward, done, info = env.step(action)"""

import gym
from nle import nethack

# Create a MiniHack environment using the gym interface
env = gym.make("NetHackScore-v0")

# Reset the environment to start a new episode
obs = env.reset()

# Define the action for moving up (North) as an integer
action = 2  # The specific integer value depends on the action space

# Take the action
observation, reward, done, info = env.step(action)

print(env.action_space)
print(env.observation_space)
num_actions = env.action_space.n
print(num_actions)