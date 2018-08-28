# coding:utf-8

class Finder(object):
    '''
        判断两个相邻的数字是否连续，若连续：
            1.继续向后判断
            2.记录连续长度
        最后返回最大连续长度
    '''
    def find_continuity(self,index,array,length=1):
        if index+1 < len(array):
            _curr = array[index]
            _next = array[index+1]
            if abs(_next-_curr) == 1:
                length += 1
                length = self.find_continuity(index+1,array,length)
        return length

        '''
        将每个数字开头的索引值及最大连续区间长度存入字典
        找出字典中最大的键值即最大连续区间
        根据最大连续区间的索引和长度返回对应的数组切片
        '''
    def find_longest(self,array):
        continuity = dict()
        for i in range(len(array)):
            length = self.find_continuity(i,array)
            continuity[i] = length
        longest = max(continuity.items(), key=lambda x: x[1])
        index,length = longest[0],longest[1]
        return array[index:index+length]

if __name__ == '__main__':
    array = [1,9,8,-5,7,0,-1,6,-7,16,-3,1]
    finder = Finder()
    longest_array = finder.find_longest(array)
    print(longest_array)