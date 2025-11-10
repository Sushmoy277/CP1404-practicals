"""Project Management - load projects from file"""
"""Estimate: 90 minutes
Actual:     minutes"""

import csv
import datetime
from project import Project

DATE_FORMAT = "%d/%m/%Y"


def load_projects_from(filename):
    """Read projects from a tab-delimited file."""
    projects = []
    with open(filename, "r", newline="") as in_file:
        reader = csv.reader(in_file, delimiter="\t")
        next(reader)  # skip header
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
