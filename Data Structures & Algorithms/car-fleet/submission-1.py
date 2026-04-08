class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first zip and sort the two lists based off position. 
        cars = list(zip(position, speed))
        cars.sort(key=lambda car: car[0])

        # get times they reach the end.
        # target - position // speed
        cars = [(target-car[0]) / car[1] for car in cars]

        # now, while loop and check each cars time to get to target. 
        # if a next car has faster time, then it is a part of that fleet.
        # try to visualize it. slower cars make a new fleet
        fleet_time, fleets = 0, 0 
        while cars:
            time = cars.pop()
            if time > fleet_time:
                fleet_time = time
                fleets += 1
            # else: becomes a part of the fleet
        return fleets