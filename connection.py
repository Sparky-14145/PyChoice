"""
connection.py
Connect to a database and return samples at random.

First Edition:
Just read strings from a txt file, default file is "assets/data.txt".
"""

import random, str_def

with open(str_def.get_setting("database"), "r") as file:
    index = [i for i in file]

def connect(address):
    '''
    address: str
    Close all present connections and connect to the given database. The change will be saved as the
    cfg.txt changes. 
    '''
    global index
    str_def.set_setting("database", address)
    with open(address, "r") as file:
        index = [i for i in file]

def sample(num = 1):
    if num < 0 or num > len(index):
        raise IndexError(str_def.get_lang("no_enough_students"))
    else:
        return random.sample(index, num)

def main():
    print(index)
    while True:
        try:
            n = int(input())
            smp = sample(n)
            print(smp)
        except IndexError as e:
            print(e.args[0])
        except EOFError:
            break
        else:
            pass

if __name__ == "__main__":
    main()