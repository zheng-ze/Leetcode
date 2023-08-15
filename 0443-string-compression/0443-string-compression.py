class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        if len(chars) == 1:
            return 1
        
        c = chars[0]
        count = 1
        modify_pointer = 0
        
        for i in range(1, length):
            if chars[i] == c:
                count += 1
            
            if chars[i] != c:
                chars[modify_pointer] = c
                modify_pointer += 1
                if count > 1:
                    str_count = str(count)
                    chars[modify_pointer : modify_pointer + len(str_count)] = \
                        [x for x in str_count]
                    modify_pointer += len(str_count)
                c = chars[i]
                count = 1
        chars[modify_pointer] = c
        modify_pointer += 1

        if count > 1:
            str_count = str(count)
            chars[modify_pointer : modify_pointer + len(str_count)] = \
                [x for x in str_count]
            modify_pointer += len(str_count)
        
        return modify_pointer