# License Plate Display for Rideshare Drivers

This project uses the [Pimoroni Galactic Unicorn](https://shop.pimoroni.com/products/space-unicorns?variant=40842033561683) - an all-in-one LED matrix display with an integrated Raspberry Pi Pico W. It creates an eye-catching display for rideshare drivers to show their license plate number. The large, outlined text and colorful blinking background make it easy for passengers to spot their driver's vehicle.

![Project Photo](IMG_3663.jpeg)

## Features

- Displays license plate number in clear, high-visibility text
- Blinking background in random colors to stand out
- Customize background and text color with button presses  
- Adjust display brightness to suit conditions
- Easy to personalize text in the code

## Required Hardware

- [Pimoroni Galactic Unicorn](https://shop.pimoroni.com/products/space-unicorns?variant=40842033561683) with integrated Pico W 

## Setup Instructions

1. Update the `text` variable in `main.py` with your license plate number
2. Flash the `main.py` file to your Galactic Unicorn's Pico W
3. Power up the Galactic Unicorn via USB or battery pack

## Operation 

The display will light up showing your plate number over the blinking background.

- Press button A to randomize the background color
- Press button B to randomize the text color
- Use the LUX + and - buttons to brighten or dim the display

## Customization Options

Several aspects can be easily customized by editing the code:

- `text`: Set to your license plate number 
- `color`: Change the initial background color
- Outline color: Edit the pen color in `outline_text()`  
- Animation speed: Adjust the `time.sleep()` duration in the main loop

## Important Notes

- Check local regulations and rideshare company policies before using this device
- Mount securely and ensure the display doesn't obstruct views or distract drivers
- The project is open-source under the MIT License - feel free to adapt the code

I hope this device helps your passengers find you quickly and easily. Happy ridesharing!