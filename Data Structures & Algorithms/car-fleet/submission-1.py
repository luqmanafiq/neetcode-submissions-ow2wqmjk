class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # group together position and speed
        cars = sorted(zip(position, speed), reverse=True)
        prev_time = float('-inf')
        fleet = 0
        for pos, speed in cars:
            time = (target - pos) / speed
            # if intersect at target, become one            
            if time > prev_time:
                fleet += 1
                prev_time = time
        return fleet