class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temps = []
        final = [0] * len(temperatures)
        for i, day in enumerate(temperatures):
            print(stack_temps)
            ## add to the stack if temp is less than day before
            ## or if its the first day
            if len(stack_temps) == 0 or day <= stack_temps[-1]:
                ## to store its index
                stack_temps.append(i)

                stack_temps.append(day)
            else:
                ## if its a warmer day, then need to pop from stack until a day
                ## is colder 
                while (stack_temps and stack_temps[-1] < day):
                    stack_temps.pop() ## remove the day 
                    index = stack_temps.pop() ## get the index of that day
                    final[index] = i - index
                ## store index
                stack_temps.append(i)

                stack_temps.append(day)
        return final

