#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
import queue
from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        dict_meeting = defaultdict(set)

        for i in meetings:
            dict_meeting[i[2]].add((i[0], i[1]))

        priority_queue = queue.PriorityQueue()
        for priority, meetings in dict_meeting.items():
            priority_queue.put((priority, meetings))

        secret_shared = set({0, firstPerson})

        while not priority_queue.empty():
            priority, meetings = priority_queue.get()

            # print(f"secret_shared: {secret_shared}")
            # print(f"priority: {priority}, persons: {persons}")

            graph = defaultdict(set)
            people = set()
            for person in meetings:
                graph[person[0]].add(person[1])
                graph[person[1]].add(person[0])
                people.add(person[0])
                people.add(person[1])

            # find all the connected staring from firstPerson
            if not secret_shared.isdisjoint(people):
                people_intersected = secret_shared.intersection(people)
                pipe = list(people_intersected)
                visited = set()
                for person in people_intersected:
                    while pipe:
                        node = pipe.pop(0)
                        if node not in visited:
                            visited.add(node)
                            pipe.extend(graph[node] - visited)

                    secret_shared.update(visited)

        return secret_shared


# print(Solution().findAllPeople(6, [[0, 2, 1], [1, 3, 1], [4, 5, 1]], 1))

# print(Solution().findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))
# @lc code=end
