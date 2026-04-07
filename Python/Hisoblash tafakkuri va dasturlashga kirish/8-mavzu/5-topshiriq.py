def min_points_to_cover_intervals(intervals):
    if not intervals:
        return []

    # 1. Kesmalarni tugash vaqti (o'ng chegarasi) bo'yicha saralaymiz
    # x[1] - bu kesmaning o'ng uchi
    intervals.sort(key=lambda x: x[1])

    points = []
    # Birinchi nuqtani birinchi kesmaning oxiriga qo'yamiz
    last_point = intervals[0][1]
    points.append(last_point)

    for i in range(1, len(intervals)):
        start, end = intervals[i]
        
        # Agar joriy kesma oxirgi tanlangan nuqtani o'z ichiga olmasa
        if start > last_point:
            # Yangi nuqta qo'yamiz (bu kesmaning oxiriga)
            last_point = end
            points.append(last_point)
            
    return points

# Sinov uchun:
# Kesmalar: [1, 3], [2, 5], [3, 6], [6, 7], [8, 10]
test_intervals = [[1, 3], [2, 5], [3, 6], [6, 7], [8, 10]]
result_points = min_points_to_cover_intervals(test_intervals)

print(f"Berilgan kesmalar: {test_intervals}")
print(f"Minimal nuqtalar to'plami: {result_points}")
print(f"Nuqtalar soni: {len(result_points)}")