import pytest
import sys
sys.path.append("..")  # Adds higher directory to python modules path.
from tm import TM

def test_create_tm_from_file():

    x = 3
    assert x == 4

#import pytest

"""
@pytest.fixture(scope="module")
def create_dpda():
    d_pushdown_automota = DPDA("dpda.txt")
    return d_pushdown_automota
"""
"""

class TestTM(object):
    @pytest.fixture(autouse=True)
    def test_remove_whitespace_and_newline(self, create_dpda):
        whitespaced__newline_word = "q4\n "
        formatted_word = "q4"
        whitespaced__newline_word = create_dpda.remove_whitespace_and_newline(
            whitespaced__newline_word)
        assert whitespaced__newline_word == formatted_word

    def test_parsing_file_for_states(self, create_dpda):
        expected_states = set(["q1", "q2", "q3", "q4"])
        states = create_dpda.get_states()
        assert expected_states == states

   """

