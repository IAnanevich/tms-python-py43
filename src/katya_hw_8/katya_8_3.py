class RealString:
    def __init__(self, first_str, second_str):
        self.first_str = first_str
        self.second_str = second_str

    def main(self):
        if len(self.first_str) == len(self.second_str):
            print(f'{self.first_str} == {self.second_str}')
        elif len(self.first_str) > len(self.second_str):
            print(f'{self.first_str} > {self.second_str}')
        else:
            print(f'{self.first_str} < {self.second_str}')

specified_lines = RealString('jhuygf ghhj', 'hgygygh')
specified_lines.main()
