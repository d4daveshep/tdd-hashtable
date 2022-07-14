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




