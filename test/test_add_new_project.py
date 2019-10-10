from operator import itemgetter
from collections import OrderedDict
from string import ascii_uppercase as alphabet
from model.project import Project


def test_add_new_project(app, json_projects):
    project = json_projects
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    # assert sorted(old_projects) == new_projects

