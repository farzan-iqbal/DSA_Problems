class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge_map = {}  # Stores next greater for each element in nums2

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                nge_map[prev] = num
            stack.append(num)

        # Remaining elements in stack have no next greater
        while stack:
            nge_map[stack.pop()] = -1

        # Now build result for nums1 from map
        return [nge_map[num] for num in nums1]
