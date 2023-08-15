class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        if len(chars) == 1:
            return 1
        
        read, write = 0, 0
        
        # Invariant: chars from index 0 to write is 'solved'
        # Note: Since we find number of repeats using the inner loop, there is not need
        # to track the previous character. Each iteration of outer loop will be for a new
        # character
        while read < length:
            chars[write] = chars[read]
            count = 1
            write += 1
            
            # Get num of repeats
            while read + 1 < length and chars[read] == chars[read + 1]:
                read += 1
                count += 1
            
            # Write numbers if there are repeats
            if count > 1:
                for char in str(count):
                    chars[write] = char
                    write += 1
            
            # Move to next character
            read += 1
        
        return write