class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n = len(piles)
        max_pile = max(piles)
        hi = ceil(max_pile / (h / n))
        
        lo = max(1, ceil(sum(piles)/h)) 
        while lo <= hi:
            curr_guess = (lo + hi) // 2
            hours_passed = sum(ceil(pile / curr_guess) for pile in piles)
            
            if hours_passed > h:
                lo = curr_guess + 1
            else:
                hi = curr_guess - 1
                
        return int(lo)
        