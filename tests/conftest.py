from copy import deepcopy

import pytest

import app as app_module


initial_activities = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_activities))

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_activities))