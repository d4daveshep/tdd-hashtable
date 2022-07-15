import pytest

from entities.hashtable import HashTable


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    # Given
    hashtable = HashTable(capacity=3)
    expected_values = [None] * 3

    # When
    actual_values = hashtable.values

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
    assert sample_hashtable_1["hola"] == "hello"
    assert sample_hashtable_1[98.6] == 37
    assert sample_hashtable_1[False] == True

def test_should_raise_error_on_missing_key(sample_hashtable_1):
    with pytest.raises(KeyError) as exception_info:
        sample_hashtable_1["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_delete_key_value_pair(sample_hashtable_1):
    assert "hola" in sample_hashtable_1
    assert "hello" in sample_hashtable_1.values
    assert len(sample_hashtable_1) == 100

    del sample_hashtable_1["hola"]

    assert "hola" not in sample_hashtable_1
    assert "hello" not in sample_hashtable_1.values
    assert len(sample_hashtable_1) == 100

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