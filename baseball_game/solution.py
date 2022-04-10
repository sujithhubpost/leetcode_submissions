'''
Solution to the baseball problem in leetcode
'''
class Solution:
    '''
    Main class : Solution to the baseball problem in leetcode
    '''
    def calPoints(self, ops: List[str]) -> int:
        '''
        Main function.
        Input : list of strings
        Output : Score
        '''
        final_list = []
        removed_val = 2
        for val in ops:
            if val == 'C':
                final_list.pop()
            elif val == 'D':
                final_list_val = int(final_list[-1]) * int(removed_val)
                final_list.append(int(final_list_val))
            elif val == '+':
                final_list.append(int(int(final_list[-1]) + int(final_list[-2])))
            else :
                final_list.append(int(val))
        return sum(final_list)
