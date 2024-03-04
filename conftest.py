import pytest
from comtypes.client import CreateObject
import os
from fixture.application import Application



@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\PycharmProjects\\addressbook\\addressbook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x[0]) for x in testdata])

def load_from_xlsx(file):
    try:
        project_dir = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(project_dir, "groups.xlsx")
        xl = CreateObject("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(file)
        return xl.Range["A%s:A%s" % (1, 10)].Value()
        xl.Quit()
    finally:
        try:
            xl.Quit()
        except:
            pass
