# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from ..utils import requires_py3

pytestmark = [requires_py3]


def test_make_immutable_check_config():
    # TODO: move imports up top when we drop Python 2
    from immutables import Map

    from datadog_checks.base.utils.models.types import make_immutable_check_config

    obj = make_immutable_check_config(
        {
            'string': 'foo',
            'integer': 9000,
            'float': 3.14,
            'boolean': True,
            'array': [{'key': 'foo'}, {'key': 'bar'}],
            'mapping': {'foo': 'bar'},
        }
    )

    assert isinstance(obj, Map)
    assert len(obj) == 6
    assert isinstance(obj['string'], str)
    assert obj['string'] == 'foo'
    assert isinstance(obj['integer'], int)
    assert obj['integer'] == 9000
    assert isinstance(obj['float'], float)
    assert obj['float'] == 3.14
    assert isinstance(obj['boolean'], bool)
    assert obj['boolean'] is True
    assert isinstance(obj['array'], tuple)
    assert len(obj['array']) == 2
    assert isinstance(obj['array'][0], Map)
    assert obj['array'][0]['key'] == 'foo'
    assert isinstance(obj['array'][1], Map)
    assert obj['array'][1]['key'] == 'bar'
    assert isinstance(obj['mapping'], Map)
    assert len(obj['mapping']) == 1
    assert obj['mapping']['foo'] == 'bar'
