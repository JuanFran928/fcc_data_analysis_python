import numpy as np

def calculate(list):
  if (len(list) == 9) :
      matrix = np.asarray(list).reshape((3, 3))
      matrixF = matrix.flatten('C')
      
      meanH = np.mean(matrix, axis = 0).tolist()
      meanV = np.mean(matrix, axis = 1).tolist()
      meanF = np.mean(matrixF).tolist()
      
      varianceH = np.var(matrix, axis=0).tolist()
      varianceV = np.var(matrix, axis=1).tolist()
      varianceF = np.var(matrixF).tolist()
      
      standardDevH = np.std(matrix, axis = 0).tolist()
      standardDevV = np.std(matrix, axis = 1).tolist()
      standardDevF = np.std(matrixF).tolist()
      
      maxH = np.amax(matrix, axis = 0).tolist()
      maxV = np.amax(matrix, axis = 1).tolist()
      maxF = np.amax(matrix).tolist()
      
      minH = np.amin(matrix, axis = 0).tolist()
      minV = np.amin(matrix, axis = 1).tolist()
      minF = np.amin(matrix).tolist()
      
      sumH = np.sum(matrix, axis = 0).tolist()
      sumV = np.sum(matrix, axis = 1).tolist()
      sumF = np.sum(matrix).tolist()
      
      calculations = {
      'mean': [meanH, meanV, meanF],
      'variance': [varianceH, varianceV, varianceF],
      'standard deviation': [standardDevH, standardDevV, standardDevF],
      'max': [maxH, maxV, maxF],
      'min': [minH, minV, minF],
      'sum': [sumH, sumV, sumF]
      } 
  else:
    raise ValueError("List must contain nine numbers.")
  return calculations
