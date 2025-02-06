from BaseClasses import ItemClassification, Item
from typing import NamedTuple, TypedDict, Dict, Set 

class LocationData(NamedTuple):
    memadd: str = 0
    value: str = 0

spiral_mountain_locations : Dict[str, LocationData] = {
    "SM HC Stump":                  LocationData("3832E2", "0800"),
    "SM HC Tree":                 LocationData("3832E2", "4000"),
    "SM HC Waterfall":            LocationData("3832E2", "1000"),
    "SM HC Underwater":           LocationData("3832E2", "2000"),
    "SM HC Boulder":                LocationData("3832E2", "0100"),
    "SM HC Coli":                   LocationData("3832E2", "8000"),

    "SM Move Camera Molehill":      LocationData("3832C6", "1"),
    "SM Move Stumps Molehill":      LocationData("3832C6", "2"),
    "SM Move Diving Molehill":      LocationData("3832C6", "3"),
    "SM Move Climbing Molehill":    LocationData("3832C6", "4"),
    "SM Move Quarry Molehill":      LocationData("3832C6", "5"),
    "SM Move Garden Molehill":      LocationData("3832C6", "6"),
}

mumbos_mountain_main_locations : Dict[str, LocationData] = {
    "MM HC Top of Spinning Totem": LocationData("3832E0", "0400"),
    "MM HC Lake Cave": LocationData("3832E0", "0200"),

    "MM Stonehenge Molehill":   LocationData("3832C6", "7"),
    "MM Jungle Molehill":   LocationData("3832C6", "8"),
    "MM Village Molehill":   LocationData("3832C6", "9"),

    "MM Jiggy Orange Switches":           LocationData("3832C0", "0100"),
    "MM Jiggy Give Monkey Orange":        LocationData("3832C0", "0002"),
    "MM Jiggy Beat Conga":                LocationData("3832C0", "0004"),
    "MM Jiggy Middle of Stonehenge":      LocationData("3832C0", "4000"),
    "MM Jiggy On Slope":                  LocationData("3832C0", "8000"),
    "MM Jiggy Feed Spinning Totem":       LocationData("3832C0", "1000"),
    # "MM Jiggy Save Jinjos":               LocationData("3832C0", "0200"),
    "MM Jiggy Inside Hut":                LocationData("3832C0", "2000"),
    "MM Jiggy Mumbo's Hut Eye":           LocationData("3832C0", "0800"),

    "MM Token Behind Pillar": LocationData("3832F0", "1000"),
    "MM Token Jungle Pillars": LocationData("3832F0", "0200"),
    "MM Token Behind Stonehenge": LocationData("3832F0", "0400"),
    "MM Token Under Stairs to Mumbo's Hut": LocationData("3832F0", "0800"),

    "MM Jinjo Purple Pillar Starting Area": LocationData("385F7B", "08"),
    "MM Jinjo Blue Lake": LocationData("385F7B", "01"),
    "MM Jinjo Orange On Stonehenge": LocationData("385F7B", "04"),
    "MM Jinjo Yellow On Slope": LocationData("385F7B", "10"),
    "MM Jinjo Green Inside Hut": LocationData("385F7B", "02"),
}

location_table: Dict[str, LocationData] = {
    "GL Jiggy Entrance":                  LocationData("3832C6", "0800"),
    "GL Jiggy Mumbo's Mountain Switch":   LocationData("3832C6", "1000"),
    "MM Jiggy Top of Tinker's Tower":     LocationData("3832C0", "0400"),
    "MM Token Ticker's Tower": LocationData("3832F0", "2000"),
    #"TTC Token Behind Lighthosue Door": LocationData("3832F0", "0004"),
    #"GL Token Behind Lobby Purple Cauldren": LocationData("3832FA", "0200"),
    #"GL Token Click Clock Wood Painting Room": LocationData("3832FA", "0400"),
}