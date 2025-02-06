from BaseClasses import Region, Entrance, MultiWorld, Location
from typing import NamedTuple, TypedDict, Dict, Set 
from Locations import spiral_mountain_locations, mumbos_mountain_main_locations

#Move to Locations
class BKLocation(Location):
    game: str = "Banjo-Kazooie"

def create_regions(multiworld: MultiWorld, player: int) -> None:
    menu = Region("Menu", player, multiworld)
    multiworld.regions += menu

    spiral_mountain = Region("Spiral Mountain", player, multiworld)
    spiral_mountain.add_locations(spiral_mountain_locations, BKLocation)
    multiworld.regions += spiral_mountain

    banjos_house = Region("Banjo's House", player, multiworld)
    multiworld.regions += banjos_house

    gl_1_lower = Region("GL: 1 Lower", player, multiworld)
    gl_1_lower.add_locations(["GL Jiggy Entrance", "GL Jiggy Mumbo's Mountain Switch"], BKLocation)
    multiworld.regions += gl_1_lower

    gl_1_upper = Region("GL: 1 Upper", player, multiworld)
    multiworld.regions += gl_1_upper

    mm_main = Region("MM: Main", player, multiworld)
    mm_main.add_locations(mumbos_mountain_main_locations, BKLocation)
    multiworld.regions += mm_main

    mm_mumbo = Region("MM: Mumbo's Hut", player, multiworld)
    multiworld.regions += mm_mumbo

    mm_ticker = Region("MM: Ticker's Tower", player, multiworld)
    mm_ticker.add_locations(["MM Token Ticker's Tower"], BKLocation)
    multiworld.regions += mm_ticker

    mm_ticker_top = Region("MM: Ticker's Tower Top", player, multiworld)
    mm_ticker_top.add_locations(["MM Jiggy Top of Tinker's Tower"], BKLocation)
    multiworld.regions += mm_ticker_top

    menu.connect(spiral_mountain, "Game Start")
    spiral_mountain.connect(banjos_house, "Door to Banjo's House")
    spiral_mountain.connect(gl_1_lower, "Entrance to Grunt's Lair")
    banjos_house.connect(gl_1_lower, "Banjo's House Exit")
    gl_1_lower.connect(spiral_mountain, "Lair Exit")
    gl_1_lower.connect(mm_main, "Mumbos Mountain Entrance")
    gl_1_lower.connect(gl_1_upper, "Slope to GL 1 Upper", lambda state: state.has("Talon Trot", player))
    gl_1_upper.connect(gl_1_lower, "Slope to GL 1 Lower")
    mm_main.connect(gl_1_lower, "Level Exit")
    mm_main.connect(mm_mumbo, "MM: Mumbo's Hut Entrance")
    mm_main.connect(mm_ticker, "Ticker's Tower Bottom Entrance")
    mm_ticker.connect(mm_main, "Ticker's Tower Bottom Exit")
    mm_ticker.connect(mm_ticker_top, "Ticker's Tower Top Exit") #Needs check for termite
    mm_ticker_top.connect(mm_ticker, "Ticker's Tower Top Entrance")
    mm_ticker_top.connect(mm_main, "Drop Down From Ticker's Tower")
    # gl_1_upper.connect(gl_2, "Note Door 1", lambda state: state.has("Notes", player, 50))