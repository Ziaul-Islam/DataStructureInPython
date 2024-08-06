class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        global_count = 0
        local_count = 0
        i = 0
        while i < len(s):
            element = s[i]
            if element in dic.keys():
                i = dic[element] + 1
                element = s[i]
                dic = {}
                dic[element] = i
                local_count = 1
            else:
                dic[element] = i
                local_count += 1
            i += 1
            global_count = local_count if local_count > global_count else global_count
        return global_count
        