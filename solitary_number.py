
def solo_number(self, nums):
    i=0
    try:
        while i<len(nums):
            j=nums[i]
            nums.remove(j)
            if nums.count(j)>0:
                nums.remove(j)
            else:
                return j
                print('Second:', nums)
        i+=1
    except IndexError: quit
    return j
