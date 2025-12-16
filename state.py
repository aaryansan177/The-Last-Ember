class GameState:
    def __init__(self):
        # Scene control
        self.scene = "intro_winterfell"

        # Trust values
        self.dany_trust = 0
        self.jon_trust = 0
        self.sansa_trust = 0
        self.arya_trust = 0
        self.tyrion_trust = 0

        # Investigation flags
        self.knows_raven_plot = False
        self.knows_target_is_jon = False

        self.told_jon_truth = False
        self.told_dany_truth = False

        self.saw_bran_vision = False
        self.asked_arya_for_help = False
        self.asked_tyrion_for_help = False

        # Strategic choices
        self.supported_sansa_plan = False
        self.supported_arya_plan = False
        self.attempted_peace = False

        self.accused_tyrion = False
        self.accused_generals = False
        self.held_back_on_dragonstone = False

        # Early investigation paths
        self.visited_sansa_early = False
        self.visited_arya_early = False
        self.visited_bran_early = False

        # Meta / UI
        self.unlocked_chapters = {"Chapter 1"}

        self.typing_enabled = True
        self.music_enabled = True
        self.sfx_enabled = True

    # Save / Load helpers
    def to_dict(self):
        """Convert state to serializable dict (for autosave)."""
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data):
        """Restore state from autosave dict."""
        state = cls()
        state.__dict__.update(data)
        return state
