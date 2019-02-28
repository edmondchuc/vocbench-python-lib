import pytest
from config import Config
from vocbench import Vocbench

#
# -- Fixtures ----------------------------------------------------------------------------------------------------------
#

@pytest.fixture
def get_vocbench_login_session():
    return Vocbench(Config.VB_USER, Config.VB_PASSWORD, Config.VB_ENDPOINT)


@pytest.fixture
def get_a_project(get_vocbench_login_session):
    return get_vocbench_login_session.list_projects().get('result')[0].get('name')


#
# -- Vocbench API Tests ------------------------------------------------------------------------------------------------
#

def test_list_projects(get_vocbench_login_session):
    assert get_vocbench_login_session.list_projects().get('result')


def test_export_project(get_vocbench_login_session, get_a_project):
    project_name = get_a_project
    rdf = get_vocbench_login_session.export_project(project_name)
    assert len(rdf) > 0


def test_get_output_formats(get_vocbench_login_session, get_a_project):
    v = get_vocbench_login_session
    project_name = get_a_project
    output = v.get_output_formats(project_name)
    assert len(output.get('result')) > 0


def test_sparql(get_vocbench_login_session, get_a_project):
    v = get_vocbench_login_session
    project_name = get_a_project

    query = """ SELECT *
                WHERE {{
                    ?s ?p ?o .
                }} LIMIT 10"""

    result = v.sparql(project_name, query)
    assert result.get('result').get('resultType') == 'tuple'
    assert result.get('result').get('sparql').get('head').get('vars') == ['s', 'p', 'o']