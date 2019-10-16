import random

from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.get_project_list_via_soap("administrator", "root")
    print('\nold_projects:', old_projects)
    if len(old_projects) == 0:
        app.project.create(Project(name="Test5656"))
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_project_list_via_soap("administrator", "root")
    print('\nnew_projects:', new_projects)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(old_projects, key=Project.id_or_max)