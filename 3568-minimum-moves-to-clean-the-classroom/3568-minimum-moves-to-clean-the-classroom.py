class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r, start_c = 0, 0
        litter_map = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        target_mask = (1 << litter_count) - 1

        queue = deque([(start_r, start_c, energy, 0, 0)])

        visited = {(start_r, start_c, 0): energy}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()

            if curr_energy == 0 and classroom[r][c] != 'R':
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    next_mask = mask
                    cell = classroom[nr][nc]

                    if cell == 'R':
                        next_energy = energy
                    elif (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])

                    if next_mask == target_mask:
                        return moves + 1

                    state = (nr, nc, next_mask)
                    if state not in visited or visited[state] < next_energy:
                        visited[state] = next_energy
                        queue.append((nr, nc, next_energy, next_mask, moves + 1))

        return -1