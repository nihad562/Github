def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en-gb')
