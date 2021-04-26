class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d_paths = dict(paths)
        for i in d_paths.values():
            if i not in d_paths.keys():
                return i
