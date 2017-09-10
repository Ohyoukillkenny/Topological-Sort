class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        sorted_List = []
        noincoming_List = []
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for pairs in prerequisites:
            if pairs[1] not in graph[pairs[0]]:
                graph[pairs[0]].append(pairs[1])

        for key, items in graph.iteritems():
            if len(items) == 0:
                noincoming_List.append(key)

        while len(noincoming_List) > 0:
            n = noincoming_List.pop()
            sorted_List.append(n)
            for key, items in graph.iteritems():
                if n in items:
                    items.remove(n)
                    if len(items) == 0:
                        noincoming_List.append(key)

        flag = True
        for key, items in graph.iteritems():
            if items:
                flag = False
        if flag:
            return sorted_List
        else:
            return []