class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        order_map = {val: i for i, val in enumerate(order)}

        sorted_s = sorted(s, key=lambda x: order_map.get(x, float('inf')))

        return ''.join(sorted_s)