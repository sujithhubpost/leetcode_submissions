'''
Q : Given a roman numeral, convert it to an integer.
'''
class Solution:
    '''
    Main class for the solution
    '''
    def romanToInt(self, s: str) -> int:
        '''
        Ex.
        **Input:** s = "MCMXCIV"
        **Output:** 1994
        **Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.
        '''
        conversion_table = {
                                "0" : 10000,
                                "I" : 1,
                                "V" : 5,
                                "X" : 10,
                                "L" : 50,
                                "C" : 100,
                                "D" : 500,
                                "M" : 1000,
                            }
        res = 0
        leng = len(s)
        prev = 0
        curr = 0
        for c in s[::-1]:
            curr = conversion_table[c]
            if prev > curr :
                res -= curr
            else :
                res += curr
            prev = conversion_table[c]
        # print(conc, conc_x)
        return res