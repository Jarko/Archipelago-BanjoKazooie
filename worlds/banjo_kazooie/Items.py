from BaseClasses import ItemClassification, Item
from typing import NamedTuple, TypedDict, Dict, Set 

class ItemData(NamedTuple):
    memadd: str = 0
    value: str = 0
    type: str = ""
    qty: int = 1

item_table: Dict[str, ItemData] = {
    #"Extra Lives": ItemData("385F8B", "", ItemClassification.filler, 2),
    "Empty Honey Comb": ItemData("385F7F", "", ItemClassification.useful, 8),
    "Jiggies": ItemData("385FCB", "", ItemClassification.useful, 12),
    #"Notes": ItemData("??? set pr world", "", ItemClassification.useful, 10), # 10 x 10 batches
    "Mumbo Tokens": ItemData("385FA3", "", ItemClassification.progression, 5),

    #Moves'
    "Camera": ItemData("37C3A2", "0000", ItemClassification.filler),
    "Climbing": ItemData("37C3A2", "0020", ItemClassification.progression),
    "Diving": ItemData("37C3A2", "8000", ItemClassification.progression),
    "Beak Barge": ItemData("37C3A2", "0001", ItemClassification.progression),
    "High Jump": ItemData("37C3A2", "0400", ItemClassification.progression),
    "Double Jump": ItemData("37C3A2", "0080", ItemClassification.progression),
    "FlapFlip": ItemData("37C3A2", "0100", ItemClassification.progression),
    "Claw Swipe": ItemData("37C3A2", "0010", ItemClassification.progression),
    "Roll": ItemData("37C3A2", "1000", ItemClassification.progression),
    "Rat-At-Tat Rap": ItemData("37C3A2", "0800", ItemClassification.progression),
    "Talon Trot": ItemData("37C3A0", "0001", ItemClassification.progression),
    "Beak Buster": ItemData("37C3A2", "0004", ItemClassification.progression),
    "Eggs": ItemData("37C3A2", "0040", ItemClassification.progression),
}