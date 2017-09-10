# Topological Sort

### Problem define:###

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

#### example:####

Given n = `2`, prerequisites = `[[1,0]]`
Return [0,1]

Given n = `2`, prerequisites = `[[1,0],[0,1]]`
Return []

## Documents

1. *topological-sort1.py* contains a solution which has not been optimized.
2. *topological-sort2.py* contains a solution which has been optimized by using two dictionaries as graphs.