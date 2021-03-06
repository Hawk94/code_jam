"""Problem:

The urban legend goes that if you go to the Google homepage and search for "Google", 
the universe will implode. We have a secret to share... It is true! Please don't try 
it, or tell anyone. All right, maybe not. We are just kidding.

The same is not true for a universe far far away. In that universe, if you search on
any search engine for that search engine's name, the universe does implode!

To combat this, people came up with an interesting solution. All queries are pooled 
together. They are passed to a central system that decides which query goes to which 
search engine. The central system sends a series of queries to one search engine, and 
can switch to another at any time. Queries must be processed in the order they're received. 
The central system must never send a query to a search engine whose name matches the 
query. In order to reduce costs, the number of switches should be minimized.

Your task is to tell us how many times the central system will have to switch between
search engines, assuming that we program it optimally."""

from utils import read_input, write_output


def get_test(values):
    test_output = list()
    for i, j in enumerate(values):
        if i%3 == 0:
            test_output.append(get_engine(values, i, j))

    return 

def get_search_engines(values, i, j):
    search_engines = values[i+1:i+j]
    return search_engines

def get_searches(values, i, j):


def get_switches(values):
    test_case_index = [i for i in values if ]
    
    
