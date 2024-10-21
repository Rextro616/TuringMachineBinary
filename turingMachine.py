class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)
        self.position = 0
        self.initialState = 'q0' 
        self.state = self.initialState
        self.finalState = 'q4'
        self.accepted = False

    def run(self):
        while self.state != self.finalState:
            if self.state == 'q0':
                self.stateQ0()
            elif self.state == 'q1':
                self.stateQ1()
            elif self.state == 'q2':
                self.stateQ2()
            elif self.state == 'q3':
                self.stateQ3()
    
    def stateQ0(self):
        if self.tape[self.position] == '0':
            self.tape[self.position] = 'X'
            self.position += 1
            self.state = 'q1'
        elif self.tape[self.position] == 'Y':
            if self.position != len(self.tape) - 1:
                self.position += 1
            self.state = 'q3'
        else:
            self.state = 'q4'
            self.accepted = False
            
            
    def stateQ1(self):
        if (self.tape[self.position] == '0' or self.tape[self.position] == 'Y') and self.position != len(self.tape) - 1:
            self.position += 1
        elif self.tape[self.position] == '1':
            self.tape[self.position] = 'Y'
            self.position -= 1
            self.state = 'q2'
        else:
            self.state = 'q4'
            self.accepted = False
            
    def stateQ2(self):
        if (self.tape[self.position] == '0' or self.tape[self.position] == 'Y') and self.position > 0:
            self.position -= 1
        elif self.tape[self.position] == 'X':
            self.position += 1
            self.state = self.initialState
        else:
            self.state = 'q4'
            self.accepted = False
            
    def stateQ3(self):
        if self.position == len(self.tape) - 1 and self.tape[self.position] == 'Y':
            self.state = 'q4'
            self.accepted = True
        elif self.tape[self.position] == 'Y':
            self.position += 1
        else:
            self.state = 'q4'
            self.accepted = False     
            
    def stateQ4(self):
        if self.accepted:
            return ''.join(self.tape)
        else:
            return 'La cinta no es aceptada por la maquina de Turing.'
        
    def start(self):
        self.run()
        return self.stateQ4()