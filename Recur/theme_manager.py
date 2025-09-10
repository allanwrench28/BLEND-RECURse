import random

class Theme:
    def __init__(self, name, emojis, glyphs, enunciation, expertise_fragments):
        self.name = name
        self.emojis = emojis
        self.glyphs = glyphs
        self.enunciation = enunciation
        self.expertise_fragments = expertise_fragments

    def get_random_emoji(self):
        return random.choice(self.emojis)

    def get_random_glyph(self):
        return random.choice(self.glyphs)

    def get_random_enunciation(self):
        return random.choice(self.enunciation)

    def get_expertise_fragment(self):
        return random.choice(self.expertise_fragments)


class ThemeManager:
    def __init__(self):
        self.themes = {}
        self.current_theme = None

    def add_theme(self, theme):
        self.themes[theme.name] = theme

    def set_theme(self, name):
        if name in self.themes:
            self.current_theme = self.themes[name]
        else:
            raise ValueError(f"Theme '{name}' not found.")

    def get_current_theme(self):
        return self.current_theme

    def swap_theme(self, name):
        self.set_theme(name)

    def get_fragment(self):
        if self.current_theme:
            return self.current_theme.get_expertise_fragment()
        return None

    def get_emoji(self):
        if self.current_theme:
            return self.current_theme.get_random_emoji()
        return None

    def get_glyph(self):
        if self.current_theme:
            return self.current_theme.get_random_glyph()
        return None

    def get_enunciation(self):
        if self.current_theme:
            return self.current_theme.get_random_enunciation()
        return None


# Example themes
upi_theme = Theme(
    name="UPI",
    emojis=["🔌", "🧩", "🛠️"],
    glyphs=["U", "P", "I"],
    enunciation=["Universal", "Plug", "Interface"],
    expertise_fragments=["Automation", "Integration", "Scripting"]
)

science_theme = Theme(
    name="Science",
    emojis=["🔬", "🧪", "🌌"],
    glyphs=["S", "C", "I"],
    enunciation=["Scientific", "Research", "Discovery"],
    expertise_fragments=["Physics", "Biology", "Astronomy"]
)

# Usage
if __name__ == "__main__":
    manager = ThemeManager()
    manager.add_theme(upi_theme)
    manager.add_theme(science_theme)
    manager.set_theme("UPI")
    print(f"Current Theme: {manager.get_current_theme().name}")
    print(f"Emoji: {manager.get_emoji()}")
    print(f"Glyph: {manager.get_glyph()}")
    print(f"Enunciation: {manager.get_enunciation()}")
    print(f"Expertise Fragment: {manager.get_fragment()}")
    manager.swap_theme("Science")
    print(f"\nSwapped to Theme: {manager.get_current_theme().name}")
    print(f"Emoji: {manager.get_emoji()}")
    print(f"Glyph: {manager.get_glyph()}")
    print(f"Enunciation: {manager.get_enunciation()}")
    print(f"Expertise Fragment: {manager.get_fragment()}")
