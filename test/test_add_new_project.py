import pytest

from model.project import Project
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_new_project(app):
    project_name = random_string("name", 10)
    app.session.login("administrator", "root")
    old_projects = app.soap.get_project_list_via_soap("administrator", "root")
    names_of_existing_projects = []
    for element in old_projects:
        name = element.name
        names_of_existing_projects.append(name)
    if project_name not in names_of_existing_projects:
        project = Project(name=project_name)
        app.project.create(project)
        new_projects = app.soap.get_project_list_via_soap("administrator", "root")
        assert len(old_projects) + 1 == len(new_projects)
        old_projects.append(project)
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


        #  get lists of projects from UI:

        # new_projects = app.project.get_project_list()
        # assert len(old_projects) + 1 == len(new_projects)
        # old_projects.append(project)
        # assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
