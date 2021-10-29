from pathlib import Path
from rl_inventory_api.item import Item
import csv
from dataclasses import astuple
from rl_data_utils.inventory.inventory import ABCInventory
from rl_data_utils.item.item import ABCItem


class Inventory(ABCInventory):
    def __init__(self, items: list[Item]):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items: list[ABCItem]):
        self.items = items

    @staticmethod
    def read(path=Path(str(Path.home()) + "\\AppData\\Roaming\\bakkesmod\\bakkesmod\\data\\inventory.csv")):
        with open(path, "r") as file:
            inv = list(csv.reader(file, delimiter=","))
        return Inventory([Item(*item) for item in inv[1:]])

    def save(self, path=str(Path.home()) + "\\inventory.csv"):
        with open(path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["product id", "name", "slot", "paint", "certification", "certification value",
                             "certification label", "quality", "crate", "tradeable", "amount", "instanceid"])
            writer.writerows([astuple(item) for item in self.items])
