from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_name("manage_proj_create_page_token")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_css_selector("input[value='Create New Project']" ).click()
        # fill group form
        self.fill_project_form(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects_page()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        projects_list = []
        for element in wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project')]"):
            id = element.get_attribute('href').split("id=", 1)[1]
            name = element.text
            projects_list.append(Project(id=id, name=name))
        return list(projects_list)

    def delete_project_by_name(self, project_name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text("%s" % project_name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()






