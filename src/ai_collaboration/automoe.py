from random import choice


class AUTOMoE:
    def __init__(self, ghst_pool):
        """
        Initialize AUTOMoE with a pool of GHSTs.

        :param ghst_pool: List of available GHSTs.
        """
        self.ghst_pool = ghst_pool

    def select_ghst(self, mode):
        """
        Select a GHST based on the specified mode.

        :param mode: The mode of operation ('speedbuild', 'personalized',
        'mixed').
        :return: Selected GHST.
        """
        if mode == "speedbuild":
            return self._automated_selection()
        elif mode == "personalized":
            return self._user_selection()
        elif mode == "mixed":
            return self._mixed_selection()
        else:
            raise ValueError(
                "Invalid mode. Choose from 'speedbuild', 'personalized', or "
                "'mixed'."
            )

    def _automated_selection(self):
        """Automatically select a GHST."""
        return choice(self.ghst_pool)

    def _user_selection(self):
        """Allow the user to select a GHST."""
        print("Available GHSTs:")
        for idx, ghst in enumerate(self.ghst_pool):
            print(f"{idx + 1}: {ghst}")
        choice_idx = int(input("Enter the number of your choice: ")) - 1
        if 0 <= choice_idx < len(self.ghst_pool):
            return self.ghst_pool[choice_idx]
        else:
            raise ValueError("Invalid choice.")

    def _mixed_selection(self):
        """Combine automated and user selection."""
        if choice([True, False]):
            return self._automated_selection()
        else:
            return self._user_selection()
