import sys
import os
import logging
import time
import requests
from PyQt5.QtWidgets import QApplication
from src.ui_components.speedbuild_slider import SpeedbuildSlider
from src.ai_collaboration.automoe import AUTOMoE

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Add project root to module search path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)


class AUTOMoESliderDemo:
    def __init__(self, ghst_pool):
        logging.debug("Initializing AUTOMoESliderDemo.")
        self.ghst_pool = ghst_pool
        self.automoe = AUTOMoE(ghst_pool)
        self.slider = SpeedbuildSlider()
        self.slider.slider.valueChanged.connect(self.update_mode)

    def update_mode(self):
        logging.debug("Slider value changed.")
        mode = self.slider.get_mode()
        logging.debug(f"Current mode: {mode}")
        selected_ghst = self.automoe.select_ghst(mode)
        logging.debug(f"Selected GHST: {selected_ghst}")
        print(f"Mode: {mode}, Selected GHST: {selected_ghst}")


# Load GHST pool dynamically from an external source
def load_ghst_pool():
    try:
        # Correct the API endpoint to /ghst_pool
        response = requests.get("http://127.0.0.1:5000/ghst_pool")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to load GHST pool: {e}")
        return [
            {
                "name": "Fallback GHST Alpha",
                "expertise": "General",
                "weight": 1
            },
            {
                "name": "Fallback GHST Beta",
                "expertise": "General",
                "weight": 1
            }
        ]


# Updated GHST pool loading
ghst_pool = load_ghst_pool()


class AUTOMoEAutomation:
    def __init__(self, automoe, slider):
        self.automoe = automoe
        self.slider = slider

    def run(self):
        while True:
            mode = self._auto_select_mode()
            selected_ghst = self.automoe.select_ghst(mode)
            reasoning = self._generate_reasoning(selected_ghst, mode)
            logging.info(
                "Mode: %s, Selected GHST: %s, Reasoning: %s",
                mode, selected_ghst, reasoning
            )
            time.sleep(5)  # Adjust the interval as needed

    def _auto_select_mode(self):
        # Example logic for automated mode selection
        current_hour = time.localtime().tm_hour
        if 9 <= current_hour < 17:
            return "speedbuild"
        elif 17 <= current_hour < 21:
            return "personalized"
        else:
            return "mixed"

    def _generate_reasoning(self, selected_ghst, mode):
        if mode == "speedbuild":
            return (
                f"Selected {selected_ghst} based on weighted attributes for "
                "efficiency."
            )
        elif mode == "personalized":
            return (
                f"User-selected {selected_ghst} for specific expertise."
            )
        elif mode == "mixed":
            return (
                f"Selected {selected_ghst} using a combination of automated "
                "and user-driven selection for balanced decision-making."
            )
        else:
            return "Unknown mode."


class AUTOMoE:
    # Ensure only one definition of AUTOMoE exists

    def _user_selection(self):
        logging.warning(
            "User input is disabled. Falling back to automated selection."
        )
        return self._weighted_selection()

    # ...existing code...


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    demo = AUTOMoESliderDemo(ghst_pool)
    demo.slider.show()

    # Start the automation
    automation = AUTOMoEAutomation(demo.automoe, demo.slider)
    automation.run()

    if not QApplication.instance():
        sys.exit(app.exec_())
