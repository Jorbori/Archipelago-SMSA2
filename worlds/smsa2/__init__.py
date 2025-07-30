"""
Archipelago init file for Super Mario Sunshine Arcade 2
"""
import random
from typing import Dict, Any
import os

from BaseClasses import ItemClassification
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, Type, launch_subprocess, icon_paths
from .items import ALL_ITEMS_TABLE, REGULAR_PROGRESSION_ITEMS, ALL_PROGRESSION_ITEMS, TICKET_ITEMS, Smsa2Item
from .locations import ALL_LOCATIONS_TABLE
from .options import Smsa2Options
from .regions import create_regions


class Smsa2WebWorld(WebWorld):
    theme = "ocean"


class Smsa2World(World):
    """
    Created by Augs SMSHacks, Super Mario Sunshine Arcade 2 is a Romhack for Super Mario Sunshine. Featuring 96 platforming gauntlets
    based on mechanics and locations from the base game, the player is given the chance to experience Sunshine's mechanics in a whole
    new light.
    """
    game = "Super Mario Sunshine Arcade 2"
    web = Smsa2WebWorld()

    data_version = 1

    options_dataclass = Smsa2Options
    options: Smsa2Options

    item_name_to_id = ALL_ITEMS_TABLE
    location_name_to_id = ALL_LOCATIONS_TABLE

    goal_shines: int
    possible_shines = 0

    def generate_early(self):
        pick = random.choice(list(TICKET_ITEMS.keys()))
        tick = str(pick)
        print(tick)
        self.multiworld.push_precollected(self.create_item(tick))

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        pool = [self.create_item(name) for name in REGULAR_PROGRESSION_ITEMS.keys()]

        pool += [self.create_item(name) for name in TICKET_ITEMS.keys()]

        
        if len(self.multiworld.get_locations(self.player)) - len(pool) - 1 < self.options.shine_count.value:
            self.options.shine_count.value = len(self.multiworld.get_locations(self.player)) - len(pool) - 1

        if self.options.goal_level_shines > self.options.shine_count.value:
            self.options.goal_level_shines.value = self.options.shine_count.value

        for i in range(0, self.options.shine_count.value):
            pool.append(self.create_item("Shine Sprite"))
            self.possible_shines += 1

        for i in range(0, len(self.multiworld.get_locations(self.player)) - len(pool) - 1):
            pool.append(self.create_item("Green Coin"))

        self.multiworld.itempool += pool

    def create_item(self, name: str):
        if name in ALL_PROGRESSION_ITEMS:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler

        return Smsa2Item(name, classification, ALL_ITEMS_TABLE[name], self.player)

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        self.goal_shines = self.options.goal_level_shines
        if self.goal_shines > self.possible_shines:
            self.goal_shines = self.possible_shines

    
    def fill_slot_data(self) -> Dict[str, Any]:
        return {"difficulty": self.options.difficulty.value,
                "shine_count": self.options.shine_count.value,
                "goal_level_shines": self.options.goal_level_shines.value,
                "shine_sanity": self.options.shine_sanity.value,
                "blue_coin_sanity": self.options.blue_coin_sanity.value}
    
    def interpret_slot_data(self, slot_data: dict[str, Any]) -> None:
        if "starting_location" in slot_data:
            self.origin_region_name = slot_data["starting_location"]

        if "entrances" in slot_data:
            # Update entrance connections for ER
            entrances = {
                entrance.name: entrance
                for region in self.get_regions()
                for entrance in region.entrances
            }
            for source_exit, target_entrance in slot_data["entrances"]:
                entrances[source_exit].connected_region = entrances[target_entrance].parent_region


def launch_client():
    from .SMSA2Client import main
    launch_subprocess(main, name="SMSA2 client")


def add_client_to_launcher() -> None:
    version = "0.1.0"
    found = False
    for c in components:
        if c.display_name == "Super Mario Sunshine Arcade 2 Client":
            found = True
            if getattr(c, "version", 0) < version:
                c.version = version
                c.func = launch_client
                return
    if not found:
        icon_paths["smsa2_ico"] = f"ap:{__name__}/icon.png"
        components.append(Component("Super Mario Sunshine Arcade 2 Client", "SMSA2 Client", func=launch_client, component_type=Type.CLIENT, icon="smsa2_ico"))


add_client_to_launcher()
