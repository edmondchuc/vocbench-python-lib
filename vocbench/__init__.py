import vocbench.http as http


class Vocbench:
    def __init__(self, user, password, st_core_services_endpoint):
        self.user = user
        self.password = password
        self.endpoint = st_core_services_endpoint

        self.session = http.auth_login(self.user, self.password, self.endpoint)

    def list_projects(self):
        return http.list_projects(self.session, self.endpoint)

    def export_project(self, project_name):
        return http.export_project(self.session, self.endpoint, project_name)

    def get_output_formats(self, project_name):
        return http.get_output_formats(self.session, self.endpoint, project_name)

    def sparql(self, project_name, query):
        return http.sparql(self.session, self.endpoint, project_name, query)