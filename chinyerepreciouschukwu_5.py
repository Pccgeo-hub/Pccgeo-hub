s = "Strings are awesome!"
print("Length of s = %d" % len(s)) # Length should be 20
 # First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a")) # Number of a's should be 2
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("String in uppercase: %s" % s.upper()) # Convert everything to uppercase
print("String in lowercase: %s" % s.lower()) # Convert everything to lowercase
if s.startswith("Str"):# Check how a string starts
    print("String starts with 'Str'. Good!")
if s.endswith("ome!"):# Check how a string ends
    print("String ends with 'ome!'. Good!")
# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
