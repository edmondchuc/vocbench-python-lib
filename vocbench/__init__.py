import vocbench.http as http


class Vocbench:
    def __init__(self, user, password, st_core_services_endpoint):
        self._user = user
        self._password = password
        self._endpoint = st_core_services_endpoint

        self._session = http.auth_login(self._user, self._password, self._endpoint)

    def list_projects(self):
        return http.list_projects(self._session, self._endpoint)

    def export_project(self, project_name):
        return http.export_project(self._session, self._endpoint, project_name)

    def get_output_formats(self, project_name):
        return http.get_output_formats(self._session, self._endpoint, project_name)

    def sparql(self, project_name, query):
        return http.sparql(self._session, self._endpoint, project_name, query)