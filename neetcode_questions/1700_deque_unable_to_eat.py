from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        n = len(students)
        q = deque(students)
        res = n
        for i,sandwich in enumerate(sandwiches):
            cnt = 0
            while cnt < n and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            if q[0] == sandwich:
                res -= 1
                cur = q.popleft()
            else:
                break
        return q

sandwiches = [1,0,0,0,1,1]
students = [1,1,1,0,0,1]

s = Solution()
print(s.countStudents(students,sandwiches))
