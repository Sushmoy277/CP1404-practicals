"""Project Management - load projects from file"""
"""Estimate: 90 minutes
Actual:     4 hours """

import datetime
from project import Project
from operator import itemgetter

FILENAME = 'project.txt'
DATE_FORMAT = "%d/%m/%Y"


def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def main():
    """Display menu for project management program"""
    print("Welcome to Pythonic Project Management")
    filename = "projects.txt"
    projects = load_projects_from(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    print_menu()
    choice = input(">>> ")
    while choice != "q":
        print_menu()
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load from: ")
            if filename == "":
                filename = FILENAME
            projects = load_projects_from(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ")
            if filename == "":
                filename = FILENAME
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")

        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            answer = input(f"Would you like to save to {filename}? ").lower()
            if answer.startswith("y"):
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")


def load_projects_from(filename):
    """Read projects from a tab-delimited file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            if line.strip():
                parts = line.split("\t")
                name = parts[0]
                start_date = datetime.datetime.strptime(parts[1], DATE_FORMAT).date()
                priority = int(parts[2])
                cost = float(parts[3])
                completion = int(parts[4])
                projects.append(Project(name, start_date, priority, cost, completion))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion", file=out_file)
        for project in projects:
            print(f"{project.name}\t"
                  f"{project.start_date.strftime(DATE_FORMAT)}\t"
                  f"{project.priority}\t"
                  f"{project.cost_estimate:.2f}\t"
                  f"{project.completion}",
                  file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects using itemgetter (less ideal for objects)."""
    incomplete = [(project.priority, project) for project in projects if not project.is_complete()]
    completed = [(project.priority, project) for project in projects if project.is_complete()]
    incomplete.sort(key=itemgetter(0))
    completed.sort(key=itemgetter(0))

    print("Incomplete projects:")
    for priority, project in incomplete:
        print("  ", project.display_line())

    print("Completed projects:")
    for priority, project in completed:
        print("  ", project.display_line())


def filter_projects_by_date(projects):
    """Show projects starting after a given date (using itemgetter)."""
    date_text = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_text, DATE_FORMAT).date()
    filtered = [(project.start_date, project) for project in projects if project.start_date >= filter_date]
    filtered.sort(key=itemgetter(0))
    for start_date, project in filtered:
        print(project.display_line())


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_text = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_text, DATE_FORMAT).date()
    priority = int(input("Priority: "))
    cost_text = input("Cost estimate: $")
    cost = float(cost_text.replace("$", "").replace(",", ""))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Modify completion or priority for a chosen project."""
    for i, project in enumerate(projects):
        print(f"{i} {project.display_line()}")
    choice = input("Project choice: ")
    if choice == "":
        return
    index = int(choice)
    project = projects[index]
    print(project.display_line())
    new_percent = input("New Percentage: ")
    if new_percent != "":
        project.completion = int(new_percent)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


main()
