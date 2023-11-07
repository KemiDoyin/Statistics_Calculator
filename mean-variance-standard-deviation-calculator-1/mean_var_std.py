import numpy as np

def calculate(num):

  if len(num) == 9 and (num.isdigit() for x in num):
      nums = np.array(num).reshape((3,3))

      result = {
          'mean' :[nums.mean(axis=0).tolist(), nums.mean(axis=1).tolist(), nums.mean()],
        'variance': [nums.var(axis=0).tolist(), nums.var(axis=1).tolist(), nums.var()],
        'standard deviation': [nums.std(axis=0).tolist(), nums.std(axis=1).tolist(), nums.std()],
          'max' : [nums.max(axis=0).tolist(), nums.max(axis=1).tolist(), nums.max()],
        'min': [nums.min(axis=0).tolist(), nums.min(axis=1).tolist(), nums.min()],
        'sum' : [nums.sum(axis=0).tolist(), nums.sum(axis=1).tolist(), nums.sum()],
      }
      return result
  else:
      raise ValueError("List must contain nine numbers.")