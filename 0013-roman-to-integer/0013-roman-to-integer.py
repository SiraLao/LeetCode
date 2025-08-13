class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
        total_num = 0
        pre_value = 0

        for i in reversed(s):
            current_value = roman_values[i]
            if current_value < pre_value:
                total_num=total_num-current_value
            else: 
                total_num=total_num+current_value
            pre_value = current_value
        return total_num