# env utils
import gym
from acme.wrappers import gym_wrapper
from acme import wrappers
import dm_env
from acme.wrappers import base
from sage_rl.rl_module.envwapper import TCP_dmEnv_Wrapper
import numpy as np
import tree
try:
    import pybulletgym
except:
    pass

#总的来说，这个函数根据不同的环境名称创建相应的环境实例，并对其进行必要的处理，以便在强化学习中使用。
def make_env(environment_name, config):

    if 'cartpole' in environment_name:
        environment = gym_wrapper.GymWrapper(gym.make('CartPole-v0'))
        environment = wrappers.SinglePrecisionWrapper(environment)

    elif 'cheetah-run' == environment_name:
        from dm_control import suite
        environment = suite.load('cheetah', 'run')
        environment = wrappers.SinglePrecisionWrapper(environment)

    elif 'walker-stand' == environment_name:
        from dm_control import suite
        environment = suite.load('walker', 'stand')
        environment = wrappers.SinglePrecisionWrapper(environment)

    elif 'tcp' in environment_name:
        print(environment_name)
        environment = TCP_dmEnv_Wrapper(config=config['tcpspec'])
        environment = wrappers.SinglePrecisionWrapper(environment)

    else:
        raise ValueError('Unknown environment: {}.'.format(environment_name))

    return environment
