variables = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]
domains = {subject: list(time_slots) for subject in variables}

constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI"),
]


def is_consistent(subject, slot, assignment):
    for a, b in constraints:
        if subject == a:
            other = b
        elif subject == b:
            other = a
        else:
            continue
        if assignment.get(other) == slot:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    subject = next(v for v in variables if v not in assignment)

    for slot in domains[subject]:
        if is_consistent(subject, slot, assignment):
            assignment[subject] = slot
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[subject]

    return None


solution = backtrack({})

if solution:
    print("=== FINAL TIMETABLE ===")
    for slot in time_slots:
        subjects = [s for s in variables if solution[s] == slot]
        print(f"{slot:>9} : {', '.join(subjects) if subjects else '(free)'}")

    print("\n=== ASSIGNMENTS ===")
    for subject in variables:
        print(f"{subject:<7} -> {solution[subject]}")

    print("\n=== CONSTRAINT CHECK ===")
    for a, b in constraints:
        ok = solution[a] != solution[b]
        print(f"{a} != {b} ({solution[a]} vs {solution[b]}): {'SATISFIED' if ok else 'VIOLATED'}")
else:
    print("No valid timetable exists.")