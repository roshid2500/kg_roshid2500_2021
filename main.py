import sys

#Input arguments are global constants in this case
#Must check whether arguments are given
INPUT1 = sys.argv[1] if(len(sys.argv) == 3) else "";
INPUT2 = sys.argv[2] if(len(sys.argv) == 3) else "";


'''
Determines whether string x has a one-to-one mapping with
string y
O(n) time where n = len(x)
O(n) space due to dictionary
'''
def hasMapping(x, y):
    #base case: if string(s) do not exits, no mapping exists
    #if string sizes are not equal, then 1-1 mapping cannot be made
    if((len(x) != len(y)) or (len(x) == 0) or (len(y) == 0)):
        return False;

    #initialize dictionary
    mappings = {};

    #iterate through x; if entry is not present, add it in;
    #else its entry is in the dictionary and not equal
    #to the coresponding char in y, then return false;
    for i in range(len(x)):
        if(x[i] not in mappings):
            mappings[x[i]] = y[i]
        if(mappings[x[i]] != y[i]):
            return False;

    return True;



def main():
    #call to funct
    print(hasMapping(INPUT1, INPUT2))
main()
