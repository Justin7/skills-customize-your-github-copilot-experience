# 📘 Assignment: List Search Tool

## 🎯 Objective

Practice searching Python lists with loops by finding the position of a value and counting how many times it appears.

## 📝 Tasks

### 🛠️	Find the First Match

#### Description
Write a function called `linear_search(numbers, target)` that checks each item in a list until it finds the target.

#### Requirements
Completed program should:

- Return the zero-based index of the first matching value.
- Return `-1` if the target is not in the list.
- Search through the list with a loop instead of using `list.index()`.
- Work with an empty list.
- Example: `linear_search([4, 7, 2, 7], 7)` returns `1` and `linear_search([4, 7, 2, 7], 5)` returns `-1`.

### 🛠️	Count Matching Values

#### Description
Write a function called `count_matches(numbers, target)` that searches the entire list and counts every item equal to the target.

#### Requirements
Completed program should:

- Return the number of times the target appears in the list.
- Use a loop to check each item instead of using `list.count()`.
- Return `0` when the target does not appear or the list is empty.
- Example: `count_matches([4, 7, 2, 7], 7)` returns `2` and `count_matches([4, 7, 2, 7], 5)` returns `0`.