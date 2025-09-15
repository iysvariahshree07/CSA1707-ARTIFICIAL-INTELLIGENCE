def vacuum_world(states):
    for loc, status in states.items():
        print(f"Vacuum at {loc}, Status: {status}")
        if status == "Dirty":
            print(f"Action: Clean {loc}")
            states[loc] = "Clean"
        else:
            print(f"Action: Move to next")
    print("Final state:", states)

states = {"A": "Dirty", "B": "Clean"}
vacuum_world(states)
