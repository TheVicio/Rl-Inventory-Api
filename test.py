from inventory import Inventory
i = Inventory.read()


def test_get_names():
    names = i.get_names()


def test_get_types():
    types = i.get_types()


def test_get_rarities():
    rarities = i.get_rarities()


def test_get_colors():
    colors = i.get_colors()


def test_get_series():
    series = i.get_series()


def test_get_certificates():
    certificates = i.get_certifies()


def test_filter_by_name():
    r = i.filter_by_name("Chequered Flag")


def test_filter_by_color():
    r = i.filter_by_color("Titanium White")


def test_filter_by_type():
    r = i.filter_by_type("Wheel")


def test_filter_by_amount():
    r = i.filter_by_amount(1)


def test_filter_by_certify():
    r = i.filter_by_certify("Striker")


def test_filter_by_series():
    r = i.filter_by_series("RLCS reward")


def test_filter_painted():
    r = i.filter_painted()


def test_filter_certified():
    r = i.filter_certified()


def test_filter_non_crate():
    r = i.filter_non_crate()


def test_filter_blueprint():
    r = i.filter_blueprint()


def test_filter_animated_decal():
    r = i.filter_animated_decal()


def test_filter_antennas():
    r = i.filter_antennas()


def test_filter_avatar_border():
    r = i.filter_avatar_border()


def test_filter_cars():
    r = i.filter_cars()


def test_filter_decals():
    r = i.filter_decals()


def test_filter_engine_audio():
    r = i.filter_engine_audio()


def test_filter_goal_explosion():
    r = i.filter_goal_explosion()


def test_filter_paint_finish():
    r = i.filter_paint_finish()


def test_filter_player_anthem():
    r = i.filter_player_anthem()


def test_filter_banners():
    r = i.filter_banners()


def test_filter_titles():
    r = i.filter_titles()


def test_filter_boost():
    r = i.filter_boost()


def test_filter_toppers():
    r = i.filter_toppers()


def test_filter_trails():
    r = i.filter_trails()


def test_filter_wheels():
    r = i.filter_wheels()


def test_filter_strikers():
    r = i.filter_strikers()