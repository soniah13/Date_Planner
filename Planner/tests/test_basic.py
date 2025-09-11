import importlib


def test_planner_module_imports():
    mod = importlib.import_module("planner.plans")
    assert hasattr(mod, "load_plans") or hasattr(mod, "add_plans")
