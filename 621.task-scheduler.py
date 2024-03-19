#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
from collections import Counter
# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Step 2: Sort tasks based on their frequencies
        sorted_tasks = sorted(task_counts.values(), reverse=True)
        
        # Step 3: Schedule tasks
        max_freq = sorted_tasks[0] - 1
        idle_slots = max_freq * n
        
        for freq in sorted_tasks[1:]:
            idle_slots -= min(freq, max_freq)
        
        idle_slots = max(0, idle_slots)
        
        # Step 4: Calculate minimum intervals required
        return len(tasks) + idle_slots
        
# @lc code=end

