"""
Wireless AI Smart Hat
DoA Module - ReSpeaker Direction Test

This script provides a standalone test for Direction of Arrival
using the ReSpeaker USB microphone array.
"""

import os
import sys
import time
import usb.core
import usb.util


# ============================================================
# ReSpeaker Configuration
# ============================================================

PIXEL_RING_DIR = os.path.expanduser("~/pixel_ring")
USB_MIC_DIR = os.path.join(
    PIXEL_RING_DIR,
    "usb_4_mic_array"
)

if USB_MIC_DIR not in sys.path:
    sys.path.append(USB_MIC_DIR)

try:
    from tuning import Tuning
except ImportError:
    print("Cannot import ReSpeaker tuning module.")
    print("Expected path:")
    print(USB_MIC_DIR)
    sys.exit(1)


VENDOR_ID = 0x2886
PRODUCT_ID = 0x0018


# ============================================================
# Direction Conversion
# ============================================================

def classify_direction(angle):
    """
    Convert DoA angle into a simplified direction.

    ReSpeaker angle:
    0 / 360 degrees -> Front
    90 degrees       -> Right
    180 degrees      -> Back
    270 degrees      -> Left
    """

    if angle is None:
        return "Unknown"

    angle = angle % 360

    if angle >= 315 or angle < 45:
        return "Front"

    elif 45 <= angle < 135:
        return "Right"

    elif 135 <= angle < 225:
        return "Back"

    else:
        return "Left"


# ============================================================
# Initialize ReSpeaker
# ============================================================

def initialize_respeaker():

    device = usb.core.find(
        idVendor=VENDOR_ID,
        idProduct=PRODUCT_ID
    )

    if device is None:
        print("ReSpeaker USB microphone array not found.")
        return None

    print("ReSpeaker device found.")

    return Tuning(device)


# ============================================================
# Main
# ============================================================

def main():

    tuning = initialize_respeaker()

    if tuning is None:
        return

    print("DoA test started.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:

            angle = tuning.direction

            direction = classify_direction(angle)

            print(
                f"Angle: {angle:>3} degrees"
                f" | Direction: {direction}"
            )

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nDoA test stopped.")


if __name__ == "__main__":
    main()