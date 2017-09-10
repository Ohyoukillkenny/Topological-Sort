class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        sorted_List = []
        noincoming_List = []
        graph1 = {}
        graph2 = {}

        for i in range(numCourses):
            graph1[i] = []
            graph2[i] = []
        for pairs in prerequisites:
            if pairs[1] not in graph1[pairs[0]]:
                graph1[pairs[0]].append(pairs[1])
                graph2[pairs[1]].append(pairs[0])

        for key, items in graph1.iteritems():
            if len(items) == 0:
                noincoming_List.append(key)

        while len(noincoming_List) > 0:
            n = noincoming_List.pop()
            sorted_List.append(n)
            mlist = graph2[n]
            graph2[n] = []
            for m in mlist:
                graph1[m].remove(n)
                if len(graph1[m]) == 0:
                    noincoming_List.append(m)

        flag = True
        for key, items in graph1.iteritems():
            if items:
                flag = False
        if flag:
            return sorted_List
        else:
            return []