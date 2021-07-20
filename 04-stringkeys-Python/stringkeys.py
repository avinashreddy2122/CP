"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        #Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        a=self.calculate_hash_value(string)
        self.table[a] = string
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        a = self.calculate_hash_value(string)
        if self.table[a] == string:
            # print(a)
            return a
        else:
        
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        hashvalue = ord(string[0]) * 100  + ord(string[1])
        # print (hashvalue)
        return hashvalue
    
hash_table= HashTable()
print(hash_table.calculate_hash_value('UDACIOUS'))
print(hash_table.lookup('UDACITY'))