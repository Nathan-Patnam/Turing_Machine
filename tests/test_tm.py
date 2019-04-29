from tm import TM
import pytest
import sys
sys.path.append("..")  # Adds higher directory to python modules path.


class Testtm(object):
    @pytest.fixture(scope="function")
    def create_tm(self):
        tm = TM("tests/set_1/tm.txt")
        return tm

    def test_parse_line_for_tm_states(self, create_tm):
        states = set(["q1", "q2", "q3", "q4", "q5", "accept", "reject"])
        tm_states = create_tm.get_states()
        assert states == tm_states

    def test_parse_line_for_tm_input_alphabet(self, create_tm):
        alphabet = set("0")
        tm_alphabet = create_tm.get_input_alphabet()
        assert alphabet == tm_alphabet

    def test_parse_line_for_tm_tape_alphabet(self, create_tm):
        tape_alphabet = set(["0", "x", "_"])
        tm_tape_alphabet = create_tm.get_tape_alphabet()
        assert tape_alphabet == tm_tape_alphabet

    def test_parse_line_for_tm_start_state(self, create_tm):
        start_state = "q1"
        tm_start_state = create_tm.get_start_state()
        assert start_state == tm_start_state

    def test_parse_lines_for_tm_transitions(sxelf, create_tm):
        transitions = {

            ("q1", "0"): ("_", 'q2', "R"),
            ("q1", "_"): ("_", "reject", "R"),
            ("q1", "x"): ("x", 'reject', 'R'),
            ("q2", "x"): ('x', "q2", "R"),
            ("q2", "0"): ("x", "q3", "R"),
            ("q2", "_"): ("_", "accept", "R"),
            ("q3", "x"): ("x", 'q3', "R"),
            ("q3", "_"): ("_", "q5", "L"),
            ("q3", "0"): ("0", "q4", "R"),
            ("q4", "x"): ("x", "q4", "R"),
            ("q4", "0"): ("x", "q3", "R"),
            ("q4", "_"): ("_", "reject", "R"),
            ("q5", "0"): ("0", "q5", "L"),
            ("q5", "x"): ("x", "q5", 'L'),
            ("q5", "_"): ("_", 'q2', "R"),
        }

        tm_transitions = create_tm.get_transitions()
        assert transitions == tm_transitions
