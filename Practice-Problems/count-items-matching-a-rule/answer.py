class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_dict = {"type": 0, "color": 1, "name": 2}
        rule_idx = rule_dict[ruleKey]
        return sum([items[i][rule_idx] == ruleValue for i in range(len(items))])
