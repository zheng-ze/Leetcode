class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words) == 1:
            return [words[0] + " " * (maxWidth - len(words[0]))]
        output = []
        
        curr = [words[0]]
        length = len(words[0])
        i = 1
        
        # Each iteration of outer loop will resolve for 1 sentence
        while i <= len(words):
            # Greedy filling of lines. Make sure that there is at least space between each word
            while i < len(words) and length + len(words[i]) < maxWidth:
                curr.append(words[i])
                length += (1 + len(words[i]))
                i += 1
            
            numExtraSpaces = maxWidth - length
            
            if len(curr) == 1:
                output.append(curr[0] + " " * numExtraSpaces)
            else:
                # No more words -> This is final line so left justify
                if i == len(words):
                    output.append(" ".join(curr) + " " * numExtraSpaces)
                    return output
                
                # Full justify
                
                #Spaces are split evenly but filled from left first
                spaces = [1] * (len(curr) - 1)
                
                for j in range(numExtraSpaces):
                    idx = j % len(spaces)
                    spaces[idx] += 1
                
                sentence = curr[0]
                for j in range(len(spaces)):
                    sentence += " " * spaces[j] + curr[j + 1] 
                output.append(sentence)
            
            if i == len(words):
                return output
            
            curr = [words[i]]
            length = len(words[i])
            i += 1
        
        return output