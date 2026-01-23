# Objective: This tutorial will teach you how to create a simple simulation of "sentient" sprites that react to their environment.
# We will focus on a fundamental AI concept: **Rule-Based Decision Making**.
# Each sprite will have a set of simple rules that determine its behavior based on its surroundings.

import random
import time

# --- Constants for our simulation environment ---
# These represent different types of tiles in our grid.
EMPTY = 0         # An empty space
FOOD = 1          # A source of food
OBSTACLE = 2      # Something the sprite cannot pass through
SPRITE_ID = 3     # A placeholder for a sprite's position (we'll store actual sprites separately)

# --- Sprite Class ---
class Sprite:
    def __init__(self, x, y, world_size):
        # The sprite's current position in the simulation grid.
        self.x = x
        self.y = y
        # The size of the world, used for boundary checks.
        self.world_size = world_size
        # A simple hunger level. Higher means more hungry.
        self.hunger = 0
        # A simple energy level. Affects movement and decision making.
        self.energy = 100
        # A unique identifier for this sprite.
        self.id = f"S{random.randint(100, 999)}" # For identification in print statements

    def __str__(self):
        # A human-readable representation of the sprite.
        return f"<{self.id} at ({self.x}, {self.y}), Hunger: {self.hunger}, Energy: {self.energy}>"

    def perceive(self, world):
        # This method simulates the sprite "seeing" its immediate surroundings.
        # We'll define a small perception radius around the sprite.
        perception_radius = 1 # How many tiles away the sprite can see in each direction.
        surroundings = {}     # A dictionary to store what the sprite perceives.

        # Iterate through the area around the sprite within the perception radius.
        for dy in range(-perception_radius, perception_radius + 1):
            for dx in range(-perception_radius, perception_radius + 1):
                # Calculate the neighbor's coordinates.
                nx, ny = self.x + dx, self.y + dy

                # Check if the neighbor is within the world boundaries.
                if 0 <= nx < self.world_size and 0 <= ny < self.world_size:
                    # Get the tile type from the world.
                    tile_type = world[ny][nx]
                    # Store the perceived tile type, noting its relative position.
                    surroundings[(dx, dy)] = tile_type
        return surroundings

    def decide_action(self, surroundings):
        # This is the core of our AI: rule-based decision making.
        # The sprite looks at its surroundings and decides what to do.

        # Rule 1: If hungry, try to find food.
        if self.hunger > 50:
            # Look for food in the immediate vicinity.
            for (dx, dy), tile_type in surroundings.items():
                if tile_type == FOOD:
                    # If food is found, decide to move towards it.
                    # We'll return a 'move' action with the target direction.
                    return {"action": "move", "direction": (dx, dy)}

        # Rule 2: If energy is low, try to rest (or avoid strenuous activity).
        if self.energy < 30:
            # If energy is low, maybe avoid moving or look for a safe spot.
            # For simplicity, we'll just decide to "wait" if energy is low.
            return {"action": "wait"}

        # Rule 3: If there's an obstacle directly in front, try to go around.
        # We assume the sprite primarily looks forward (0, 1) for obstacles.
        # This is a simplification; a real system would be more nuanced.
        if (0, 1) in surroundings and surroundings[(0, 1)] == OBSTACLE:
            # Try to move left (dx=-1, dy=0) or right (dx=1, dy=0) if possible.
            if (-1, 0) in surroundings and surroundings[(-1, 0)] == EMPTY:
                return {"action": "move", "direction": (-1, 0)}
            elif (1, 0) in surroundings and surroundings[(1, 0)] == EMPTY:
                return {"action": "move", "direction": (1, 0)}

        # Default behavior: If no specific rule is met, move randomly.
        # We try to find an empty adjacent tile to move to.
        possible_moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Exclude moving to the same spot (0,0).
                if dx == 0 and dy == 0:
                    continue
                # Check if the target tile is within bounds and is empty.
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < self.world_size and 0 <= ny < self.world_size and surroundings.get((dx, dy)) == EMPTY:
                    possible_moves.append((dx, dy))

        if possible_moves:
            # If there are valid random moves, pick one.
            return {"action": "move", "direction": random.choice(possible_moves)}
        else:
            # If no moves are possible (e.g., surrounded by obstacles), wait.
            return {"action": "wait"}

    def update(self, world):
        # This method updates the sprite's state based on its decisions.
        # 1. Perceive the environment.
        surroundings = self.perceive(world)

        # 2. Decide on an action.
        decision = self.decide_action(surroundings)
        action_type = decision["action"]

        # 3. Execute the action and update sprite state.
        if action_type == "move":
            # Get the direction from the decision.
            dx, dy = decision["direction"]
            # Calculate the new position.
            new_x, new_y = self.x + dx, self.y + dy

            # Check if the move is valid (within bounds and not an obstacle).
            # Note: The decide_action already tries to ensure this, but this is a safeguard.
            if 0 <= new_x < self.world_size and 0 <= new_y < self.world_size and world[new_y][new_x] != OBSTACLE:
                # Update the world grid: mark the old position as empty and the new as a sprite.
                # IMPORTANT: The world object needs to handle this update.
                # For this simulation, we'll assume the main loop handles world updates.
                # Here, we just update the sprite's internal coordinates.
                self.x = new_x
                self.y = new_y

                # Moving costs energy.
                self.energy -= 5
                # Hunger increases over time, especially when moving.
                self.hunger += 10

                # If we landed on food, eat it!
                if world[self.y][self.x] == FOOD:
                    self.hunger = max(0, self.hunger - 30) # Reduce hunger
                    self.energy = min(100, self.energy + 10) # Gain a little energy
                    # IMPORTANT: The world needs to remove the food.
                    # We'll handle this in the main simulation loop.

            else:
                # If the move was invalid, the sprite might just wait or try another action.
                # For simplicity, we'll say an invalid move results in waiting.
                self.energy -= 2 # Minor energy cost for attempting a move.
                self.hunger += 2 # Slight hunger increase.

        elif action_type == "wait":
            # Resting slightly increases energy and reduces hunger slowly.
            self.energy = min(100, self.energy + 5)
            self.hunger = max(0, self.hunger + 2)

        # Ensure energy and hunger stay within reasonable bounds.
        self.energy = max(0, min(100, self.energy))
        self.hunger = max(0, min(100, self.hunger))

