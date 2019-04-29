from tm import TM
import pytest
import sys
sys.path.append("..")  # Adds higher directory to python modules path.





class Testtm(object):
    @pytest.fixture(scope="function")
    def create_tm(self):
        tm = TM("set_1/tm.txt")
        return tm


    def test_parse_line_for_tm_states(self, create_tm):
        states = set(["q1", "q2", "q3", "q4" ,"q5","accept","reject"])
        tm_states = create_tm.get_states()
        assert create_tm.states == tm_states

   
   
