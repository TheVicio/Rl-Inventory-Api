from pathlib import Path
from item import Item
import csv


class Inventory:
    def __init__(self, items: list[Item]):
        self.items = items

    @staticmethod
    def read(path=None):
        if not path:
            path = Path(str(Path.home()) + "\\AppData\\Roaming\\bakkesmod\\bakkesmod\\data\\inventory.csv")
        with open(path, "r") as file:
            inv = list(csv.reader(file, delimiter=","))
        return Inventory([Item(*item) for item in inv[1:]])

    def save(self, path=None):
        if not path:
            path = str(Path.home()) + "\\inventory.csv"
        with open(path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(Item.get_arguments())
            writer.writerows([list(item.__dict__.values()) for item in self.items])

    def get_values(self, attribute):
        return {getattr(item, attribute) for item in self.items}

    def get_names(self):
        return self.get_values("name")

    def get_types(self):
        return self.get_values("slot")

    def get_rarities(self):
        return self.get_values("quality")

    def get_colors(self):
        return self.get_values("paint")

    def get_series(self):
        return self.get_values("crate")

    def get_certifies(self):
        return self.get_values("certification_label")

    def filter(self, lamb):
        return Inventory(list(filter(lamb, self.items)))

    def filter_by_tradeable(self, tradeable):
        return self.filter(lambda item: item.tradeable == tradeable)

    def filter_tradeable(self):
        return self.filter_by_tradeable("true")

    def filter_not_tradeable(self):
        return self.filter_by_tradeable("false")

    def filter_by_name(self, name):
        return self.filter(lambda item: item.name == name)

    def filter_by_color(self, color):
        return self.filter(lambda item: item.paint == color)

    def filter_by_type(self, type_):
        return self.filter(lambda item: item.slot == type_)

    def filter_by_amount(self, amount):
        return self.filter(lambda item: int(item.amount) == int(amount))

    def filter_by_certify(self, certify):
        return self.filter(lambda item: item.certification_label == certify)

    def filter_by_series(self, series):
        return self.filter(lambda item: item.crate == series)

    def filter_painted(self):
        return self.filter(lambda item: item.paint != "none")

    def filter_certified(self):
        return self.filter(lambda item: item.certification_label != "none")

    def filter_non_crate(self):
        return self.filter_by_series("Postgame")

    def filter_blueprint(self):
        return self.filter_by_type("Blueprint")

    def filter_animated_decal(self):
        return self.filter_by_type("Animated Decal")

    def filter_antennas(self):
        return self.filter_by_type("Antenna")

    def filter_avatar_border(self):
        return self.filter_by_type("Avatar Border")

    def filter_cars(self):
        return self.filter_by_type("Body")

    def filter_decals(self):
        return self.filter_by_type("Decal")

    def filter_engine_audio(self):
        return self.filter_by_type("Engine Audio")

    def filter_goal_explosion(self):
        return self.filter_by_type("Goal Explosion")

    def filter_paint_finish(self):
        return self.filter_by_type("Paint Finish")

    def filter_player_anthem(self):
        return self.filter_by_type("Player Anthem")

    def filter_banners(self):
        return self.filter_by_type("Player Banner")

    def filter_titles(self):
        return self.filter_by_type("Player Title")

    def filter_boost(self):
        return self.filter_by_type("Rocket Boost")

    def filter_toppers(self):
        return self.filter_by_type("Topper")

    def filter_trails(self):
        return self.filter_by_type("Trail")

    def filter_wheels(self):
        return self.filter_by_type("Wheels")

    def filter_strikers(self):
        return self.filter_by_certify("Striker")
