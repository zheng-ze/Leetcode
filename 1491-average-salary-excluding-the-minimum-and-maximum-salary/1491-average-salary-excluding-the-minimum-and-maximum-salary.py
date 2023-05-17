class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        minimum = 10 ** 6
        maximum = 1000

        for i in salary:
            total += i
            minimum = min(minimum, i)
            maximum = max(maximum, i)
        
        return (total - minimum - maximum) / (len(salary) - 2)