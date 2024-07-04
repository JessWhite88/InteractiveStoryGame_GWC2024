# InteractiveStoryGame (GWC2024)


Welcome to the Interactive Story Game project! This is a fun and engaging project where you can create and play an interactive story game. You will make choices that affect the outcome of the story, and you can also add your own branches to the story to make it more exciting.

## Project Overview

In this project, you will:
- Learn basic Python programming concepts (code pathway).
- Use GitHub for version control and collaboration (code pathway).
- Create an interactive story with multiple choices and outcomes.
- Share your project with others.
- Alternatively, use Figma to design your interactive story visually without any code (no-code pathway).

## Prerequisites

Before you begin, make sure you have the following:
### For Code Pathway:
- [Python](https://www.python.org/downloads/) (version 3.6 or later)
- [Git](https://git-scm.com/downloads)
- A GitHub account (sign up [here](https://github.com/))

### For No-Code Pathway:
- A [Figma](https://www.figma.com/) account (sign up [here](https://www.figma.com/signup/))

## Setup Instructions

### Code Pathway

Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   Open your terminal or command prompt and run the following command:
   ```sh
   git clone https://github.com/your-username/interactive-story-game.git
   ```
   Replace `your-username` with your GitHub username.

2. **Navigate to the Project Directory:**
   ```sh
   cd interactive-story-game
   ```

3. **Create a Virtual Environment (optional but recommended):**
   ```sh
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

5. **Install Required Packages (if any):**
   This project does not require any external packages, but you can install any additional packages if needed using:
   ```sh
   pip install package-name
   ```

### No-Code Pathway

Follow these steps to set up the project using Figma:

1. **Create a Figma Account:**
   - Go to the [Figma website](https://www.figma.com/) and sign up for a free account.

2. **Create a New Figma Project:**
   - Click on the "New File" button to create a new project.

3. **Design Your Interactive Story Template:**
   - Use Figma's tools to design your interactive story template.
   - Create frames for each part of your story.
   - Use shapes, text, and images to visualize each scene and choice in your story.
   - Connect frames with interactive links to simulate the flow of your story.

## Running the Interactive Story Game

### Code Pathway

1. **Run the Python Script:**
   ```sh
   python story_game.py
   ```

2. **Follow the Prompts:**
   The game will prompt you with choices. Type your choice and press Enter to proceed.

### No-Code Pathway

1. **Design the Story:**
   - Use the Figma project you created to design each scene of your interactive story.

2. **Add Interactivity:**
   - Use Figma's prototype features to add interactivity to your story.
   - Connect frames with clickable links to simulate choices and outcomes.

3. **Share Your Design:**
   - Share the Figma project link with others to showcase your interactive story design.

## Example Game Play

### Code Pathway

Here's an example of what the game looks like:

```
You are in a dark forest. Do you go left or right?
Enter 'left' or 'right': left
You encounter a friendly dragon. He gives you treasure. You win!
```

### No-Code Pathway

Here's an example of how to design your story:

1. **Frame 1:**
   - Text: "You are in a dark forest. Do you go left or right?"
   - Buttons: "Left", "Right"

2. **Frame 2 (Left Choice):**
   - Text: "You encounter a friendly dragon. He gives you treasure. You win!"
   - Button: "Restart"

3. **Frame 3 (Right Choice):**
   - Text: "You fall into a pit. Game over!"
   - Button: "Restart"

## Contributing to the Project

### Code Pathway

You can contribute to this project by adding more branches to the story, fixing bugs, or improving the code. Follow these steps to contribute:

1. **Create a Branch:**
   ```sh
   git checkout -b new-branch-name
   ```

2. **Make Your Changes:**
   Edit the `story_game.py` file to add new branches, fix bugs, or improve the code.

3. **Commit Your Changes:**
   ```sh
   git add .
   git commit -m "Description of your changes"
   ```

4. **Push Your Changes to GitHub:**
   ```sh
   git push origin new-branch-name
   ```

5. **Create a Pull Request:**
   Go to the GitHub repository and create a pull request to merge your changes into the main branch.

### No-Code Pathway

You can contribute to this project by designing more scenes, adding visuals, and improving the interactivity. Follow these steps to contribute:

1. **Duplicate the Figma Project:**
   - Duplicate the existing Figma project to make your changes.

2. **Make Your Changes:**
   - Add new frames, update visuals, and improve the story flow.

3. **Share Your Design:**
   - Share the updated Figma project link with others.

## Example Code

### Code Pathway

Here is a basic structure for the interactive story game in `story_game.py`:

```python
def start_game():
    print("You are in a dark forest. Do you go left or right?")
    choice = input("Enter 'left' or 'right': ")
    if choice == 'left':
        encounter_dragon()
    elif choice == 'right':
        fall_in_pit()
    else:
        print("Invalid choice. Try again.")
        start_game()

def encounter_dragon():
    print("You encounter a friendly dragon. He gives you treasure. You win!")
    restart_game()

def fall_in_pit():
    print("You fall into a pit. Game over!")
    restart_game()

def restart_game():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thanks for playing!")
    else:
        print("Invalid choice. Try again.")
        restart_game()

start_game()
```

### No-Code Pathway

Here is an example of how to design your story in Figma:

1. **Frame 1:**
   - Text: "You are in a dark forest. Do you go left or right?"
   - Buttons: "Left", "Right"

2. **Frame 2 (Left Choice):**
   - Text: "You encounter a friendly dragon. He gives you treasure. You win!"
   - Button: "Restart"

3. **Frame 3 (Right Choice):**
   - Text: "You fall into a pit. Game over!"
   - Button: "Restart"

## Additional Resources

Here are some additional resources to help you learn more about Python, GitHub, and Figma:
- [Python Official Documentation](https://docs.python.org/3/)
- [GitHub Learning Lab](https://lab.github.com/)
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)
- [Real Python Tutorials](https://realpython.com/)
- [Figma Learn](https://www.figma.com/learn/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
