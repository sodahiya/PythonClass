from pyfiglet import Figlet
from termcolor import colored

# Create ASCII art text
fig = Figlet(font='bulbhead')  # Try 'block', 'doom', or 'slant' fonts for variety
ascii_art = fig.renderText('Obsidian Shell')

# Add color to the text
colored_art = colored(ascii_art, 'cyan', attrs=['bold'])

# Display the fancy output
print(colored_art)