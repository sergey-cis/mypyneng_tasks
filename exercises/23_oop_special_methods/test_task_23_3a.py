import pytest
import task_23_3a
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_23_3a, "Topology")


def test_attr_topology(topology_with_dupl_links):
    top_with_data = task_23_3a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    top_with_data = task_23_3a.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_iterable(normalized_topology_example):
    top1 = task_23_3a.Topology(normalized_topology_example)
    try:
        iterator = iter(top1)
    except TypeError as error:
        pytest.fail("An instance of the Topology class is not an iterable\n", error)
    else:
        item = next(iterator)
        assert item == (("R1", "Eth0/0"), ("SW1", "Eth0/1"))
