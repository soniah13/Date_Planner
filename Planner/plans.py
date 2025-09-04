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

if __name__ == "__main__":
    main()