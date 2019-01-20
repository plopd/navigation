[//]: # (Image References)

# Navigation

## Introduction

### Objective

Train an agent with the [DQN algorithm](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) to navigate a virtual world and collect as many yellow bananas as possible while avoiding blue bananas.

<p align="center"><a href="https://github.com/plopd/navigation/blob/master/results/trained_agent.gif">
 <img width="512" height="256" src="https://github.com/plopd/navigation/blob/master/results/trained_agent.gif"></a>
</p>

### Background

The *reward* of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The *state* space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions. Four *discrete actions* are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is *discounted* and *episodic*, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

## Getting Started

### Setup

0. Clone the repository
```bash
git clone https://github.com/plopd/navigation.git
cd navigation
```

1. Create and activate a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name navigation python=3.6
	source activate navigation
	```
	- __Windows__: 
	```bash
	conda create --name navigation python=3.6 
	activate drlnd
	```
	
2. Clone and install the openai-gym repository
```bash
cd ..
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
```

3. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `navigation` environment.  
```bash
python -m ipykernel install --user --name navigation --display-name "navigation"
```

4. Start (local) jupyter notebook server
```bash
cd ../navigation
jupyter-notebook
```

**2. Download the Unity Environment**

1. Download the environment from one of the links below. You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

2. Place the file in the root of this repo, and unzip (or decompress) the file.

### Code

The code is structured as follows:

`checkpoints` - holds checkpoints of models for the agent

`results` - camera-ready graphs and figures highlighting the results of the training

`src` - agent and models used

`utils` - useful code reusable for different agents (e.g. replay buffer)

`Navigation.ipynb` - tutorial notebook to help users go through the training and testing pipeline

`REPORT.md` - outlines details on the algorithms used to train the agent

## Instructions

Follow the instructions in `Navigation.ipynb` to get started with training and/or watching a smart agent.
