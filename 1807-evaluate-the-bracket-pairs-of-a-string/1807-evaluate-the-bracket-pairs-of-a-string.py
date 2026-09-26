class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know_dict = {k: v for k, v in knowledge}
    
        res = []
        curr_key = []
        in_bracket = False
        
        # Step 2: Iterate through the string
        for char in s:
            if char == '(':
                in_bracket = True
                curr_key = [] # Reset key builder
            elif char == ')':
                in_bracket = False
                # Look up the key, default to "?" if not found
                key_str = "".join(curr_key)
                res.append(know_dict.get(key_str, "?"))
            else:
                if in_bracket:
                    curr_key.append(char)
                else:
                    res.append(char)
                    
        # Step 3: Join and return the evaluated string
        return "".join(res)