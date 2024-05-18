# Sherry Gao

import random

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.agents = []
        self.initialize_agents(num_agents)

    def initialize_agents(self, num_agents):
        for i in range(num_agents):
            while True:
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
                if self.grid[y][x] == '.':
                    agent = Agent(i, x, y)
                    self.agents.append(agent)
                    self.grid[y][x] = 'A'
                    break

    def find_empty_patch(self):
        empty_patches = [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == '.']
        return random.choice(empty_patches) if empty_patches else None

    def move_agent(self, agent):
        new_x, new_y = self.find_empty_patch()
        self.grid[agent.y][agent.x] = '.'
        self.grid[new_y][new_x] = 'A'
        agent.move_to(new_x, new_y)

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

width, height, num_agents = 5, 5, 2
world = World(width, height, num_agents)
world.display()

num_iterations = 3
for iteration in range(num_iterations):
    print(f'{iteration + 1}:')
    for agent in world.agents:
        world.move_agent(agent)
    world.display()
