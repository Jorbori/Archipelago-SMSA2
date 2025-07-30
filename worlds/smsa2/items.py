from BaseClasses import Item


class Smsa2Item(Item):
    game: str = "Super Mario Sunshine Arcade 2"


REGULAR_PROGRESSION_ITEMS: dict[str, int] = {
    "Spray Nozzle": 523000,
    "Hover Nozzle": 523001,
    "Rocket Nozzle": 523002,
    "Turbo Nozzle": 523003,
}

TICKET_ITEMS: dict[str, int] = {
    "World 1 Ticket": 523030,
    "World 2 Ticket": 523031,
    "World 3 Ticket": 523032,
    "World 4 Ticket": 523033,
    "World 5 Ticket": 523034,
    "World 6 Ticket": 523035,
    "World 7 Ticket": 523036,
    "World 8 Ticket": 523037,
    "World 9 Ticket": 523038,
    "World 10 Ticket": 523039,
    "World 11 Ticket": 523040,
    "World 12 Ticket": 523041,
}

ALL_PROGRESSION_ITEMS: dict[str, int] = {
    "Shine Sprite": 523004,
    **REGULAR_PROGRESSION_ITEMS,
    **TICKET_ITEMS,
}

JUNK_ITEMS: dict[str, int] = {
    "Green Coin": 523012,
}


ALL_ITEMS_TABLE: dict[str, int] = {
    **ALL_PROGRESSION_ITEMS,
    **JUNK_ITEMS,
}
