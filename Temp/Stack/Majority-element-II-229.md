---
title: Medium | Majority Element II 229
tags:
  - common
  - tricky
  - oh-no
  - corner case
categories:
  - Leetcode
  - Stack
date: 2020-06-22 16:27:13
---

Given an integer array of size *n*, find all elements that appear more than `⌊ n/3 ⌋` times.

**Note:** The algorithm should run in linear time and in O(1) space.

[Leetcode](https://leetcode.com/problems/majority-element-ii/)

<!--more-->

**Example 1:**

```
Input: [3,2,3]
Output: [3]
```

**Example 2:**

```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

**Follow up:** [Majority Element I](https://aranne.github.io/2020/01/10/169-Majority-element/)

---

#### Tricky 

This problem is an extension to [169. Majority Element](https://leetcode.com/problems/majority-element/), which needs Boyer-Moore Majority Vote Algorithm to find the element, whose count is over `n/2`.

When I was learning about Boyer-Moore, I was always thinking about **the pair**. I drew a picture to get myself understandable.

Suppose there are nine elements in array **A**, and the round one is the majority.

![0_1477537808895_upload-f2ddd14f-9954-4025-b77a-40137c5abf06](https://leetcode.com/uploads/files/1477537810177-upload-f2ddd14f-9954-4025-b77a-40137c5abf06.png)

No matter in what order we select element from the array, we can only get two results

![0_1477537956098_upload-e3d23d8b-0d43-4f8f-ace1-065bd0928493](https://leetcode.com/uploads/files/1477537957428-upload-e3d23d8b-0d43-4f8f-ace1-065bd0928493.png)

Compared to fully pairing, it is a little wasting of the partially pairing as there are some round ones are not paired (definitely it would be left). So, under the condition that the majority element exists, we could only think about **the fully pairing situation**. (It's useful when dealing with `n/3` situation)

We can consider either column as the candidate, and it's intuitive for me to get understand that the code means found a pair.

```
if candidate != element
  count -= 1
end
```

![0_1477539703014_upload-2186f2ff-dc3d-4324-a3ce-5f7ade11a2da](https://leetcode.com/uploads/files/1477539704324-upload-2186f2ff-dc3d-4324-a3ce-5f7ade11a2da.png)

So here comes the `n/3` problem, we would only think about the fully pairing situation. If the over one third majority exists, it should be left after pairing.

![0_1477539890642_upload-1c838025-3ff3-4fa9-ae23-abd8b7e10be9](https://leetcode.com/uploads/files/1477539893194-upload-1c838025-3ff3-4fa9-ae23-abd8b7e10be9.png)
Why would we use three elements as a pair? Because it makes sure that in fully pairing the count of majority element equals `n/3`.

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        int n = nums.length;
        int target = n / 3;
        int candidate1 = -1, candidate2 = -1;
        int cnt1 = 0, cnt2 = 0;
        for (int a : nums) {
            if (candidate1 == a) {
                cnt1++;
            } else if (candidate2 == a) {
                cnt2++;
            } else if (cnt1 == 0) {
                candidate1 = a;
                cnt1++;
            } else if (cnt2 == 0) {
                candidate2 = a;
                cnt2++;
            } else {     //find a pair of 3
                cnt1--;    
                cnt2--;
            }
        }
        cnt1 = 0;
        cnt2 = 0;
        for (int a : nums) {
            if (a == candidate1) {
                cnt1++;
            } else if (a == candidate2) {
                cnt2++;
            }
        }
        if (cnt1 > target) {
            res.add(candidate1);
        }
        if (cnt2 > target) {
            res.add(candidate2);
        }
        return res;
    }
}
```

T: O(n)			S: O(1)