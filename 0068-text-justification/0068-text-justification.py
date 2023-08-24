class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words) == 1:
            return [words[0] + " " * (maxWidth - len(words[0]))]
        output = []
        
        curr = [words[0]]
        length = len(words[0])
        i = 1
        while i < len(words):
            print("1", i)
            # Greedy filling of lines. Make sure that there is at least space between each word
            while i < len(words) and length + len(words[i]) < maxWidth:
                # print("2", i)
                # print(curr)
                curr.append(words[i])
                length += (1 + len(words[i]))
                i += 1
            
            numExtraSpaces = maxWidth - length
            
            if len(curr) == 1:
                output.append(curr[0] + " " * numExtraSpaces)
            else:
                if i == len(words):
                    output.append(" ".join(curr) + " " * numExtraSpaces)
                    return output
                spaces = [1] * (len(curr) - 1)
                
                for j in range(numExtraSpaces):
                    idx = j % len(spaces)
                    spaces[idx] += 1
                
                sentence = curr[0]
                for j in range(len(spaces)):
                    sentence += " " * spaces[j] + curr[j + 1] 
                output.append(sentence)
            if (i < len(words) - 1):
                curr = [words[i]]
                length = len(words[i])
                i += 1
            elif i == len(words) - 1:
                output.append(words[i] + " " * (maxWidth - len(words[i])))
                return output
        
        return output