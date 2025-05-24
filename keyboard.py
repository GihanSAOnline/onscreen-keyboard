import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

class OnScreenKeyboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("On-Screen Keyboard")
        self.root.geometry("1000x400")
        self.root.resizable(True, True)
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Variables for keyboard state
        self.caps_lock = False
        self.shift_pressed = False
        self.ctrl_pressed = False
        self.alt_pressed = False
        
        # Text display area
        self.create_text_area()
        
        # Create keyboard layout
        self.create_keyboard()
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_text_area(self):
        """Create a text area to show what's being typed"""
        text_frame = tk.Frame(self.root, bg='lightgray', height=80)
        text_frame.pack(fill='x', padx=5, pady=5)
        text_frame.pack_propagate(False)
        
        # Text display
        self.text_display = tk.Text(text_frame, height=4, font=('Arial', 12), 
                                   wrap='word', bg='white', fg='black')
        self.text_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Buttons frame
        button_frame = tk.Frame(text_frame)
        button_frame.pack(fill='x', pady=2)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_text,
                             bg='lightcoral', fg='white', font=('Arial', 10))
        clear_btn.pack(side='left', padx=2)
        
        # Copy button
        copy_btn = tk.Button(button_frame, text="Copy", command=self.copy_text,
                            bg='lightblue', fg='white', font=('Arial', 10))
        copy_btn.pack(side='left', padx=2)
        
        # Paste button
        paste_btn = tk.Button(button_frame, text="Paste", command=self.paste_text,
                             bg='lightgreen', fg='white', font=('Arial', 10))
        paste_btn.pack(side='left', padx=2)
        
    def create_keyboard(self):
        """Create the main keyboard layout"""
        keyboard_frame = tk.Frame(self.root)
        keyboard_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Keyboard layout definitions
        row1 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace']
        row2 = ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
        row3 = ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Enter']
        row4 = ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift']
        row5 = ['Ctrl', 'Alt', 'Space', 'Alt', 'Ctrl']
        
        # Special key mappings for shift
        self.shift_map = {
            '`': '~', '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
            '6': '^', '7': '&', '8': '*', '9': '(', '0': ')', '-': '_',
            '=': '+', '[': '{', ']': '}', '\\': '|', ';': ':', "'": '"',
            ',': '<', '.': '>', '/': '?'
        }
        
        self.buttons = {}
        
        # Row 1
        row1_frame = tk.Frame(keyboard_frame)
        row1_frame.pack(fill='x', pady=2)
        for i, key in enumerate(row1):
            width = 8 if key != 'Backspace' else 12
            btn = tk.Button(row1_frame, text=key, width=width, height=2,
                           command=lambda k=key: self.key_press(k),
                           font=('Arial', 10), relief='raised')
            btn.pack(side='left', padx=1)
            self.buttons[key] = btn
            
        # Row 2
        row2_frame = tk.Frame(keyboard_frame)
        row2_frame.pack(fill='x', pady=2)
        for key in row2:
            width = 6 if key == 'Tab' else 6
            btn = tk.Button(row2_frame, text=key, width=width, height=2,
                           command=lambda k=key: self.key_press(k),
                           font=('Arial', 10), relief='raised')
            btn.pack(side='left', padx=1)
            self.buttons[key] = btn
            
        # Row 3
        row3_frame = tk.Frame(keyboard_frame)
        row3_frame.pack(fill='x', pady=2)
        for key in row3:
            width = 8 if key == 'Caps' else 10 if key == 'Enter' else 6
            btn = tk.Button(row3_frame, text=key, width=width, height=2,
                           command=lambda k=key: self.key_press(k),
                           font=('Arial', 10), relief='raised')
            btn.pack(side='left', padx=1)
            self.buttons[key] = btn
            
        # Row 4
        row4_frame = tk.Frame(keyboard_frame)
        row4_frame.pack(fill='x', pady=2)
        for key in row4:
            width = 10 if key == 'Shift' else 6
            btn = tk.Button(row4_frame, text=key, width=width, height=2,
                           command=lambda k=key: self.key_press(k),
                           font=('Arial', 10), relief='raised')
            btn.pack(side='left', padx=1)
            self.buttons[key] = btn
            
        # Row 5 (Space bar row)
        row5_frame = tk.Frame(keyboard_frame)
        row5_frame.pack(fill='x', pady=2)
        for key in row5:
            if key == 'Space':
                width = 40
            else:
                width = 8
            btn = tk.Button(row5_frame, text=key, width=width, height=2,
                           command=lambda k=key: self.key_press(k),
                           font=('Arial', 10), relief='raised')
            btn.pack(side='left', padx=1)
            self.buttons[key] = btn
            
        # Arrow keys
        arrow_frame = tk.Frame(keyboard_frame)
        arrow_frame.pack(pady=5)
        
        # Up arrow
        up_btn = tk.Button(arrow_frame, text="↑", width=4, height=1,
                          command=lambda: self.key_press('Up'),
                          font=('Arial', 12))
        up_btn.grid(row=0, column=1, padx=1, pady=1)
        
        # Left, Down, Right arrows
        left_btn = tk.Button(arrow_frame, text="←", width=4, height=1,
                            command=lambda: self.key_press('Left'),
                            font=('Arial', 12))
        left_btn.grid(row=1, column=0, padx=1, pady=1)
        
        down_btn = tk.Button(arrow_frame, text="↓", width=4, height=1,
                            command=lambda: self.key_press('Down'),
                            font=('Arial', 12))
        down_btn.grid(row=1, column=1, padx=1, pady=1)
        
        right_btn = tk.Button(arrow_frame, text="→", width=4, height=1,
                             command=lambda: self.key_press('Right'),
                             font=('Arial', 12))
        right_btn.grid(row=1, column=2, padx=1, pady=1)
        
    def key_press(self, key):
        """Handle key press events"""
        try:
            if key == 'Backspace':
                pyautogui.press('backspace')
                # Also update text display
                current = self.text_display.get("1.0", tk.END)
                if len(current) > 1:  # Don't delete the last newline
                    self.text_display.delete("end-2c", "end-1c")
                    
            elif key == 'Enter':
                pyautogui.press('enter')
                self.text_display.insert(tk.END, '\n')
                
            elif key == 'Tab':
                pyautogui.press('tab')
                self.text_display.insert(tk.END, '\t')
                
            elif key == 'Space':
                pyautogui.press('space')
                self.text_display.insert(tk.END, ' ')
                
            elif key == 'Caps':
                self.toggle_caps_lock()
                
            elif key == 'Shift':
                self.toggle_shift()
                
            elif key == 'Ctrl':
                self.toggle_ctrl()
                
            elif key == 'Alt':
                self.toggle_alt()
                
            elif key in ['Up', 'Down', 'Left', 'Right']:
                pyautogui.press(key.lower())
                
            else:
                # Regular character keys
                char_to_type = self.get_character(key)
                if char_to_type:
                    pyautogui.typewrite(char_to_type)
                    self.text_display.insert(tk.END, char_to_type)
                    
        except Exception as e:
            print(f"Error in key_press: {e}")
            
    def get_character(self, key):
        """Get the character to type based on current modifiers"""
        if len(key) == 1:  # Single character key
            if self.shift_pressed or self.caps_lock:
                if key.isalpha():
                    return key.upper() if (self.caps_lock != self.shift_pressed) else key.lower()
                elif key in self.shift_map:
                    return self.shift_map[key] if self.shift_pressed else key
                else:
                    return key
            else:
                return key.lower() if key.isalpha() else key
        return None
        
    def toggle_caps_lock(self):
        """Toggle caps lock state"""
        self.caps_lock = not self.caps_lock
        btn = self.buttons['Caps']
        if self.caps_lock:
            btn.config(bg='lightblue', relief='sunken')
        else:
            btn.config(bg='SystemButtonFace', relief='raised')
            
    def toggle_shift(self):
        """Toggle shift state"""
        self.shift_pressed = not self.shift_pressed
        for btn in [self.buttons[key] for key in self.buttons if key == 'Shift']:
            if self.shift_pressed:
                btn.config(bg='lightgreen', relief='sunken')
            else:
                btn.config(bg='SystemButtonFace', relief='raised')
                
    def toggle_ctrl(self):
        """Toggle ctrl state"""
        self.ctrl_pressed = not self.ctrl_pressed
        for btn in [self.buttons[key] for key in self.buttons if key == 'Ctrl']:
            if self.ctrl_pressed:
                btn.config(bg='lightcoral', relief='sunken')
            else:
                btn.config(bg='SystemButtonFace', relief='raised')
                
    def toggle_alt(self):
        """Toggle alt state"""
        self.alt_pressed = not self.alt_pressed
        for btn in [self.buttons[key] for key in self.buttons if key == 'Alt']:
            if self.alt_pressed:
                btn.config(bg='lightyellow', relief='sunken')
            else:
                btn.config(bg='SystemButtonFace', relief='raised')
                
    def clear_text(self):
        """Clear the text display area"""
        self.text_display.delete("1.0", tk.END)
        
    def copy_text(self):
        """Copy text from display area to clipboard"""
        try:
            text = self.text_display.get("1.0", tk.END).strip()
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
        except Exception as e:
            print(f"Error copying text: {e}")
            
    def paste_text(self):
        """Paste text from clipboard"""
        try:
            text = self.root.clipboard_get()
            pyautogui.typewrite(text)
            self.text_display.insert(tk.END, text)
        except Exception as e:
            print(f"Error pasting text: {e}")
            
    def on_closing(self):
        """Handle window closing"""
        self.root.destroy()
        
    def run(self):
        """Start the keyboard application"""
        self.root.mainloop()

def main():
    """Main function to run the on-screen keyboard"""
    try:
        # Check if pyautogui is available
        import pyautogui
        pyautogui.FAILSAFE = True  # Enable fail-safe
        
        # Create and run the keyboard
        keyboard = OnScreenKeyboard()
        print("On-Screen Keyboard started successfully!")
        print("The keyboard window will stay on top of other windows.")
        print("Click on any key to type, or use the text area for preview.")
        keyboard.run()
        
    except ImportError:
        print("Error: pyautogui is required but not installed.")
        print("Please install it using: pip install pyautogui")
    except Exception as e:
        print(f"Error starting keyboard: {e}")

if __name__ == "__main__":
    main()
