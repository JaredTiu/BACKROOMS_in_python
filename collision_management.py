# collision_management.py

def check_collision(new_pos, walls):
    for wall in walls:
        (x1, y1), (x2, y2) = wall
        
        # Check if the new position is within the wall boundaries
        if (new_pos[0] >= min(x1, x2) and new_pos[0] <= max(x1, x2) and
            new_pos[1] >= min(y1, y2) and new_pos[1] <= max(y1, y2)):
            return True  # Collision detected
    return False  # No collision