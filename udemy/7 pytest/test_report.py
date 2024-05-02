import json
import report
import pytest


# @pytest.fixture(scope='function') # it runs the ficture once per each test
# @pytest.fixture(scope='module') # it runs the ficture once per each module in case the fixture is imported in other files
@pytest.fixture(scope='session') # it runs the ficture once for the whole session
def report_json():
    print('\n[ Fixture ]: requested...')
    report.generate_report()
    with open('report.json') as f:
        print('\n[ Fixture ]: ...return report data')
        return json.load(f)


def test_report_json(report_json):
    print('\n[ Test1 ]: received -', report_json)
    assert type(report_json) == dict


def test_report_fields(report_json):
    print('\n[ Test2 ]: received -', report_json)
    assert 'timestamp' in report_json.keys()
    assert 'status' in report_json.keys()
