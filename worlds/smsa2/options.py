from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Range, Toggle

class Difficulty(Choice):
    """The difficulty of the randomizer's logic.
    Standard: Logic only requires tricks at a similar level of difficulty to the base game
    Hard: Logic requires some advanced tech and more difficult execution compared to the base game
    Expert: Logic requires glitches and extremely difficult execution"""
    display_name = "Difficulty"
    option_standard = 0
    alias_normal = 0
    alias_medium = 0
    option_hard = 1
    option_expert = 2
    alias_extreme = 2
    alias_salty_tears = 2
    alias_tears = 2
    default = 0

class ShineCount(Range):
    """How many Shine Sprite items appear in the item pool
    If this number of shines is less than the availiable locations, it will be adjusted to the number of availible locations"""
    display_name = "Shine Count"
    range_start = 1
    range_end = 171
    default = 75

class GoalLevelShines(Range):
    """How many Shine Sprites are required to access level 12-8.
    If less than this number of Shines exist in the pool, it will be adjusted to the total Shine count."""
    display_name = "Goal Level Shines"
    range_start = 0
    range_end = 170
    default = 40

class ShineSanity(Toggle):
    """Enables Shine Sprites in the location pool. 
    Note that if Blue Coin Sanity is also disabled, this will be forcefully enabled"""
    display_name = "Shine Sanity"
    default = True

class BlueCoinSanity(Toggle):
    """Enables Blue Coins in the location pool. 
    Note that if this is the only location option selected, you may find yourself saving and qutting the game regularly to exit levels"""
    display_name = "Blue Coin Sanity"

@dataclass
class Smsa2Options(PerGameCommonOptions):
    difficulty: Difficulty
    shine_count: ShineCount
    goal_level_shines: GoalLevelShines
    shine_sanity: ShineSanity
    blue_coin_sanity: BlueCoinSanity
