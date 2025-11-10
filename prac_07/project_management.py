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
