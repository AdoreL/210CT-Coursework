s = "beautiful"
def REM(s):
    """Recursively remove vowels from the input."""
    v = "aeiou"
    if not s: #if it returns none
        return s #the string is empty therefor it has zero vowels.
    if s[0] in v: # first character is vowel
        return REM(s[1:]) # skip first character and process rest
    return s[0] + REM(s[1:]) # return first character and process rest

print(REM(s))
