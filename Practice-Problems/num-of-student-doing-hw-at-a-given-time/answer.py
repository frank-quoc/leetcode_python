class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        query_student = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                query_student += 1
        return query_student
