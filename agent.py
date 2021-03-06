import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))

        self.epsilon = 0.0001
        self.alpha = 0.1
        self.gamma = 0.8
        
#        self.episode = 1
#        self.score = 0
#        self.next_action = -1

    def update_Q(self, Qsa, Qsa_next, reward, alpha, gamma):
        """ updates the action-value function estimate using the most recent time step """
        return Qsa + (alpha * (reward + (gamma * Qsa_next) - Qsa))

#    def epsilon_greedy_probs(self, Q_s):
#        """ obtains the action probabilities corresponding to epsilon-greedy policy """
#        epsilon = 1.0 / self.episode
#        policy_s = np.ones(self.nA) * epsilon / self.nA
#        policy_s[np.argmax(Q_s)] = 1 - epsilon + (epsilon / self.nA)
#        return policy_s

    def epsilon_greedy_probs(self, Q_s, epsilon):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """

        policy_s = np.ones(self.nA) * epsilon / self.nA
        policy_s[np.argmax(Q_s)] = 1 - epsilon + (epsilon / self.nA)
        return policy_s    
    
    
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        state_policy = self.epsilon_greedy_probs(self.Q[state], self.epsilon)
        action = np.random.choice(np.arange(self.nA), p=state_policy)

#        action = 0
#        if self.next_action == -1:            
#            policy_s = self.epsilon_greedy_probs(self.Q[state])
#            # pick action A
#            action = np.random.choice(np.arange(self.nA), p=policy_s)
#        else: 
#            action = self.next_action
        return action
        #return np.random.choice(self.nA)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """        
        #Q-learning (sarsamax)
        old_Q = self.Q[state][action]
                
        self.Q[state][action] = old_Q + (self.alpha * (reward + (self.gamma * np.max(self.Q[next_state]) - old_Q)))
        
        #self.Q[state][action] += 1
#        alpha = 0.2
#        self.score += reward
#        if not done:
#            # get epsilon-greedy action probabilities
#            policy_s = self.epsilon_greedy_probs(self.Q[next_state])
#            # pick next action A'
#            self.next_action = np.random.choice(np.arange(self.nA), p=policy_s)
#            # update TD estimate of Q
#            self.Q[state][action] = self.update_Q(self.Q[state][action], self.Q[next_state][self.next_action], 
#                                        reward, alpha, 1.0)
#        if done:
#            # update TD estimate of Q
#            self.Q[state][action] = self.update_Q(self.Q[state][action], 0, reward, alpha, 1.0)
#            self.episode += 1
#            self.score = 0

