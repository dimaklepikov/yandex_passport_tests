import pytest
from src import runner


def pytest_addoption(parser):
    """Add additional options to the command line parser."""
    parser.addoption(
        "--browser",
        action="store",
        dest="browser",
        type=str,
        choices=("firefox", "chrome"),
        default="chrome",
        help="The browser which automated UI tests will execute using",
    )


@pytest.fixture(scope="session")
def driver(request):
    """A fixture to set up driver depends on CLI option passed"""
    if request.config.getvalue("browser") == "firefox":
        driver = runner.firefox()

    # Set Chrome driver to be default
    driver = runner.chrome()

    yield driver

    # Add teardown callable to a finalizer
    request.addfinalizer(driver.quit)


# @pytest.fixture(autouse=True)
# def capture_test_result(request):
#     yield
#     outcome = request.node.rep_call
#     test_name = request.node.name
#     result = "PASSED" if outcome.passed else "FAILED"
#
#     with open("test_results.txt", "a") as file:
#         file.write(f"Test: {test_name} - Result: {result}\n")
#
