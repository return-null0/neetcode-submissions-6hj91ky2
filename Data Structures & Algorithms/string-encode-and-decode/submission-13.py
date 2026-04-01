class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\znq"
        encoded = ""
        for index, string in enumerate(strs):
            encoded = encoded + string
            if index != len(strs)-1:
                encoded = encoded + "\znq"
        return encoded



    def decode(self, s: str) -> List[str]:
        if s == "\znq": return []
        elif len(s) == 0: return [""]
        else:
            return s.split("\znq")

