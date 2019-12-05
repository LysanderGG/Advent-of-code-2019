import opcode
from dataclasses import dataclass
from typing import Callable, List


def read_input(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.readline().split(",")]


class Program:
    instruction_nb_params = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        99: 0
    }

    def __init__(self, program: List[int], input_: int):
        self.input = input_
        self.program = list(program)
        self.pc = 0
        self.modes: List[bool] = []

    def next_operands(self):
        s = str(self.program[self.pc]).rjust(5, '0')
        op, m1, m2, m3 = int(s[-2:]), s[2] == '0', s[1] == '0', s[0] == '0'

        self.modes = [m1, m2, m3]
        return op

    def get_param(self, i, force_immediate_mode: bool = False):
        if force_immediate_mode:
            return self.program[self.pc+i]

        return self.program[self.program[self.pc+i]] if self.modes[i-1] else self.program[self.pc+i]

    def solve(self):
        while (op := self.next_operands()) != 99:
            if op == 1:
                self.program[self.get_param(3, True)] = self.get_param(1) + self.get_param(2)
            elif op == 2:
                self.program[self.get_param(3, True)] = self.get_param(1) * self.get_param(2)
            elif op == 3:
                self.program[self.get_param(1, True)] = self.input
            elif op == 4:
                print(self.get_param(1))
            elif op == 5:
                if self.get_param(1):
                    self.pc = self.get_param(2)-3
            elif op == 6:
                if not self.get_param(1):
                    self.pc = self.get_param(2)-3
            elif op == 7:
                self.program[self.get_param(3, True)] = 1 if self.get_param(1) < self.get_param(2) else 0
            elif op == 8:
                self.program[self.get_param(3, True)] = 1 if self.get_param(1) == self.get_param(2) else 0
            else:
                raise ValueError(f"Unknown instruction {op=}")

            self.pc += self.instruction_nb_params[op] + 1

        return 0


if __name__ == "__main__":
    program = read_input('day05.txt')
    print(f"Part1: {Program(program, 1).solve()}")
    print(f"Part2: {Program(program, 5).solve()}")
