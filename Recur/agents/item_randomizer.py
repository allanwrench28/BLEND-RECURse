import random

# Photorealistic, emojified coding/statistics/science PhD ghost experts
GHOST_EMOJIS = [
    "👻", "🧑‍🎓", "🧑‍🔬", "🧑‍💻", "🧑‍🚀", "🧑‍🏫", "🧑‍🔧", "🧑‍🎨",
    "🧑‍⚕️", "🧑‍🔭", "🧑‍💼", "🧑‍🌾", "🧑‍🍳", "🧑‍🎤", "🧑‍🎩"
]

ACCESSORIES = [
    "🎩", "👟", "🧢", "🥽", "🕶️", "🧤", "🧣", "🦺", "🪖", "🩴", "🧦", "🪶"
]

NICHES = [
    "Statician", "Quantum Coder", "Automation Guru", "UPI Architect",
    "Home Automation PhD", "Universal Plugin Engineer", "Math Magician",
    "Astro Physicist", "AI Ethicist", "Neural Network Whisperer",
    "Data Wrangler", "Script Alchemist", "Space Systems Designer",
    "Bioinformatics Hacker", "Photorealistic Renderer", "Cosmic Algorithmist"
]

INNOVATIONS = [
    "Self-healing scripts", "Auto-refactoring engine", "Photorealistic code visualizer",
    "Universal API bridge", "Quantum randomizer", "Cosmic math solver",
    "Plug-and-play automation", "Neural plugin generator", "UPI universal adapter",
    "Home IoT orchestrator", "Statistical anomaly detector", "Astro data pipeline",
    "Bio-sequence automator", "AI code reviewer", "Space-time optimizer"
]

PHOTOREALISTIC = ["🖼️", "📸", "🎬", "🪞", "🧬"]


def randomize_ghost():
    emoji = random.choice(GHOST_EMOJIS)
    accessory = random.choice(ACCESSORIES)
    niche = random.choice(NICHES)
    innovation = random.choice(INNOVATIONS)
    photorealistic = random.choice(PHOTOREALISTIC)
    name = f"{emoji}{accessory} {niche}"
    specialty = f"{innovation} {photorealistic}"
    return {
        "name": name,
        "specialty": specialty
    }


def print_randomized_ghosts(n=10):
    for i in range(n):
        ghost = randomize_ghost()
        print(f"Ghost {i+1}: {ghost['name']} | Specialty: {ghost['specialty']}")
        print()


if __name__ == "__main__":
    print_randomized_ghosts(10)
