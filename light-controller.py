import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 20      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def setLEDs(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000)

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--white', action='store_true', help='Sets all LEDs to on max')
parser.add_argument('-o', '--off', action='store_true', help='Sets all LEDs to off')
parser.add_argument('-s', '--hps', action='store_true', help='Set to HPS (High Pressure Sodium)')
parser.add_argument('-t', '--tungsten', action='store_true', help='Set to 40w Tungsten (2600 Kevin)')
parser.add_argument('-x', '--halogen', action='store_true', help='Set to Halogen (3200 Kelvin)')
parser.add_argument('-c', '--candle', action='store_true', help='Set to Candle (1900 Kelvin)')
args = parser.parse_args()
# B,R,G

if args.off:
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  setLEDs(strip, Color(0, 0, 0))

if args.white:
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  setLEDs(strip, Color(255, 255, 255))

if args.hps:
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  setLEDs(strip, Color(76, 255, 183))

if args.tungsten:
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  setLEDs(strip, Color(197, 255, 143))

if args.halogen:
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  setLEDs(strip, Color(224, 255, 241))

if args.candle:
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  setLEDs(strip, Color(41, 255, 147))
