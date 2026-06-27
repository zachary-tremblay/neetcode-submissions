class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        fleet = 0

        for i in range(len(speed)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse = True)
        
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]

            if not stack  or time > stack[-1]:
                fleet += 1
                stack.append(time)
        return fleet
            
