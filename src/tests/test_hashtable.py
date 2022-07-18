import pytest
from pytest_unordered import unordered

from entities.hashtable import HashTable


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 0


def test_should_create_empty_pair_slots():
    # Given
    hashtable = HashTable(capacity=3)
    expected_values = [None] * 3

    # When
    actual_values = hashtable._HashTable__pairs
    # shouldn't really access the private pairs attribute

    # Then
    assert actual_values == expected_values


@pytest.fixture
def sample_hashtable_1():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data


def test_should_insert_key_value_pairs(sample_hashtable_1):
    assert ("hola", "hello") in sample_hashtable_1.pairs
    assert (98.6, 37) in sample_hashtable_1.pairs
    assert (False, True) in sample_hashtable_1.pairs

    assert len(sample_hashtable_1) == 3


def test_should_raise_error_on_missing_key(sample_hashtable_1):
    with pytest.raises(KeyError) as exception_info:
        sample_hashtable_1["missing_key"]
    assert exception_info.value.args[0] == "missing_key"


def test_should_delete_key_value_pair(sample_hashtable_1):
    assert "hola" in sample_hashtable_1
    assert ("hola", "hello") in sample_hashtable_1.pairs
    assert len(sample_hashtable_1) == 3

    del sample_hashtable_1["hola"]

    assert "hola" not in sample_hashtable_1
    assert ("hola", "hello") not in sample_hashtable_1.pairs
    assert len(sample_hashtable_1) == 2


def test_should_raise_error_on_get_deleted_key(sample_hashtable_1):
    del sample_hashtable_1["hola"]
    with pytest.raises(KeyError) as exception_info:
        sample_hashtable_1["hola"]
    assert exception_info.value.args[0] == "hola"


def test_should_find_key(sample_hashtable_1):
    assert "hola" in sample_hashtable_1


def test_should_not_find_key(sample_hashtable_1):
    assert "missing_key" not in sample_hashtable_1


def test_should_get_value(sample_hashtable_1):
    assert sample_hashtable_1.get("hola") == "hello"


def test_should_get_none_when_missing_key(sample_hashtable_1):
    assert sample_hashtable_1.get("missing_key") is None


def test_should_get_default_value_when_missing_key(sample_hashtable_1):
    assert sample_hashtable_1.get("missing_key", "default") == "default"


def test_should_get_value_with_default(sample_hashtable_1):
    assert sample_hashtable_1.get("hola", "default") == "hello"


def test_should_raise_error_when_deleting_missing_key(sample_hashtable_1):
    with pytest.raises(KeyError) as exception:
        del sample_hashtable_1["missing_key"]
    assert exception.value.args[0] == "missing_key"


def test_should_return_key_value_pairs(sample_hashtable_1):
    assert ("hola", "hello") in sample_hashtable_1.pairs
    assert (98.6, 37) in sample_hashtable_1.pairs
    assert (False, True) in sample_hashtable_1.pairs


def test_should_not_contain_none_value_when_created():
    hashtable = HashTable(capacity=100)
    assert None not in hashtable.values


def test_should_return_copy_of_pairs(sample_hashtable_1):
    assert sample_hashtable_1.pairs is not sample_hashtable_1.pairs


def test_should_not_include_blank_pairs(sample_hashtable_1):
    assert None not in sample_hashtable_1.pairs


def test_should_insert_none_values():
    hashtable = HashTable(capacity=100)
    hashtable["key"] = None
    assert ("key", None) in hashtable.pairs


def test_should_return_duplicate_values():
    hashtable = HashTable(capacity=100)
    hashtable["Alice"] = 24
    hashtable["Bob"] = 42
    hashtable["Jeo"] = 42
    assert [24, 42, 42] == sorted(hashtable.values)


def test_should_get_values(sample_hashtable_1):
    assert unordered(sample_hashtable_1.values) == ["hello", 37, True]


def test_should_get_values_of_empty_hashtable():
    assert HashTable(capacity=100).values == []


def test_should_return_copy_of_values(sample_hashtable_1):
    assert sample_hashtable_1.values is not sample_hashtable_1.values


def test_should_get_keys(sample_hashtable_1):
    assert sample_hashtable_1.keys == {"hola", 98.6, False}


def test_should_get_keys_of_empty_hashtable():
    assert HashTable(capacity=100).keys == set()


def test_should_return_copy_of_keys(sample_hashtable_1):
    assert sample_hashtable_1.keys is not sample_hashtable_1.keys


def test_should_return_pairs(sample_hashtable_1):
    assert sample_hashtable_1.pairs == {
        ("hola", "hello"),
        (98.6, 37),
        (False, True)
    }


def test_should_get_pairs_of_empty_hashtable():
    assert HashTable(capacity=100).pairs == set()


def test_should_convert_to_dict(sample_hashtable_1):
    dictionary = dict(sample_hashtable_1.pairs)
    assert set(dictionary.keys()) == sample_hashtable_1.keys
    assert set(dictionary.items()) == sample_hashtable_1.pairs
    assert list(dictionary.values()) == unordered(sample_hashtable_1.values)


def test_should_report_length_of_empty_hashtable():
    assert len(HashTable(capacity=100)) == 0


def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)


def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-123)


def test_should_report_length(sample_hashtable_1):
    assert len(sample_hashtable_1) == 3


def test_should_report_capacity_of_empty_hashtable():
    assert HashTable(capacity=100).capacity == 100


def test_should_report_capacity(sample_hashtable_1):
    assert sample_hashtable_1.capacity == 100


def test_should_iterate_over_keys(sample_hashtable_1):
    for key in sample_hashtable_1.keys:
        assert key in ("hola", 98.6, False)


def test_should_iterate_over_values(sample_hashtable_1):
    for value in sample_hashtable_1.values:
        assert value in ("hello", 37, True)


def test_should_iterate_over_pairs(sample_hashtable_1):
    for key, value in sample_hashtable_1.pairs:
        assert key in sample_hashtable_1.keys
        assert value in sample_hashtable_1.values


def test_should_iterate_over_instance(sample_hashtable_1):
    for key in sample_hashtable_1:
        assert key in ("hola", 98.6, False)


def test_should_use_dict_literal_for_str(sample_hashtable_1):
    assert str(sample_hashtable_1) in {
        "{'hola': 'hello', 98.6: 37, False: True}",
        "{'hola': 'hello', False: True, 98.6: 37}",
        "{98.6: 37, 'hola': 'hello', False: True}",
        "{98.6: 37, False: True, 'hola': 'hello'}",
        "{False: True, 'hola': 'hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'hola': 'hello'}",
    }

@pytest.fixture()
def dictionary():
    return {'hola': 'hello', 98.6: 37, False: True}

def test_should_create_hashtable_from_dict(dictionary):

    hashtable = HashTable.from_dict(dictionary)

    assert hashtable.capacity == len(dictionary) * 10
    assert hashtable.keys == set(dictionary.keys())
    assert hashtable.pairs == set(dictionary.items())
    assert unordered(hashtable.values) == list(dictionary.values())


def test_should_create_hashtable_from_dict_with_custom_capacity(dictionary):

    hashtable = HashTable.from_dict(dictionary, capacity=100)

    assert hashtable.capacity == 100
    assert hashtable.keys == set(dictionary.keys())
    assert hashtable.pairs == set(dictionary.items())
    assert unordered(hashtable.values) == list(dictionary.values())
