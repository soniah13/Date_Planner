# Date Planner

A simple command-line project to manage and randomly select date plans.  
The idea came from a real situation: having too many exciting date ideas but struggling to decide which one to start with. Instead of spending hours deciding, this project helps by letting the program pick for you.

---

## Features
- **Add a plan**: Save your date ideas into a JSON file.  
- **List plans**: View all saved plans with their status.  
- **Draw a plan**: Randomly select one plan that has not been chosen yet.  
- **Mark done**: Mark a chosen plan as completed once it’s accomplished.  
- **Reset**: Reset all plans when you have gone through them all.  

---

## Statuses
Each plan goes through different statuses:

- `Plan made` — when a new plan is created.  
- `Date locked In` — when the program randomly selects a plan for you.  
- `Memory made` — when the plan has been marked as done.  
- `Lets do it again` — when all plans are finished and reset.  

---

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Date_Planner.git
   cd Date_Planner/Planner
   ```

2. Run the Program by running:
    ```bash
    python plans.py [command] [arguments]
    ```
    
3. Commands 

    - add new plan
    python plans.py add "Ice cream date"
        
    - list all plans
    python plans.py list
        
    - draw a randomised date plan 
    python plans.py draw

    - mark date plan as completed
    python plans.py done [plan_id]

    - reset all plans and start again 
    python plans.py reset

## Why this project
Deciding on which date plan to go for can sometimes take longer than the actual date itself. This project solves that problem by letting the computer decide fairly and randomly. It is simple, fun, and makes life easier while practicing Python basics like file handling, JSON storage, and command-line arguments.