/**
 * Leetcode: 53. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
 * 
 * Approach: Kadane's algorithm
 *
 * Analysis: Time - O(n) | Space - O(1) - where n is the length of the input array
 *
 * @param nums - array of numbers
 * @returns maximum sum of a contiguous subarray
 */
function maxSubArray(nums: number[]): number {
    let maxSum: number = Number.NEGATIVE_INFINITY;
    let currSum: number = 0;
    nums.forEach((num) => {
        currSum = Math.max(num, currSum + num);
        maxSum = Math.max(currSum, maxSum);
    });
    return maxSum;
};
