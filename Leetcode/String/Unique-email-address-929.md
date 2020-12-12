---
title: Easy | Unique Email Address 929
tags:
  - common
categories:
  - Leetcode
  - String
date: 2020-06-27 01:17:59
---

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in `alice@leetcode.com`, `alice` is the local name, and `leetcode.com` is the domain name.

Given a list of `emails`, we send one email to each address in the list.  How many different addresses actually receive mails? 

[Leetcode](https://leetcode.com/problems/unique-email-addresses/)

<!--more-->

Besides lowercase letters, these emails may contain `'.'`s or `'+'`s.

If you add periods (`'.'`) between some characters in the **local name** part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, `"alice.z@leetcode.com"` and `"alicez@leetcode.com"` forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus (`'+'`) in the **local name**, everything after the first plus sign will be **ignored**. This allows certain emails to be filtered, for example `m.y+name@email.com` will be forwarded to `my@email.com`.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

---

#### First solution

```java
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for (String email : emails) {
            String[] names = email.split("@");
            String[] local = names[0].split("\\+");
            set.add(local[0].replace(".", "") + "@" + names[1]);
        }
        return set.size();
    }
}
```

T: O(n * len)		S: O(n)

---

#### Optimized

```java
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for (String email : emails) {
            String[] names = email.split("@");
            StringBuilder sb = new StringBuilder();
            for (char c : names[0].toCharArray()) {
                if (c == '.') continue;
                if (c == '+') break;
                sb.append(c);
            }
            sb.append("@").append(names[1]);
            set.add(sb.toString());
        }
        return set.size();
    }
}
```

T: O(n * len) 		S: O(n)