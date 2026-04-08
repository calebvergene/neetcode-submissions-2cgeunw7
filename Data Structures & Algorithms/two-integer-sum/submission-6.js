class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let dict = {}
        for (let i in nums){
            if (nums[i] in dict){
                return [dict[nums[i]], i].map(num => Number(num))
            }
            dict[target-nums[i]] = i
        }
    }
}
