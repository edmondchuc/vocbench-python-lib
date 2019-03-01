import requests
import json


class VocbenchConnectionError(Exception):
    pass


def auth_login(user, password, endpoint):
    s = requests.session()
    r = s.post(
        endpoint + '/Auth/login',
        data={
            'email': user,
            '_password': password
        }
    )
    if r.status_code == 200:
        return s
    else:
        raise VocbenchConnectionError('Not able to log in. Error from Vocbench: ' + r.content.decode('utf-8'))


def list_projects(s, endpoint):
    r = s.get(endpoint + '/Projects/listProjects', params={'consumer': 'SYSTEM'})
    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        raise VocbenchConnectionError(r.content.decode('utf-8'))


def export_project(s, endpoint, project_name):
    reformatting_exporter_spec = r'{"factoryId":"it.uniroma2.art.semanticturkey.extension.impl.reformattingexporter.' \
                               r'rdfserializer.RDFSerializingExporter",' \
                               r'"configType":"it.uniroma2.art.semanticturkey.extension.impl.reformattingexporter.' \
                               r'rdfserializer.RDFSerializingExporterConfiguration","configuration":{}}'

    r = s.post(endpoint + '/Export/export?ctx_project={0}&outputFormat=Turtle&reformattingExporterSpec={1}'.format(
        project_name, reformatting_exporter_spec))
    if r.status_code == 200:
        return r.content.decode('utf-8')
    else:
        raise Exception(r.content.decode('utf-8'))


def get_output_formats(s, endpoint, project_name):
    r = s.get(endpoint + '/Export/getOutputFormats', params={'ctx_project': project_name})
    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        raise Exception(r.content.decode('utf-8'))


def sparql(s, endpoint, project_name, query):
    r = s.post(endpoint + '/SPARQL/evaluateQuery', data={'query': query, 'ctx_project': project_name})
    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        raise Exception(r.content.decode('utf-8'))