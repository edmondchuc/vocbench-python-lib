# VocBench for Python

*This is a Python library to make web requests to make web requests to an instance of VocBench.* 


## Installation

### pip

`pip install git+https://github.com/edmondchuc/vocbench-python-lib.git#egg=vocbench`


## Usage

```python
if __name__ == '__main__':
    from config import Config
    from vocbench import Vocbench
    import pprint as pp

    v = Vocbench(Config.VB_USER, Config.VB_PASSWORD, Config.VB_ENDPOINT)

    # Get the first project's name returned by list_projects()
    project_name = v.list_projects().get('result')[0].get('name')

    # Get the project's output formats
    pp.pprint(v.get_output_formats(project_name))

    # Export the project as RDF text/turtle
    pp.pprint(v.export_project(project_name))

    query = """ SELECT *
                WHERE {{
                    ?s ?p ?o
                }} LIMIT 10
            """
    pp.pprint(v.sparql(project_name, query))
    
```


## Tests

Tests are done using the pytest framework. Please enter your VocBench credentials and endpoint in the `config.py` to run the tests.
