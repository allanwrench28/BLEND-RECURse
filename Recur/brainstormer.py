import random

class ExpertTeam:
    def __init__(self, name, experts):
        self.name = name
        self.experts = experts

    def get_random_expert(self):
        return random.choice(self.experts)

    def get_all_experts(self):
        return self.experts


class Brainstormer:
    def __init__(self, teams):
        self.teams = teams

    def auto_recommend_team(self, question):
        # Simple keyword-based recommendation (can be replaced with ML/NLP)
        keywords = {
            "math": "Math Masters",
            "science": "Science Squad",
            "automation": "Automation Gurus",
            "plugin": "UPI Architects",
            "ai": "AI Ethicists",
            "data": "Data Wranglers",
            "space": "Cosmic Thinkers"
        }
        for key, team_name in keywords.items():
            if key in question.lower():
                return self.teams.get(team_name)
        # Default: random team
        return random.choice(list(self.teams.values()))

    def get_team(self, name):
        return self.teams.get(name)


# Example expert teams
teams = {
    "Math Masters": ExpertTeam("Math Masters", ["Statician", "Math Magician", "Algorithmist"]),
    "Science Squad": ExpertTeam("Science Squad", ["Astro Physicist", "Bioinformatics Hacker", "Space Systems Designer"]),
    "Automation Gurus": ExpertTeam("Automation Gurus", ["Automation Guru", "Script Alchemist", "Home Automation PhD"]),
    "UPI Architects": ExpertTeam("UPI Architects", ["UPI Architect", "Universal Plugin Engineer"]),
    "AI Ethicists": ExpertTeam("AI Ethicist", ["AI Ethicist", "Neural Network Whisperer"]),
    "Data Wranglers": ExpertTeam("Data Wranglers", ["Data Wrangler", "Statistical anomaly detector"]),
    "Cosmic Thinkers": ExpertTeam("Cosmic Thinkers", ["Cosmic Algorithmist", "Space-time optimizer"])
}

brainstormer = Brainstormer(teams)

if __name__ == "__main__":
    question = input("Enter your hard question: ")
    team = brainstormer.auto_recommend_team(question)
    print(f"Recommended Expert Team: {team.name}")
    print("Experts:", ", ".join(team.get_all_experts()))
