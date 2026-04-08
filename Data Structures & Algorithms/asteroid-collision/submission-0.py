class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # have two stacks to compare collisions
        # [2, 4, -4, -1], []
        # [2, 4, -4], [-1]
        # [2, 4], [-1, -4]

        other = []
        # you will be done when asteroids is empty and they are all in other
        while asteroids:
            # same direction or go apart, so move asteroids[-1] to other
            if (len(other) == 0 
                or (other[-1] < 0 and asteroids[-1] < 0) 
                or (other[-1] > 0 and asteroids[-1] > 0)
                or (other[-1] > 0 and asteroids[-1] < 0)):
                other.append(asteroids.pop())
            # collision, they run into each other
            else:  
                if abs(other[-1]) == abs(asteroids[-1]):
                    other.pop()
                    asteroids.pop()
                elif abs(other[-1]) > abs(asteroids[-1]):
                    asteroids.pop()
                else:
                    other.pop()
        return other[::-1]