import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

    choice = input(menu + "\n>>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            project = add_new_project()
            projects.append(project)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice.")

        choice = input(menu + "\n>>> ").lower()

    save_prompt = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_prompt in ('yes', 'y'):
        save_projects(FILENAME, projects)

    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > date]
    filtered.sort(key=lambda x: x.start_date)
    for project in filtered:
        print(project)


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    project.update(new_percentage=int(new_percentage) if new_percentage else None,
                   new_priority=int(new_priority) if new_priority else None)

if __name__ == '__main__':
    main()
