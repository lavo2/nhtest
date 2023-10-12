import gym
import minihack
from nle import nethack

# Create a MiniHack environment using the gym interface
env = gym.make("NetHackScore-v0")

# Reset the environment to start a new episode
obs = env.reset()

# Define a mapping of actions to nethack.Action
action_mapping = {
    "left": nethack.CompassDirection.W,
    "right": nethack.CompassDirection.E,
    "up": nethack.CompassDirection.N,
    "down": nethack.CompassDirection.S
}

done = False
while not done:
    # Choose an action (e.g., move left)
    action = "left"

    # Send the action to the environment
    #obs, reward, done, info = env.step(nethack.CompassDirection.from_char(action_mapping[action]))
    #obs, reward, done, info = env.step(nethack.CompassDirection.E)
    print(ord("k"))
    env.step(ord("k"))
    env.render()

    # Print the current state and reward

    """print("Current State:")
    print(obs["chars"])
    print("Reward:", reward)"""