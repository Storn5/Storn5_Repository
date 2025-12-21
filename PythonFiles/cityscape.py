def insertFloor(floors, point):
	if len(floors) == 0:
		return [point,]
	for (i, floor_point) in enumerate(floors):
		if point < floor_point:
			return floors[:i] + [point,] + floors[i:]

def getSkyline(buildings):
	building_corner_pairs = map(lambda b: ((b[0], b[2]), (b[1], b[2])), buildings)
	building_corners = [point for pair in building_corner_pairs for point in pair]
	building_corners.sort(key=lambda b: b[0])
	points = [building_corners.pop(0)]
	floors = [0]

	for corner in building_corners:
		if corner[1] == points[-1][1]:
			points.append((corner[0], floors[-1]))
			while floors[-1] == points[-1][1] and floors[-1] > 0:
				floors.pop()
		elif corner[1] > points[-1][1]:
			insertFloor(floors, points[-1][1])
			points.append(corner)
		else:
			insertFloor(floors, points[-1][1])

	return points

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(getSkyline(buildings))
