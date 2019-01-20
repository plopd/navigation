[//]: # (Image References)

# Navigation

## Project Details

Train an agent to navigate and collect yellow bananas while avoiding blue bananas in a large, square world.

<p align="center"><a href="https://github.com/plopd/navigation/blob/master/results/trained_agent.gif">
 <img width="512" height="256" src="https://github.com/plopd/navigation/blob/master/results/trained_agent.gif"></a>
</p>

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

## Getting Started

**1. Clone the DRLND Repository**

[Follow the instructions in the DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. These instructions can be found in README.md at the root of the repository. By following these instructions, you will install PyTorch, the ML-Agents toolkit, and a few more Python packages required to complete the project.

**2. Download the Unity Environment**

- Download the environment from one of the links below. You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

- Place the file in the DRLND GitHub repository, in the root of this repo, and unzip (or decompress) the file. 

## Instructions

Follow the instructions in `Navigation.ipynb` to get started with training or watching a smart agent.
