'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["lint","code","love","you"]

Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]

Output: ["we", "say", ":", "yes"]

Explanation:

One possible encode method is: "we:;say:;:::;yes"
'''

# Solution #1 Does not account for the delimiting character being a part of a string, for example ["cats, "dogs", "ham:;sters"] would become ["cats, "dogs", "ham", "sters"]
class Solution:
    def encode(self, strs):
        return ":;".join(strs)

    def decode(self, str):
        return str.split(":;")
    
# Solution #2
class Solution:
    def encode(self, strs):
        # set an empty string to store the answer
        answer = ""
        # loop through the list of strings
        for string in strs:
            # for every string, find its length and put that at the front, followed by the delimiting character, then the string itself
            # so it will be like this: "cats" -> "4*cats"
            # add each of these to the overall answer string
            answer = str(len(string)) + "*" + string
        return answer
    
    def decode(self, str):
        # make empty list to hold answer
        answer = []
        # initialize slow pointer to 0
        i = 0
        # keep moving through the str until you run out to the end
        while i < len(str):
            # make fast pointer set to the value of i
            j = i
            # move through the master string until you get to a *, increasing the fast pointer
            while str[j] != "*":
                j += 1
            # find out what the length of the current string within the master string is
            length = str[i:j] # "4*cats4*dogs" -> "4" ("4*" not including *)
            # add the string to the answer list now that you know how long it is
            answer.append(str[j+1:j+1+length]) # "4*cats4*dogs" -> "cats" where j = 1 so str[2:6]
            # change value of i to the start of the next substring
            i = j+1+length # "4*cats4*dogs" -> i = 6 in the second pass
        return answer

        



# SAMPLE SOLUTION
class Codec:
    def encode(self, strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

