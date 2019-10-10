import random

from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        app.project.create(Project(name="Test5656"))
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_groups = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_groups)