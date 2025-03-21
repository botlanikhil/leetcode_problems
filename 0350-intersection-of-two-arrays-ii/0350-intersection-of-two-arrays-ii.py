class Solution(object):
    def intersect(self, nums1, nums2):
        l=[]
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            for i in nums2[:]:  # Iterate over a copy to avoid modification issues
                if i in nums1:
                    l.append(i)
                    nums1.remove(i)  # Remove only one occurrence
        else:
            for i in nums1[:]:
                if i in nums2:
                    l.append(i)
                    nums2.remove(i)  # Remove only one occurrence

        return l