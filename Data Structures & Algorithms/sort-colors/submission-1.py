class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # iter through. 0 = move to front, 2 = move to back, 1 = dont move
        # problem is: adding 2 to the back might cause an infinite loop right?
        # so, track the id() of the first 2 you find. when you come accross it again, 
        # then you know that you are done sorting.

        # also, you need to swap for o(n) time. so, track where to swap 0 and 2 and keep 1
        zero, two = 0, len(nums)-1
        i = 0
        # while i <= two because you know you already sorted everything after two
        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                # now swap the next zero in the next front slot
                zero += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
                # if you swap a two to the end, need to sort the new element at i
                continue
            i += 1

