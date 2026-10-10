"""
Wireless AI Smart Hat
OLED Module - SSD1322 Display Test

This script provides a standalone test for the SSD1322 OLED
display used in the Wireless AI Smart Hat.
"""

import os
import time

from PIL import Image, ImageDraw, ImageFont

from luma.core.interface.serial import spi
from luma.oled.device import ssd1322


# ============================================================
# OLED Configuration
# ============================================================

OLED_WIDTH = 256
OLED_HEIGHT = 64

FONT_PATH = os.path.expanduser(
    "~/Desktop/NotoSansCJK-Regular.ttc"
)

FONT_SIZE = 20


# ============================================================
# Initialize OLED
# ============================================================

def initialize_oled():
    """
    Initialize SSD1322 OLED through SPI.
    """

    serial = spi(
        port=0,
        device=0,
        gpio_DC=24,
        gpio_RST=25
    )

    device = ssd1322(
        serial,
        width=OLED_WIDTH,
        height=OLED_HEIGHT
    )

    return device


# ============================================================
# Load Font
# ============================================================

def load_font():
    """
    Load Chinese font if available.
    """

    if os.path.exists(FONT_PATH):
        return ImageFont.truetype(
            FONT_PATH,
            FONT_SIZE
        )

    print("Custom font not found.")
    print("Using default font.")

    return ImageFont.load_default()


# ============================================================
# Display Text
# ============================================================

def display_text(device, text, font):
    """
    Display text on the OLED.
    """

    image = Image.new(
        "L",
        (OLED_WIDTH, OLED_HEIGHT),
        0
    )

    draw = ImageDraw.Draw(image)

    draw.text(
        (5, 18),
        text,
        font=font,
        fill=255
    )

    device.display(image)


# ============================================================
# Main
# ============================================================

def main():

    print("Initializing OLED...")

    device = initialize_oled()

    font = load_font()

    print("OLED initialized successfully.")

    test_messages = [
        "Wireless AI Smart Hat",
        "Speech: Hello",
        "Warning: Car Horn",
        "Direction: Left"
    ]

    try:
        for message in test_messages:

            print("Displaying:", message)

            display_text(
                device,
                message,
                font
            )

            time.sleep(2)

        print("OLED test completed.")

    except KeyboardInterrupt:
        print("\nOLED test stopped.")

    finally:
        device.clear()


if __name__ == "__main__":
    main()