##############################  WIP !!!!######################################

import board
import time
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules import direct_pins
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

import adafruit_ssd1306


# --------------------------------------------------
# Keyboard setup
# --------------------------------------------------

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())


# --------------------------------------------------
# Direct switches
# --------------------------------------------------

keyboard.modules.append(
    direct_pins.DirectPins(
        pins=[
            board.D0,  # SW1
            board.D1,  # SW2
            board.D2,  # SW3
            board.D3,  # SW4
        ]
    )
)


# --------------------------------------------------
# Encoders
# --------------------------------------------------

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D6, board.D7, board.D8),    # ROT1
    (board.D9, board.D10, None),       # ROT2
)

encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU, KC.MUTE),   # ROT1
        (KC.NO, KC.NO, KC.NO),         # ROT2 - handled below
    ),
]


# --------------------------------------------------
# OLED
# --------------------------------------------------

i2c = busio.I2C(board.D5, board.D4)

oled = adafruit_ssd1306.SSD1306_I2C(
    128,
    32,
    i2c
)

oled.fill(0)
oled.show()


# --------------------------------------------------
# Keymap
# --------------------------------------------------

keyboard.keymap = [
    [
        KC.LCTRL(KC.LSHIFT(KC.C)),  # SW1
        KC.LCTRL(KC.LSHIFT(KC.V)),  # SW2
        KC.LCTRL(KC.C),             # SW3
        KC.LCTRL(KC.V),             # SW4
    ]
]


# --------------------------------------------------
# Start keyboard
# --------------------------------------------------

keyboard.go()
