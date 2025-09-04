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

def main():
    if len(sys.argv) < 2:
        print("Usage: python plans.py [add|list]")
        return

if __name__ == "__main__":
    main()