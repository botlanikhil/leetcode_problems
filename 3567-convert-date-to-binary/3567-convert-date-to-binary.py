class Solution(object):
    def convertDateToBinary(self, date):
        arr = date.split('-')                       
        arr = map(lambda x: bin(int(x))[2:], arr)   
        return "-".join(arr)
        