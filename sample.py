# sample.py
import random

def read_data():
    # Read data from a file or database...
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sample = read_data()

def mean(data):
    try: 
        print(sum(data) / len(data))
    except Exception as e:
        print(e)

def random_number():
    print(random.random())