import bakkes_mod_inventory
import rocket_league_utils as rl_utils

inventory = bakkes_mod_inventory.read_inventory()
crimson_items = tuple(filter(lambda item: rl_utils.color_utils.is_exactly(rl_utils.CRIMSON, item.color), inventory))
print(crimson_items)
