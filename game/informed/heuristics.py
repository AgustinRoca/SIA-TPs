from game.game import GameState
from itertools import permutations


def _distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def heuristic_min_distance_boxes(state: GameState) -> int:
    min_distance = None
    boxes = list(state.boxes)
    perms = list(permutations(state.goals))
    for j in range(0, len(perms)):
        total_distance = 0
        for i in range(0, len(boxes)):
            total_distance += _distance(boxes[i], perms[j][i])
        if min_distance is None or total_distance < min_distance:
            min_distance = total_distance
    return min_distance + _player_min_distance_from_a_box(state)


def _player_min_distance_from_a_box(state: GameState) -> int:
    min_distance = None
    for box in list(state.boxes):
        distance = _distance(box, state.player)
        if (box[0] - state.player[0] != 0) and (box[1] - state.player[1] != 0):
            distance += 2
        if min_distance is None or distance < min_distance:
            min_distance = distance
    return min_distance - 1


def heuristic_distance_to_closest_goals(state: GameState) -> int:
    dist = 0
    for box in state.boxes:
        if box not in state.goals:
            dist += _distance_to_closest_free_goal(box, state)
    return dist


def _distance_to_closest_free_goal(box, state):
    min_distance = None
    for goal in state.goals:
        if goal not in state.boxes:
            distance = _distance(box, goal)
            if (min_distance is None) or (distance < min_distance):
                min_distance = distance
    return min_distance
