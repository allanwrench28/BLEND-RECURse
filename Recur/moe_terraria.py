"""
MoE Terraria Clone: Text-based sandbox world powered by infinite expert agents and meta-concept quests.
"""
import random
import json

WORLD_SIZE = 8
BIOMES = ["forest", "desert", "mountain", "lake", "plains"]
RESOURCES = ["wood", "stone", "iron", "water", "crystal"]
META_QUESTS = [
    "Learn recursion by building a fractal tree.",
    "Discover abstraction by crafting a universal tool.",
    "Find emergence in a self-organizing colony.",
    "Practice ethics by helping an NPC in need.",
    "Adapt to a changing biome.",
    "Uncover universal patterns in the world layout."
]


class Tile:
    def __init__(self):
        self.biome = random.choice(BIOMES)
        self.resource = random.choice(RESOURCES)
        self.structure = None
        self.npc = None


class GHSTAgent:
    def __init__(self, name, theme, personality):
        self.name = name
        self.theme = theme
        self.personality = personality
        self.quest = random.choice(META_QUESTS)

    def interact(self):
        return (
            f"{self.name} [{self.theme} | {self.personality}] "
            f"offers quest: {self.quest}"
        )


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.inventory = []
        self.structures = []

    def move(self, dx, dy):
        self.x = max(0, min(WORLD_SIZE-1, self.x + dx))
        self.y = max(0, min(WORLD_SIZE-1, self.y + dy))

    def collect(self, tile):
        self.inventory.append(tile.resource)
        return f"Collected {tile.resource} from {tile.biome}."

    def build(self, tile, structure):
        if tile.structure:
            return "There's already a structure here."
        tile.structure = structure
        self.structures.append((self.x, self.y, structure))
        return f"Built {structure} at ({self.x}, {self.y}) in {tile.biome}."

    def interact_npc(self, npc):
        return npc.interact()


class World:
    def __init__(self):
        self.grid = [[Tile() for _ in range(WORLD_SIZE)] for _ in range(WORLD_SIZE)]
        # Place gHSTS NPCs
        personalities = ["mentor", "trickster", "guide", "guardian", "innovator"]
        for _ in range(5):
            x, y = random.randint(0, WORLD_SIZE-1), random.randint(0, WORLD_SIZE-1)
            theme = random.choice(["recursion", "abstraction", "emergence", "ethics", "adaptability"])
            personality = random.choice(personalities)
            name = f"gHSTS-{theme.capitalize()}"
            self.grid[x][y].npc = GHSTAgent(name, theme, personality)

    def get_tile(self, x, y):
        return self.grid[x][y]


class Game:
    def __init__(self):
        self.world = World()
        self.player = Player()

    def display(self):
        tile = self.world.get_tile(self.player.x, self.player.y)
        info = {
            "location": (self.player.x, self.player.y),
            "biome": tile.biome,
            "resource": tile.resource,
            "structure": tile.structure,
            "npc": tile.npc.name if tile.npc else None,
            "npc_personality": tile.npc.personality if tile.npc else None
        }
        print(json.dumps(info, indent=2))

    def play_turn(self, action):
        tile = self.world.get_tile(self.player.x, self.player.y)
        if action == "move_north":
            self.player.move(0, -1)
        elif action == "move_south":
            self.player.move(0, 1)
        elif action == "move_east":
            self.player.move(1, 0)
        elif action == "move_west":
            self.player.move(-1, 0)
        elif action == "collect":
            print(self.player.collect(tile))
        elif action.startswith("build "):
            structure = action.split(" ", 1)[1]
            print(self.player.build(tile, structure))
        elif action == "interact" and tile.npc:
            print(self.player.interact_npc(tile.npc))
        else:
            print("Invalid action or no NPC here.")
        self.display()



def auto_moe_generation():
    print("[MoE] Auto-generating world, mobs, biomes, and plugins...")
    # Simulate auto-generation (could be expanded for real procedural logic)
    game = Game()
    print("Welcome to gHSTS Sandbox! Type 'move_north', 'move_south', 'move_east', 'move_west', 'collect', 'build <structure>', 'interact', or 'quit'.")
    game.display()
    while True:
        action = input("Action: ").strip()
        if action == "quit":
            print("Thanks for playing!")
            break
        game.play_turn(action)

if __name__ == "__main__":
    auto_moe_generation()
