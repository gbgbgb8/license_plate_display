# License Plate Display for Rideshare Drivers

This project uses the [Pimoroni Galactic Unicorn](https://shop.pimoroni.com/products/galactic-unicorn) LED matrix display to create an eye-catching and informative display for rideshare drivers. The display shows the driver's license plate number along with additional text, making it easy for passengers to identify their driver's vehicle.

![Project Photo](IMG_3663.jpeg)

## Features

- Displays license plate number and additional text in a clear, high-visibility format
- Blinking background in random colors to attract attention
- Themed color schemes for different seasons or moods
- Customizable text and color settings
- Adjustable display brightness
- Button controls for easy interaction

## Required Hardware

- [Pimoroni Galactic Unicorn](https://shop.pimoroni.com/products/galactic-unicorn) LED matrix display

## Setup Instructions

1. Update the `texts` list in the code with your license plate number and any additional text you want to display.
2. Customize the `text_durations` list to set the display duration (in seconds) for each text item.
3. Flash the code to your Galactic Unicorn using a compatible IDE or utility.
4. Power on the Galactic Unicorn and enjoy your personalized display!

## Usage

The display will cycle through the text items defined in the `texts` list, showing each item for the corresponding duration specified in `text_durations`.

Use the following buttons to interact with the display:

- **Button A**: Randomize the background color.
- **Button B**: Randomize the text color.
- **Button C**: Cycle through different themed color schemes.
- **LUX + Button**: Increase the display brightness.
- **LUX - Button**: Decrease the display brightness.

The themed color schemes add a fun and seasonal touch to your display. The available themes are:

- Spring
- Summer
- Autumn
- Winter

Each theme has its own set of color schemes, and pressing Button C will randomly select a color scheme from the current theme.

## Customization

You can easily customize various aspects of the display by modifying the code:

- `texts`: Update this list to change the displayed text items.
- `text_durations`: Modify this list to adjust the display duration for each text item.
- `themed_color_schemes`: Add or modify the color schemes for each theme to suit your preferences.
- `BUTTON_DELAY`: Adjust this value to change the delay between button presses, preventing accidental rapid changes.

Feel free to experiment and make the display truly your own!

## Safety and Legal Considerations

- Ensure that the display is securely mounted and does not obstruct your view while driving.
- Check your local regulations and rideshare company policies regarding the use of such displays in your vehicle.
- Avoid looking at the display for extended periods while driving, as it may cause distraction.
- The project code is provided as-is, without any warranty or guarantee of its suitability for your specific use case.

## Contributing

If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request on the project's GitHub repository.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

Special thanks to the Pimoroni team for creating the amazing Galactic Unicorn LED matrix display and providing excellent documentation and resources.

Enjoy your ride and stay safe!