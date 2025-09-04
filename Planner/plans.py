import json 
from pathlib import path
import sys
import random

DATA_FILE = Path("plans.json")

def load_plans():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_plans(plans):
    with open(DATA_FILE, 'w') as f:
        json.dump(plans, f, indent=2)

def add_plans(title):
    plans = load_plans()
    new_plan = {"id":len(plans)+1, "title":title, "status":"Plan made"}
    plans.append(new_plan)
    save_plans(plans)
    print(f"Added: {title} (Plan made)")

def list_plans():
    plans = load_plans()
    if not plans:
        print("No plans made yet, please add a date plan first")
        return
    for plan in plans:
        print(f'{plan["id"]}.{plan["title"]} [{plan["status"]}]')
def draw_plan():
    plans = load_plans()
    unused = [plan for plan in plans if plan["status"] == "Plan made"]

    if not unused:
        for plan in plans:
            plan["status"] = "Lets do it again"
        save_plans(plans)
        print("You went to all the date plans made, lets do it again...")
        return
    
    chosen = random.choice(unused)
    for plan in plans:
        if plan["id"] == chosen["id"]:
            plan["status"] = "Date locked In"
            break
        save_plans(plans)
        print(f"Your date plan is: {chosen['title']}")

def mark_done(plan_id:int):
    plans = load_plans()
    for plan in plans:
        if plan["id"] == plan_id:
            if plan["status"] == "Date locked In":
                plan["status"] = "Memory made"
                save_plans(plans)
                print(f'Marked as done: {plan["title"]}(Memory made)')
                return
            else:
                print(f'Plan {plan["id"]} is not currently locked in. Status: {plan["status"]}')
                return
        print(f"No plan found with ID{plan_id}")

def reset_plans():
    plans = load_plans()
    for plan in plans:
        plan["status"] = "Lets do it again"
    save_plans(plans)
    print("All plans reset: 'Lets do it again'")


def main():
    if len(sys.argv) < 2:
        print("Usage: python plans.py [add|list|draw|reset] [arguments]")
        return
    
    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python plans.py add \'Ice cream date\'")
            return
        title = " ".join(sys.argv[2:])
        add_plans(title)

    elif command == "list":
        list_plans()

    elif command == "draw":
        draw_plan()

    elif command ==  "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Usage: python plans.py done [plan_id]")
            return
        mark_done(int(sys.argv[2]))

    elif command == "reset":
        reset_plans()

    else:
        print("Unknown command. Please use add,list, draw,done or reset")


if __name__ == "__main__":
    main()