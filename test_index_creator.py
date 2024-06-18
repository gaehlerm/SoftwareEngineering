from index_creator import *


def test_process_page_numbers_no_subsequent_numbers():
    page_numbers = [1, 6]
    number_range = create_number_range(page_numbers)
    assert process_page_numbers(number_range) == "1, 6"

def test_process_page_numbers_with_subsequent_numbers():
    page_numbers = [1, 2, 6]
    number_range = create_number_range(page_numbers)
    assert process_page_numbers(number_range) == "1-2, 6"

def test_process_page_numbers_many_subsequent_numbers():
    page_numbers = [1, 2, 3, 4]
    number_range = create_number_range(page_numbers)
    assert process_page_numbers(number_range) == "1-4"

def test_process_page_numbers_many_subsequent_numbers_and_a_big_one():
    page_numbers = [1, 2, 3, 4, 10]
    number_range = create_number_range(page_numbers)
    assert process_page_numbers(number_range) == "1-4, 10"