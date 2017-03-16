"""
Problem Domain CMD
"""
import sys
from cmd import Cmd

from ReadingData import Validator
val = Validator()

# FIX THIS PLEASE
# def arg():
#     try:
#         if sys.argv[1] == "happy":
#             with open("table.txt", 'r') as file:
#                 data = file.read()
#                 line = data.split()
#                 dic = dict(e.split('=') for e in line)
#                 # print(dic)
#             val.valid(dic)
#             print(val.valid(dic))
#             return val.database()
#     except Exception as err:
#         pass

class DomainCmd(Cmd):
    def __init__(self, con):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.filename = None
        self.my_name = "unknown"
        self.intro = "Welcome to the Problem Domain"
        self.con = con

    # def set_controller(self, con):
    #     self.con = con

    def do_read(self, filename):
        self.con.read_file(filename)

    def do_validate(self, line):
        self.con.validate()

    def do_table(self, line):
        self.con.database()

    # Quit the cmd
    def do_quit(self, line):
        self.con.database_close()
        print("Closing cmd..")
        return True

    # shortcut
    do_q = do_quit

# if __name__ == '__main__':
#     arg = arg()
#     print(arg)
    # domain = DomainCmd()
    # domain.cmdloop()
