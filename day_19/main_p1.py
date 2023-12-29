import scrap
import workflow


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def parse_workflows(lines):
    workflows = {}
    for line in lines:
        current_workflow = workflow.wf_from_string(line)
        workflows[current_workflow.name] = current_workflow
    return workflows


def parse_scrap(lines):
    scrap_pile = []
    for line in lines:
        scrap_pile.append(scrap.from_string(line))
    return scrap_pile


def process_full_scrap(
    scrap: scrap.Scrap, workflows: dict[str, workflow.Workflow]
) -> bool:
    current_workflow = "in"
    while True:
        for condition in workflows[current_workflow].conditions:
            step_result = condition.process_scrap_step(scrap=scrap)
            if step_result == "":
                continue
            elif step_result == "R":
                return False
            elif step_result == "A":
                return True
            else:
                current_workflow = step_result
                break
        else:
            # We have ran out of conditions, apply default
            workflow_result = workflows[current_workflow].default
            if workflow_result == "R":
                return False
            elif workflow_result == "A":
                return True
            else:
                current_workflow = workflow_result


def solve(lines: list[str]):
    splitter = lines.index("")
    workflows = parse_workflows(lines[:splitter])
    scrap_pile = parse_scrap(lines[splitter + 1 :])

    print(scrap_pile)
    print(workflows)

    total = 0
    for scrap in scrap_pile:
        if process_full_scrap(scrap, workflows):
            total += scrap.value
    return total


if __name__ == "__main__":
    lines = read_input("day_19/input.txt")
    print(solve(lines))
