import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            drawn_balls = self.contents.copy()  
            self.contents.clear() 
        else:
            drawn_balls = random.sample(self.contents, num_balls_drawn)
            for ball in drawn_balls:
                self.contents.remove(ball)
            
        return drawn_balls     

    def __str__(self):
        return f'{self.contents}'


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    probability = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    if success_count > 0:
        probability = success_count / num_experiments

    return probability



hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(f'Before draw (Hat1): {hat1}\n')
drawn = hat1.draw(3)
print(f'Drawn balls: {drawn}\n')
print(f'After draw: {hat1}\n\n\n')

print(f'Before draw (Hat2): {hat2}\n')
drawn = hat2.draw(3)
print(f'Drawn balls: {drawn}\n')
print(f'After draw: {hat2}\n\n\n')
 
print(f'Before draw (Hat3): {hat3}\n')
drawn = hat3.draw(3)
print(f'Drawn balls: {drawn}\n')
print(f'After draw: {hat3}\n')  


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=10,
                  num_experiments=2000)
print('Probability:', probability)                  