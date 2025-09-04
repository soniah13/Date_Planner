import json 
form pathlib import path
import sys

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

def main():
    if len(sys.argv) < 2:
        print("Usage: python plans.py [add|list]")
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

if __name__ == "__main__":
    main()