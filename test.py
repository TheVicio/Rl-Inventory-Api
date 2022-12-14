import bakkes_mod_inventory
import rocket_league_utils as rl_utils

inventory = bakkes_mod_inventory.read_inventory()
valid_series_items = tuple(filter(lambda item: rl_utils.serie_utils.has(rl_utils.SERIES, item.serie), inventory))
crimson_items = tuple(filter(lambda item: rl_utils.color_utils.is_exactly(rl_utils.CRIMSON, item.color), inventory))
print(crimson_items)
