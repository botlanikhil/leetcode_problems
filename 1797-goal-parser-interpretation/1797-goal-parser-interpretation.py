class Solution(object):
    def interpret(self, command):
        d = {'G': 'G', '()': 'o', '(al)': 'al'}
        s = ''
        i = 0

        while i < len(command):
            if command[i:i+4] == "(al)":  # Match "(al)"
                s += d["(al)"]
                i += 4
            elif command[i:i+2] == "()":  # Match "()"
                s += d["()"]
                i += 2
            else:  # Match "G"
                s += d["G"]
                i += 1

        return s