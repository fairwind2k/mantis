from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://mantis:8080/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list_via_soap(self, username, password):
        projects_list = []
        client = Client("http://mantis:8080/api/soap/mantisconnect.php?wsdl")
        project_data = client.service.mc_projects_get_user_accessible(username, password)
        for elem in project_data:
            id = elem[0]
            name = elem[1]
            projects_list.append(Project(id=id, name=name))
        return list(projects_list)

