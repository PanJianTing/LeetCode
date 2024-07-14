from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        self.idx = 0

        def parse():
            cur_map = defaultdict(int)
            cur_atom = ""
            cur_cnt = ""

            while self.idx < N:
                cur_c = formula[self.idx]
                if cur_c.isupper():
                    if len(cur_atom) > 0:
                        if len(cur_cnt) == 0:
                            cur_map[cur_atom] += 1
                        else:
                            cur_map[cur_atom] += int(cur_cnt)
                    cur_atom = cur_c
                    cur_cnt = ""
                    self.idx += 1
                elif cur_c.islower():
                    cur_atom += cur_c
                    self.idx += 1
                elif cur_c.isdigit():
                    cur_cnt += cur_c
                    self.idx += 1
                elif cur_c == "(":
                    self.idx += 1
                    nested_map = parse()
                    for atom in nested_map:
                        cur_map[atom] += nested_map[atom]
                elif cur_c == ")":
                    if len(cur_atom) > 0:
                        if len(cur_cnt) == 0:
                            cur_map[cur_atom] += 1
                        else:
                            cur_map[cur_atom] += int(cur_cnt)
                    self.idx += 1
                    multiple = ""
                    while self.idx < N and formula[self.idx].isdigit():
                        multiple += formula[self.idx]
                        self.idx += 1
                    if len(multiple) > 0:
                        multiple = int(multiple)
                        for atom in cur_map:
                            cur_map[atom] *= multiple
                    return cur_map
            
            if len(cur_atom) > 0:
                if len(cur_cnt) == 0:
                    cur_map[cur_atom] += 1
                else:
                    cur_map[cur_atom] += int(cur_cnt)

            return cur_map
        
        final_map = parse()
        res = ''
        for atom in sorted(final_map.keys()):
            res += atom
            if final_map[atom] > 1:
                res += str(final_map[atom])

        return res
    

    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        st = []
        idx = 0
        ans = []
        st.append(defaultdict(int))

        while idx < N:
            
            if formula[idx] == "(":
                st.append(defaultdict(int))
                idx += 1
            elif formula[idx] == ")":
                cur_map = st.pop()
                multiple = []
                idx += 1
                while idx < N and formula[idx].isdigit():
                    multiple.append(formula[idx])
                    idx += 1
                if len(multiple) > 0:
                    multiple = int(''.join(multiple))
                else:
                    multiple = 1

                for atom in cur_map.keys():
                    cur_map[atom] *= multiple
                    st[-1][atom] += cur_map[atom]
            else:
                cur_atom = [formula[idx]]
                idx += 1
                cur_cnt = []

                while idx < N and formula[idx].islower():
                    cur_atom.append(formula[idx])
                    idx += 1
                while idx < N and formula[idx].isdigit():
                    cur_cnt.append(formula[idx])
                    idx += 1
                cur_atom = ''.join(cur_atom)
                
                if len(cur_cnt) > 0:
                    cur_cnt = int(''.join(cur_cnt))
                else:
                    cur_cnt = 1
                
                st[-1][cur_atom] += cur_cnt


        for atom in sorted(st[-1].keys()):
            ans.append(atom)
            if st[-1][atom] > 1:
                ans.append(str(st[-1][atom]))

        return "".join(ans)
    


# print(Solution().countOfAtoms("H2O"))
# print(Solution().countOfAtoms("Mg(OH)2"))
# print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
print(Solution().countOfAtoms("Mg(H2O)N"))

