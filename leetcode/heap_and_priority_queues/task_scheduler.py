from typing import List
from collections import Counter, deque
from heapq import heapify, heappop, heappush


def leastInterval(tasks: List[str], n: int) -> int:
    """
    - Time complexity: O(n.m.log(m))
        - m is the number of tasks
        - n is the cooling period
    - Space complexity: O(n)
    - Approach: Min heap
        - We can use a min heap to keep track of the remaining tasks
        - We can initialize the min heap with the frequency of each task
        - We use a queue to keep track of the tasks that are waiting to be
          executed - idle_queue
        - We iterate over the min heap and pop the root task of the heap
        - Time increases by 1 for each iteration
        - Subtract 1 from the frequency of the task and if the frequency is
          greater than 0, then we add the task to the idle queue
        - Check idle queue if there is any task that can be executed and if
          it's processing time is equal to the current time, then we add it
          to the min heap
    """
    task_count = Counter(tasks).values()
    task_heap = [-count for count in task_count]
    idle_queue = deque()
    time = 0

    heapify(task_heap)
    while task_heap or idle_queue:
        time += 1
        if task_heap:
            remaining_tasks = 1 + heappop(task_heap)
            if remaining_tasks:
                active_time = time + n
                idle_queue.append([remaining_tasks, active_time])
        if idle_queue and idle_queue[0][1] == time:
            heappush(task_heap, idle_queue.popleft()[0])
    return time
