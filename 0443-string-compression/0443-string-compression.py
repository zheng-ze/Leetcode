class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        if len(chars) == 1:
            return 1
        
        read, write = 0, 0
        
        while read < length:
            chars[write] = chars[read]
            count = 1
            write += 1
            
            while read + 1 < length and chars[read] == chars[read + 1]:
                read += 1
                count += 1
            
            if count > 1:
                for char in str(count):
                    chars[write] = char
                    write += 1
            
            read += 1
        
        return write