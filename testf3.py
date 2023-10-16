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
import minihack

# Create a MiniHack environment using the gym interface
"""env = gym.make(
   "MiniHack-Corridor-R3-v0",
   observation_keys=("glyphs", "chars", "colors", "pixel"),
)"""
env = gym.make("NetHackScore-v0")

# Reset the environment to start a new episode
obs = env.reset()

# Define the action for moving up (North) as an integer
action = 1  # The specific integer value depends on the action space

# Take the action
observation, reward, done, info = env.step(action)
env.render()
print("\n")
print(env.action_space)
for i in env.observation_space:
    print(i)
print("\n")
print(env.observation_space)

print("\n")
print("Render Modes:", env.metadata['render.modes'])
num_actions = env.action_space.n
print(num_actions)
print("\n")
print(observation["glyphs"])
print("\n")

print("\n")
for y, row in enumerate(obs["tty_chars"]):
        for x, char in enumerate(row):
            #print(char)
            if char == ord("@"):  # Assuming '@' represents the agent
                agent_position = (x, y)
print("\n")
print("\n")

print(f"Agent Position: {agent_position}")


#wall_symbol = b'-'
"""while True:
    observation, reward, done, info = env.step(action)
    env.render()
    print(observation["glyphs"])
    if wall_symbol in observation["glyphs"]:
        print("Wall encountered. Stopping movement.")
        break"""
print("\n")
env.render()
wall_symbol = b'-'
print(wall_symbol)
print("\n")