import pytest
from session_info import process_log_file

def test_session_info_success():
    """
    Test case to verify the correctness of the process_log_file function.

    This test case reads a sample log file and checks if the process_log_file function
    produces the expected output for the first entry in the result. It asserts that the
    username, number of sessions, and total duration match the expected values.
    """

    # Call the process_log_file function with the sample log file
    result = process_log_file("./samplelog1.txt")

    # Extract username, number of sessions, and total duration from the first entry of the result
    username, number_of_sessions, total_duration = result[0]

    # Assert that the extracted username matches the expected value
    assert username == "ALICE99"
    # Assert that the extracted number of sessions matches the expected value
    assert number_of_sessions == 4
    # Assert that the extracted total duration matches the expected value
    assert total_duration == 240


def test_session_info_raises_an_exception_if_given_file_invalid():
    """
    Test case to verify that process_log_file function raises an exception when given an invalid log file.

    This test checks whether the process_log_file function raises an exception when provided with
    the path to an invalid log file. An invalid log file is one that does not contain the expected
    session details format. The test passes if the process_log_file function raises an Exception,
    indicating that it correctly handles invalid input.

    Raises:
        AssertionError: If process_log_file does not raise an Exception with an invalid log file.
    """
    with pytest.raises(Exception):
        process_log_file("./samplelog2.txt")
