import numpy as np

scores = np.array([89, 72, 48, 77, 92, 100])

print(f'Your scores are: {scores}')
print(f'Your sum of the scores is: {np.sum(scores)}')
print(f'Your average score is: {np.mean(scores)}')
print(f'The standard deviation of your scores is: {np.std(scores):.1f}')
print(f'Your minimum score is: {np.min(scores)}')
print(f'Your maximum score is: {np.max(scores)}')
adj_ave = (scores.sum() - scores.min())/ (len(scores)-1)
print(f'Your adjusted average score is: {adj_ave}')
print()