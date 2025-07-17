import os
import random
import time
import numpy as np

seed = os.environ.get("MY_RANDOM_SEED")
if seed is not None:
    random.seed(int(seed))
    np.random.seed(int(seed))

from rl.ucbq_agent_stateless import UCBQAgent
from rl.utils import *

agent = UCBQAgent()

from rl.ucbq_environment_lsl import UCBQEnvironmentLSL
env = UCBQEnvironmentLSL()
names = ['t', 'action', 'reward', 'reward_adjusted', 'new_Q_value', 'alpha', 'epsilon']


# State is fixed to 0
state = 0
t = 0
start_time = time.time()

while True:
    elapsed_time = time.time() - start_time

    action = agent.choose_action(state) 
    reward, next_state, done = env.step(action)
       
    learn_response = agent.learn(state, action, reward, next_state)

    zipped = dict(zip(names, learn_response))
    formatted_zipped = ', '.join([f'{key}: {value}' for key, value in zipped.items()])
    env.environment_logger.info(f't: {learn_response[0]} - l - {formatted_zipped}')

    if done:
        print(f'convergence_consecutive_limit reached, action: {action}')
        break        

    t += 1
