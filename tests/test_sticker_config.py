import unittest
from src.data_readers.config.stickers.sticker_config import *

KEY = "first"
VALUE = "hgarghakdjlgjkdsfhgkjds21783"

class TestStickerConfig(unittest.TestCase):
    def test_add_sticker(self):
        stickers_config = get_sticker_config()
        stickers_config["stickers"][KEY] = VALUE  # type: ignore
        add_sticker(KEY, VALUE)
        self.assertEqual(get_sticker_config(), stickers_config)

    def test_remove_sticker(self):
        add_sticker(KEY, VALUE)
        stickers_config = get_sticker_config()
        del stickers_config["stickers"][KEY] # type: ignore
        remove_sticker(KEY)

        self.assertEqual(get_sticker_config(), stickers_config)

    def test_set_main_sticker(self):
        add_sticker(KEY, VALUE)
        stickers_config = get_sticker_config()
        stickers_config["chosen_sticker"] = KEY
        set_main_sticker(KEY)
        self.assertEqual(get_sticker_config(), stickers_config)

    def test_set_main_sticker_pass_unexistent_key_raise_error(self):
        stickers_config = get_sticker_config()
        stickers_config["chosen_sticker"] = VALUE
        add_sticker(KEY, VALUE)
        self.assertRaises(ValueError, set_main_sticker, "unexistent_key")
    #TODO дописать тесты и начать делать хендлер с фильтрами для админки