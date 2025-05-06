def minimax(cat, mouse, cheese, depth, is_cat_turn):
    if depth == 0 or cat == mouse or mouse == cheese:
        return evaluate(cat, mouse, cheese), None

    best_move = None

    if is_cat_turn:
        max_eval = -float('inf')
        for dx, dy in MOVES + [(-1,-1), (-1,1), (1,-1), (1,1)]:
            new_cat = (cat[0] + dx, cat[1] + dy)
            if is_valid(new_cat):
                eval, _ = minimax(new_cat, mouse, cheese, depth - 1, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = new_cat
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for dx, dy in MOVES:
            new_mouse = (mouse[0] + dx, mouse[1] + dy)
            if is_valid(new_mouse):
                eval, _ = minimax(cat, new_mouse, cheese, depth - 1, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = new_mouse
        return min_eval, best_move


def get_ai_move(cat, mouse, cheese, difficulty='intermediate'):
    cx, cy = cat
    mx, my = mouse

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # no diagonals

    if difficulty == 'intermediate':
        directions += [(-1,-1), (-1,1), (1,-1), (1,1)]
    elif difficulty == 'hard':
        _, move = minimax(cat, mouse, cheese, depth=3, is_cat_turn=True)
        return move if move else cat  # fallback in case no move found

    best_move = cat
    min_dist = float('inf')
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < 7 and 0 <= ny < 7:
            dist = abs(nx - mx) + abs(ny - my)
            if dist < min_dist:
                min_dist = dist
                best_move = (nx, ny)

    return best_move
