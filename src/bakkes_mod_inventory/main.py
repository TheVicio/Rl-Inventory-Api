import csv
import re
import typing
import pathlib
import rocket_league_utils as rl_utils

INVENTORY_PATH = str(pathlib.Path.home()) + r"/AppData/Roaming/bakkesmod/bakkesmod/data/inventory.csv"


class Item(rl_utils.BaseItem):
    def __init__(self, product_id: int, name: str, slot: str, color: str, certification: str, certified_value: int,
                 certified: str, rarity: str, serie: str, trade_lock: bool, quantity: int, instance_id: int):
        self.product_id = product_id
        self.certification_value = certified_value
        self.certification = certification
        self.trade_lock = trade_lock
        self.quantity = quantity
        self.instance_id = instance_id
        super().__init__(name, slot, rarity, False, serie, rl_utils.PC, certified, color)

    def get_product_series(self) -> int:
        result = re.search(r"\?INT\?TAGame\.ProductSeries\.Series(\d{2,4})\?", self.serie)
        return int(result.group(1))


def read_inventory() -> typing.Tuple[Item, ...]:
    with open(INVENTORY_PATH, "r") as file:
        content = csv.reader(file, delimiter=",")
        inventory = tuple()
        for product_id, name, slot, paint, certification, certification_value, certification_label, rarity, crate, \
                tradeable, amount, instance_id in list(content)[1:]:
            trade_lock = tradeable == "false"
            item = Item(int(product_id), name, slot, paint, certification, int(certification_value),
                        certification_label, rarity, crate, trade_lock, int(amount), int(instance_id))
            inventory = inventory + (item, )
        return inventory
