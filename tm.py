class TM:
    def __init__(self, filename):
        self.filename = filename
        self.states = set()
        self.input_alphabet = set()
        self.tape_alphabet = set()
        self.start_state = ""
        self.transitions = {}
        self.build_TM(filename)
        
    

    def build_TM(self, filename):
        tm_fh = open(filename, "r")
        lines = tm_fh.readlines()
        line_number = 1
        for line in lines:
            if line_number == 1:
                self.set_tm_states(line)
            elif line_number == 2:
                self.set_tm_input_alphabet(line)
            elif line_number == 3:
                self.set_tm_tape_alphabet(line)
            elif line_number == 4:
                self.set_tm_start_state(line)
            else:
                self.add_transition(line)
            line_number += 1
    

    def set_tm_states(self, line):
        self.states = self.convert_comma_seperated_string_to_set(line)

    
    def set_tm_input_alphabet(self, line):
        self.input_alphabet = self.convert_comma_seperated_string_to_set(line)
    
    def set_tm_tape_alphabet(self, line):
        self.tape_alphabet = self.convert_comma_seperated_string_to_set(line)
    
    def set_tm_start_state(self, line):
        line = self.remove_whitespace_and_newline(line)
        self.start_state = line
    
    def add_transition(self, line):
        line = self.remove_whitespace_and_newline(line)
        items = line.split(",")
        start_state = items[0]
        read_character = items[1]
        write_character = items[2]
        end_state = items[3]
        direction_change = items[4]

        self.transitions[(start_state, read_character)] = (write_character, end_state, direction_change)


    def convert_comma_seperated_string_to_set(self, line):
        data_container = set()
        line = self.remove_whitespace_and_newline(line)
        items = line.split(",")
        for item in items:
            data_container.add(item)
        return data_container

    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")


    def get_states(self):
        return self.states
    
    def get_input_alphabet(self):
        return self.input_alphabet
    
    def get_tape_alphabet(self):
        return self.tape_alphabet
    
    def get_start_state(self):
        return self.start_state
    
    def get_transitions(self):
        return self.transitions
    
    


