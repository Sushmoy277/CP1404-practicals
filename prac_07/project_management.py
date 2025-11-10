"""Project Management - load projects from file"""
"""Estimate: 90 minutes
Actual:     minutes"""

import csv
import datetime
from project import Project
from operator import itemgetter

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

    choice = input(">>> ")
    while choice != "q":
        print_menu()
        choice = input(">>> ").lower()
        if choice == "l":
            name = input("Filename to load from: ")
            projects = load_projects_from(name)
        elif choice == "s":
            name = input("Filename to save to: ")
            save_projects_to(name, projects)
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
                save_projects_to(filename, projects)
            print("Thank you for using custom-built project management software.")


def load_projects_from(filename):
    """Read projects from a tab-delimited file."""
    projects = []
    with open(filename, "r", newline="") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name = row[0]
            start_date = datetime.datetime.strptime(row[1], DATE_FORMAT).date()
            priority = int(row[2])
            cost = float(row[3])
            completion = int(row[4])
            projects.append(Project(name, start_date, priority, cost, completion))
    return projects


def save_projects_to(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion"])
        for p in projects:
            writer.writerow([p.name,
                             p.start_date.strftime(DATE_FORMAT),
                             p.priority,
                             f"{p.cost_estimate:.2f}",
                             p.completion])


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    completed = [project for project in projects if project.is_complete()]
    incomplete.sort()
    completed.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(" ", project.display_line())
    print("Completed projects:")
    for project in completed:
        print(" ", project.display_line())


def filter_projects_by_date(projects):
    """Show projects starting after a given date."""
    date_text = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_text, DATE_FORMAT).date()
    filtered = [project for project in projects if project.start_date >= filter_date]
    filtered.sort(key=itemgetter("start_date"))
    for project in filtered:
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