# --- Simulation Environment ---
class World:
    def __init__(self, size):
        # Initialize the world grid.
        self.size = size
        # Create a 2D list representing the world.
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
        # Store active sprites.
        self.sprites = []

    def add_sprite(self, sprite):
        # Add a sprite to the world and update the grid.
        self.sprites.append(sprite)
        # Place the sprite in its initial position on the grid.
        self.grid[sprite.y][sprite.x] = SPRITE_ID

    def place_item(self, x, y, item_type):
        # Place an item (like food or obstacle) in the world.
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[y][x] = item_type

    def update_sprite_positions(self):
        # Clear all sprite markers from the grid.
        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] == SPRITE_ID:
                    self.grid[y][x] = EMPTY

        # Place all sprites in their new positions.
        for sprite in self.sprites:
            self.grid[sprite.y][sprite.x] = SPRITE_ID

    def update_food(self):
        # Remove food where sprites have moved onto.
        for sprite in self.sprites:
            if self.grid[sprite.y][sprite.x] == FOOD:
                self.grid[sprite.y][sprite.x] = SPRITE_ID # Ensure sprite marker is there

    def simulate_step(self):
        # This method performs one step of the simulation.

        # 1. Update each sprite's state.
        # We iterate over a copy of the sprites list because sprites might be removed or added.
        for sprite in list(self.sprites):
            # Before the sprite makes decisions, we need to know what's in its current spot.
            # If the sprite is on food, we should "consume" it before the sprite perceives.
            # This is a detail of how we synchronize world state.
            if self.grid[sprite.y][sprite.x] == FOOD:
                sprite.hunger = max(0, sprite.hunger - 30) # Eat food
                sprite.energy = min(100, sprite.energy + 10)
                self.grid[sprite.y][sprite.x] = SPRITE_ID # Replace food with sprite

            # Now, let the sprite perceive and decide.
            sprite.update(self.grid)

        # 2. Update the grid based on sprite movements.
        self.update_sprite_positions()
        # 3. Remove food that has been eaten.
        self.update_food()


    def display(self):
        # A simple way to visualize the world.
        print("-" * (self.size * 2 + 1)) # Top border
        for row in self.grid:
            display_row = "|" # Left border
            for cell in row:
                if cell == EMPTY:
                    display_row += "  " # Two spaces for empty
                elif cell == FOOD:
                    display_row += "F " # F for food
                elif cell == OBSTACLE:
                    display_row += "# " # # for obstacle
                elif cell == SPRITE_ID:
                    display_row += "S " # S for sprite
            display_row += "|" # Right border
            print(display_row)
        print("-" * (self.size * 2 + 1)) # Bottom border
        # Print sprite details
        for sprite in self.sprites:
            print(sprite)
        print("\n")


# --- Example Usage ---
if __name__ == "__main__":
    world_size = 10
    simulation = World(world_size)

    # Add some food and obstacles to the world.
    simulation.place_item(random.randint(0, world_size - 1), random.randint(0, world_size - 1), FOOD)
    simulation.place_item(random.randint(0, world_size - 1), random.randint(0, world_size - 1), FOOD)
    simulation.place_item(random.randint(0, world_size - 1), random.randint(0, world_size - 1), FOOD)
    simulation.place_item(5, 5, OBSTACLE)
    simulation.place_item(5, 6, OBSTACLE)
    simulation.place_item(4, 5, OBSTACLE)

    # Create a few sprites.
    sprite1 = Sprite(1, 1, world_size)
    sprite2 = Sprite(8, 8, world_size)
    sprite1.hunger = 60 # Make one sprite a bit hungry initially
    sprite2.energy = 20 # Make another sprite low on energy initially

    # Add sprites to the simulation.
    simulation.add_sprite(sprite1)
    simulation.add_sprite(sprite2)

    # Run the simulation for a few steps.
    num_steps = 20
    for step in range(num_steps):
        print(f"--- Simulation Step: {step + 1} ---")
        simulation.simulate_step()
        simulation.display()
        time.sleep(0.5) # Pause to see the changes

    print("--- Simulation Finished ---")