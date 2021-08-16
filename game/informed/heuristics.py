from game.game import GameState


# TODO: Check admissibility
def heuristic_completed_boxes(state: GameState) -> int:
    boxes_left = len(state.boxes)
    for goal in state.goals:
        for box in state.boxes:
            if goal == box:
                boxes_left -= 1
    return boxes_left
