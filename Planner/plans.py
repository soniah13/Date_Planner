import json
from pathlib import Path
import sys
import random

DATA_FILE = Path("plans.json")


def load_plans():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_plans(plans):
    with open(DATA_FILE, "w") as f:
        json.dump(plans, f, indent=2)


def add_plans(title):
    plans = load_plans()
    new_plan = {"id": len(plans) + 1, "title": title, "status": "Plan made"}
    plans.append(new_plan)
    save_plans(plans)
    return new_plan


def list_plans():
    plans = load_plans()
    return plans


def draw_plan():
    plans = load_plans()
    unused = [plan for plan in plans if plan["status"] == "Plan made"]
    if not unused:
        for plan in plans:
            plan["status"] = "Lets do it again"
        save_plans(plans)
        return {"message": "All plans reset: 'Lets do it again'", "plans": plans}
    chosen = random.choice(unused)
    for plan in plans:
        if plan["id"] == chosen["id"]:
            plan["status"] = "Date locked In"
            break
    save_plans(plans)
    return {"message": f"Your date plan is: {chosen['title']}", "chosen": chosen}


def mark_done(plan_id: int):
    plans = load_plans()
    for plan in plans:
        if plan["id"] == plan_id:
            if plan["status"] == "Date locked In":
                plan["status"] = "Memory made"
                save_plans(plans)
                return {"message": f"Marked as done: {plan['title']}", "plan": plan}
            else:
                return {
                    "error": f"Plan {plan['id']} is not currently locked in",
                    "status": plan["status"],
                }
    return {"error": f"No plan found with ID {plan_id}"}


def reset_plans():
    plans = load_plans()
    for plan in plans:
        plan["status"] = "Lets do it again"
    save_plans(plans)
    return {"message": "All plans reset: 'Lets do it again'", "plans": plans}


def main():
    if len(sys.argv) < 2:
        print("Usage: python plans.py [add|list|draw|done|reset] [arguments]")
        return
    command = sys.argv[1].lower()
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python plans.py add 'Ice cream date'")
            return
        title = " ".join(sys.argv[2:])
        result = add_plans(title)
        print(f"Added: {result['title']} ({result['status']})")
    elif command == "list":
        plans = list_plans()
        if not plans:
            print("No plans made yet, please add a date plan first")
        else:
            for plan in plans:
                print(f'{plan["id"]}. {plan["title"]} [{plan["status"]}]')
    elif command == "draw":
        result = draw_plan()
        print(result["message"])
    elif command == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Usage: python plans.py done [plan_id]")
            return
        result = mark_done(int(sys.argv[2]))
        print(result.get("message") or result.get("error"))
    elif command == "reset":
        result = reset_plans()
        print(result["message"])
    else:
        print("Unknown command. Please use add, list, draw, done or reset")


if __name__ == "__main__":
    main()
