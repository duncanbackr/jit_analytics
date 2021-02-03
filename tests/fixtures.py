import pytest
from Analytics.addbadge import add_badge
from Analytics.growthscore import add_growth_score
from Analytics.retainscore import add_retain_score
from Analytics.badgescore import add_fan_score
from Analytics.preparedict import unpack
from math import nan

##################badge fixtures######################

@pytest.fixture(scope='function')
def new_fan():
    return add_badge(1, 2, 1589318511000, nan, 1592585039000)

@pytest.fixture(scope='function')
def top_fan():
    return add_badge(3, 2, 1589318511000, nan, 1592585039000)

@pytest.fixture(scope='function')
def trend_fan():
    return add_badge(2, 2, 1589318511000, 1593103439000, 1592585039000)

@pytest.fixture(scope='function')
def re_engaged_fan():
    return add_badge(2, 2, 1591807439000,1581356639000, 1592585039000)

@pytest.fixture(scope='function')
def other_fan():
    return add_badge(2, 2, 1580924639000, 1578246239000,1592585039000 )


############score fixtures###################

@pytest.fixture(scope='function')
def growth():
    badge = add_badge(2, 2, 1592239439000,nan, 1592585039000)
    return add_growth_score(2, 2, 0,1592239439000,nan, 1592585039000, badge )


@pytest.fixture(scope='function')
def retain():
    badge = add_badge(3, 2,1592498639000, 1586537039000,1592585039000 )
    return add_retain_score(3, 2, 1, 0, 1592498639000, 1586537039000,1592585039000, badge )


@pytest.fixture(scope='function')
def badge():
    badge = add_badge(6, 3, 1592239439000,1591375439000, 1592585039000 )
    return add_fan_score(6, 3, 0, 1592239439000,1591375439000, 1592585039000, badge)

################exception fixtures#################

@pytest.fixture(scope='function')
def neg_date():
    badge = add_badge(6, 3, -1592239439000,1591375439000, 1592585039000 )
    return add_fan_score(6, 3, 0, -1592239439000,1591375439000, 1592585039000, badge)


@pytest.fixture(scope='function')
def empty():
    badge = add_badge(nan, 2, 1592239439000, nan, 1592585039000)
    return add_fan_score(nan, nan, nan, 1592239439000, nan, 1592585039000, badge)

@pytest.fixture(scope='function')
def unpack_row():
    fan = [3, nan, 2, 'content', False, 1589318511000, 'video', 1, 0, 0, nan, 'fan_name', 'url', 1592585039000]
    return unpack(fan)




