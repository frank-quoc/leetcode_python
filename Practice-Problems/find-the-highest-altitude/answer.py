class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(len(gain)):
            net_gain = altitudes[i] + gain[i]
            altitudes.append(net_gain)
        return max(altitudes)
