from Options import PerGameCommonOptions, Choice, Toggle, DeathLink, DefaultOnToggle, StartInventoryPool

class HardMode(Toggle):
    """Hard Mode.
    Adds difficult platforming to logic.
    This will require using moves other than those intended to reach certain locations,
    and may not be imediately intuitive."""
    display_name = "Hard Mode"


class BKOptions(PerGameCommonOptions):
    hard_mode: HardMode