class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            digits[index] += 1
            if digits[index] != 10:
                return digits
            digits[index] = 0
        return [1] + digits
