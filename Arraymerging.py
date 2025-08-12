#array Merging in python
def merge(intervals):
    intervals.sort()
    merged = []
    for s, e in intervals:
        if not merged or merged[-1][1] < s:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged
#example
print(merge([[1,3],[2,6],[8,10],[15,18]]))