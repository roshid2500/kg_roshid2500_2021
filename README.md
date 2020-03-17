# kg_roshid2500_2021

Algorithm to determine whether a one-to-one mapping exists between two strings given as commandline arguments. 

**Assumptions Made:**
1) The length of the two string arguments must be the same
  Ex. "foo"   "am"
  returns False 
  
2) If length requirements met, ONLY reject if a character in string one has more than character mapping 
  Ex. "foo"   "bar" 
  f -> b 
  o -> a 
  o -> r 
  returns False 
