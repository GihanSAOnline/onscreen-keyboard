# On-Screen Virtual Keyboard

A fully functional on-screen keyboard built with Python and Tkinter that provides a virtual keyboard interface for typing in any application.

![Keyboard Screenshot](https://via.placeholder.com/800x400/f0f0f0/000000?text=On-Screen+Keyboard+Screenshot)

## Features

- 🎹 **Full QWERTY Layout** - Complete keyboard with all standard keys
- 🔤 **Modifier Keys** - Caps Lock, Shift, Ctrl, Alt with visual feedback
- 📝 **Text Preview** - See what you're typing in real-time
- ⌨️ **Special Keys** - Backspace, Enter, Tab, Space, Arrow keys
- 📋 **Clipboard Support** - Copy and paste functionality
- 🔝 **Always on Top** - Window stays visible above other applications
- 🎨 **Visual Feedback** - Modifier keys change color when active

## Screenshots

### Main Interface
The keyboard features a clean, intuitive interface with a text preview area and full keyboard layout.

### Modifier Keys
- **Caps Lock**: Blue when active
- **Shift**: Green when active
- **Ctrl**: Red when active
- **Alt**: Yellow when active

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Required Dependencies
```bash
pip install pyautogui
```

### Download and Run
1. Clone this repository:
```bash
git clone https://github.com/yourusername/onscreen-keyboard.git
cd onscreen-keyboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python keyboard.py
```

## Usage

1. **Launch the Application**: Run `python keyboard.py`
2. **Position the Window**: The keyboard will appear and stay on top of other windows
3. **Start Typing**: Click any key to type in the currently focused application
4. **Use Modifiers**: Click Caps Lock, Shift, Ctrl, or Alt keys to activate them
5. **Text Preview**: Use the text area at the top to preview your typing
6. **Copy/Paste**: Use the built-in buttons for clipboard operations
7. **Navigation**: Use arrow keys for cursor movement

## File Structure

```
onscreen-keyboard/
│
├── keyboard.py          # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── LICENSE            # MIT License
└── .gitignore         # Git ignore file
```

## Technical Details

### Built With
- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework (built into Python)
- **PyAutoGUI** - For sending keystrokes to other applications

### Key Components
- **OnScreenKeyboard Class** - Main application class
- **GUI Layout** - Organized in rows matching standard keyboard layout
- **Event Handling** - Processes key clicks and modifier states
- **Character Mapping** - Handles shifted characters and special symbols

## Features in Detail

### Text Preview Area
- Shows what you're typing in real-time
- Clear button to reset the text
- Copy/Paste functionality
- Scrollable text area for long content

### Keyboard Layout
- Standard QWERTY layout with proper key sizing
- Special keys (Backspace, Enter, Tab, etc.) appropriately sized
- Arrow keys section for navigation
- All modifier keys with visual state indicators

### Modifier Key Support
- **Caps Lock**: Toggle for permanent capital letters
- **Shift**: Temporary capital letters and special characters
- **Ctrl/Alt**: For keyboard shortcuts (visual feedback only)

## Customization

You can easily customize the keyboard by modifying:
- **Key layouts** in the `create_keyboard()` method
- **Colors** for different key states
- **Window size** and positioning
- **Font sizes** and styles

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Function keys (F1-F12) support
- [ ] Numeric keypad
- [ ] Multiple language layouts
- [ ] Customizable themes and colors
- [ ] Sound effects for key presses
- [ ] Resizable keyboard
- [ ] Settings panel for customization
- [ ] Auto-hide functionality

## Known Issues

- On some systems, you may need to run as administrator for full functionality
- PyAutoGUI failsafe is enabled (move mouse to top-left corner to stop)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's built-in Tkinter library
- Uses PyAutoGUI for cross-platform keyboard automation
- Inspired by the need for accessible virtual keyboards

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Include your Python version and operating system

## Author

Created with ❤️ by [Gihan Sankalpa]

---

⭐ **If you found this project helpful, please give it a star on GitHub!** ⭐
