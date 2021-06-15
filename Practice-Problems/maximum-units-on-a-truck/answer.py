class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        tot_units = 0
        for box, unit in boxTypes:
            boxes = min(box, truckSize)
            tot_units += boxes * unit
            truckSize -= boxes
            if truckSize == 0:
                break
        return tot_units
