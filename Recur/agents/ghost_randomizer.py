import random

UNIQUE_GHOST_EMOJIS = [
    "👻", "🧟", "🧛", "🦇", "🦉", "🦜", "🦄", "🧞",
    "🧙‍♂️", "🧚", "🦸", "🦹", "🧑‍🎤", "🧑‍🦽", "🦢", "🦩"
]

EXTRA_NAMES = [
    "Nova", "Echo", "Blaze", "Aura", "Rune", "Vox", "Pixel", "Shade",
    "Fizz", "Quasar", "Ziggy", "Nebula", "Gizmo", "Wraith", "Spectra", "Bloop"
]

EXTRA_MONIKERS = [
    "The Visionary", "The Maverick", "The Synthesist", "The Oracle",
    "The Trickster", "The Whizbang", "The Oddball", "The Sparkplug"
]

EXTRA_SPECIALTIES = [
    "Quantum UI Animation", "Accessibility Audits", "Dark Mode Psychology",
    "Gamified Onboarding", "Microinteraction Design", "Voice UI Prototyping",
    "Ethical AI Feedback", "Color Theory Wizardry", "Mobile Responsiveness",
    "AR/VR UI Simulation", "Beta Test Automation", "User Persona Simulation",
    "Internationalization", "Neurodiverse UX", "Seasonal Theme Engine",
    "Home Automation Integration"
]

TEAM_ALPHA = [
    ("Zephyr", "The Architect", "", "Purple"),
    ("Bolt", "The Builder", "", "Blue"),
    ("Synapse", "The Thinker", "", "Indigo"),
    ("Nexus", "The Integrator", "", "Teal"),
    ("Echo", "The Debugger", "", "Silver"),
    ("Prism", "The Modularist", "", "Rainbow"),
    ("Sentinel", "The Guardian", "", "Red"),
    ("Luna", "The Designer", "", "Pink")
]

TEAM_BETA = [
    ("Sage", "The Lorekeeper", "", "Gold"),
    ("Pulse", "The Analyst", "", "Green"),
    ("Harmony", "The Auditor", "", "White"),
    ("Atlas", "The Checker", "", "Bronze"),
    ("Muse", "The Creator", "", "Violet"),
    ("Flux", "The Automator", "", "Cyan"),
    ("Unity", "The Builder", "", "Orange"),
    ("Chroma", "The Emojiist", "", "Lime")
]


def blend_color():
    base_colors = [
        "Magenta", "Turquoise", "Amber", "Emerald", "Coral", "Ivory",
        "Chartreuse", "Fuchsia", "Cyan", "Lime", "Peach", "Lavender",
        "Mint", "Aqua", "Saffron", "Ruby", "Sapphire", "Onyx",
        "Gold", "Silver", "Bronze", "Platinum", "Obsidian", "Jade"
    ]
    sheens = [
        "Glossy", "Matte", "Metallic", "Pearlescent", "Neon", "Pastel",
        "Iridescent", "Velvet"
    ]
    hues = [
        "Light", "Dark", "Vivid", "Soft", "Deep", "Bright", "Muted", "Electric"
    ]
    brightness = [
        "High", "Medium", "Low", "Radiant", "Dim", "Luminous",
        "Shadowed", "Sparkling"
    ]
    color = random.choice(base_colors)
    sheen = random.choice(sheens)
    hue = random.choice(hues)
    bright = random.choice(brightness)
    return f"{sheen} {hue} {color} ({bright} brightness)"


def randomize_team(team):
    randomized = []
    specialties = random.sample(EXTRA_SPECIALTIES, len(team))
    emojis = random.sample(UNIQUE_GHOST_EMOJIS, len(team))
    for idx, (name, moniker, _, color) in enumerate(team):
        name = random.choice([name] + EXTRA_NAMES)
        moniker = random.choice([moniker] + EXTRA_MONIKERS)
        color = blend_color()
        specialty = specialties[idx]
        emoji = emojis[idx]
        depth = random.randint(1, 5)
        if depth >= 4:
            name = f"{name} the {specialty.split()[0]} Savant"
        randomized.append({
            "name": name,
            "moniker": moniker,
            "emoji": emoji,
            "color": color,
            "specialty": specialty,
            "depth": depth
        })
    return randomized


def print_teams():
    alpha = randomize_team(TEAM_ALPHA)
    beta = randomize_team(TEAM_BETA)
    print("\n🟣 Team Alpha Ghosts (Coding & Automation)")
    for ghost in alpha:
        print(
            f"{ghost['emoji']} {ghost['name']} ({ghost['moniker']}) - "
            f"{ghost['color']} | Specialty: {ghost['specialty']} | "
            f"Depth: {ghost['depth']}"
        )
    print("\n🟡 Team Beta Ghosts (Research & Brainstorming)")
    for ghost in beta:
        print(
            f"{ghost['emoji']} {ghost['name']} ({ghost['moniker']}) - "
            f"{ghost['color']} | Specialty: {ghost['specialty']} | "
            f"Depth: {ghost['depth']}"
        )


def auto_iterate_uiux(rounds=3):
    print("\n🔁 Auto-Iterating UI/UX Beta Tests...")
    for i in range(1, rounds + 1):
        print(f"\n--- Iteration {i} ---")
        print_teams()
        print(
            "[Simulated] Ghosts run UI/UX auto-sims and beta test themselves!"
        )


if __name__ == "__main__":
    auto_iterate_uiux(rounds=3)


