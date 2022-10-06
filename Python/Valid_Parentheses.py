class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                temp=stack.pop()
                if temp=='(' and i==')':
                    continue
                elif temp=='[' and i==']':
                    continue
                elif temp=='{' and i=='}':
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            False
