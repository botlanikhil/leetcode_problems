class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for i in strs:
            sortedstring=''.join(sorted(i))
            if sortedstring in d:
                d[sortedstring].append(i)
            else:
                d[sortedstring]=[i]
        return list(d.values())




        