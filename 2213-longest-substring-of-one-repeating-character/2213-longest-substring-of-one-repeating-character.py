class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s_list = list(s)
        
        tree = [(0, 0, 0)] * (4 * n)

        def merge(l_node, r_node, left_char, right_char, left_len, right_len):
            l_pref, l_suff, l_max = l_node
            r_pref, r_suff, r_max = r_node

            max_len = max(l_max, r_max)
            pref_len = l_pref
            suff_len = r_suff

            if left_char == right_char:
                max_len = max(max_len, l_suff + r_pref)
                
                if l_pref == left_len:
                    pref_len = left_len + r_pref
                if r_suff == right_len:
                    suff_len = right_len + l_suff

            return (pref_len, suff_len, max_len)

        def build(node, start, end):
            if start == end:
                tree[node] = (1, 1, 1)
                return

            mid = (start + end) // 2
            left_child, right_child = 2 * node + 1, 2 * node + 2

            build(left_child, start, mid)
            build(right_child, mid + 1, end)

            tree[node] = merge(
                tree[left_child], tree[right_child],
                s_list[mid], s_list[mid + 1],
                mid - start + 1, end - mid
            )

        def update(node, start, end, idx, char):
            if start == end:
                s_list[idx] = char
                tree[node] = (1, 1, 1)
                return

            mid = (start + end) // 2
            left_child, right_child = 2 * node + 1, 2 * node + 2

            if idx <= mid:
                update(left_child, start, mid, idx, char)
            else:
                update(right_child, mid + 1, end, idx, char)

            tree[node] = merge(
                tree[left_child], tree[right_child],
                s_list[mid], s_list[mid + 1],
                mid - start + 1, end - mid
            )

        build(0, 0, n - 1)

        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(0, 0, n - 1, idx, char)
            ans.append(tree[0][2])

        return ans