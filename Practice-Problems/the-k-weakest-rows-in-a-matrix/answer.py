        soldier_rows = {}
        for i in range(len(mat)):
            soldier_rows[i] = mat[i].count(1)
        strength = {k: v for k, v in sorted(soldier_rows.items(), key=lambda item: item[1])}
        return list(strength.keys())[:k]
