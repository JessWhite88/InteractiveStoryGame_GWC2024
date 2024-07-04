# Hi, Girls Who Code! :crown: :computer: :keyboard: :magic_wand: 

Welcome to the Interactive Story Game project! This is a fun and engaging project where you can create and play an interactive story game. You will make choices that affect the outcome of the story, and you can also add your own ending to make it more exciting. In this project, we will simulate a real-world scenario where everyone plays a different role on their respective tech team to achieve a common goal. Don't spend too much time deciding on roles because once your part is done, you should still be helping the team. Here are the roles:

### Roles and Descriptions

1. **Software Engineers (at least 2):**
   - **Description:** The Software Engineers write the code that makes the interactive story work. They take the designs from the UX/UI Designer and turn them into a functional game. The engineers should be willing to share their screen in the breakout room.
    - **Skills:** Programming, teamwork, problem-solving.

2. **Quality Assurance (QA) Tester:**
   - **Description:** The QA Tester ensures the interactive story game works correctly by testing it for bugs and issues. They play through the game multiple times to find and report any problems, ensuring a smooth and enjoyable experience for users. they also provide support for the developers through research, code support, etc.
   - **Skills:** Attention to detail, patience, problem-solving.

3. **Project Manager:**
   - **Description:** The Project Manager is responsible for planning, organizing, and managing the project to ensure it is completed on time. They coordinate with all team members, keep track of progress and time, and help solve any issues that arise.
   - **Skills:** Organization, communication, problem-solving.

4. **UX/UI Designer:**
   - **Description:** The UX/UI Designer focuses on the user experience and interface design. They create visual designs and prototypes to make sure the interactive story is engaging and easy to navigate. Feel free to use images, audio, GIFs, and more to visually tell your story.
   - **Skills:** Creativity, design thinking, empathy.

5. **Writer:**
   - **Description:** Writer is responsible for creating and organizing the storyline of the interactive game. They ensure that the narrative is engaging and coherent.
    - **Skills:** Writing, creativity, organization.

**NOTE: The Software Engineers and Quality Assurance Tester will be on the code pathway. The UX/UI Designer and Writer will be on the no-code pathway. The Project Manager will be involved in both pathways.*

## Project Overview

In this project, you will:
- Learn basic Python programming concepts.
- Use GitHub for version control and collaboration.
- Create an interactive story with multiple choices and outcomes.
- Share your project with others.
- Use Figma to design your interactive story visually without any code.

## Prerequisites

Before you begin, make sure you have the following:
### For Code Pathway:
- [Python](https://www.python.org/downloads/) (version 3.6 or later)
- [Git](https://git-scm.com/downloads) - open it and execute Git Bash 
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

2. **Design Your Interactive Story Template:**
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

## Additional Resources

Here are some additional resources to help you learn more about Python, GitHub, and Figma:
- [Python Official Documentation](https://docs.python.org/3/)
- [GitHub Learning Lab](https://lab.github.com/)
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)
- [Real Python Tutorials](https://realpython.com/)
- [Figma Learn](https://www.figma.com/learn/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
