#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:45:06 2023

@author: ritunaik
"""


import gymnasium as gym

import time
env = gym.make("FrozenLake-v1", render_mode = "human")

env.reset() #reset the state
env.render()  
time.sleep(10)  

#print the states
print(env.observation_space)

#print the action space left=0 down=1,right=2 up=3
print(env.action_space)

#print the transition proobs of a state p(s'/s,a) give the  prob of moving to
# states from state s by performing action  on a

#syntax : p [state][action]
print(env.P[0][2])

# output is of form : trans_prob, nextstate, reward is terminal

#perform a deterministic action step 0,1,2,3
print("Deterministic Action:")

(next_state, reward,done, transn_prob,info) = env.step(2)

#return_values are nect_state,reward,terminal_state

print("next state is :{0}, Reward is : {1}, Is a terminal state is : {2}".format(next_state,reward,done))
env.render()
time.sleep(1)

#randomly select an action by sampling from the action space
rnd_action = env.action_space.sample()
(next_state,reward,done,transn_prob,info)=env.step(rnd_action)
env.render()
time.sleep(3)

env.reset()


#for each time steps

for n in range (10):
    t_return = 0
    env.reset()
    
    #number of time steps
    num_timesteps = 20
    for i in range(num_timesteps):
        #randomly select an action by sampling from the action space
        rnd_action = env.action_space.sample()
        #perform the selected action
        next_state, reward, done, info, transn_prob = env.step(rnd_action)
        t_return=t_return+reward
        env.render()
        time.sleep(1)
        if done:
            print("return of this episode=",t_return)
            break