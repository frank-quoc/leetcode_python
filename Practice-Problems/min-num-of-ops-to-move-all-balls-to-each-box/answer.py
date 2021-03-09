class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes_lst = list(boxes)
        steps = []
        for i in range(len(boxes)):
            steps.append(sum([abs(i-j) for j in range(len(boxes_lst)) if boxes_lst[j] == '1']))
        return steps
