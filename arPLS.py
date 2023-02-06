import numpy as np
from scipy import sparse
from scipy.sparse import linalg

def arPLS_baseline_correction(spectrum, ratio=1e-6, lambda_value=100, max_iterations=30):
    num_points = len(spectrum)

    # Difference matrix
    diagonal = np.ones(num_points - 2)
    first_diff_matrix = sparse.spdiags([diagonal, -2*diagonal, diagonal], [0, -1, -2], num_points, num_points - 2)

    # Regularization matrix
    regularization_matrix = lambda_value * first_diff_matrix.dot(first_diff_matrix.T)

    # Weight vector
    weights = np.ones(num_points)
    weight_matrix = sparse.spdiags(weights, 0, num_points, num_points)
  
    stop_criterion = 1
    iteration_count = 0

    while stop_criterion > ratio:
        z = linalg.spsolve(weight_matrix + regularization_matrix, weight_matrix * spectrum)
        residual = spectrum - z
        negative_residuals = residual[residual < 0]

        mean_residual = np.mean(negative_residuals)
        std_residual = np.std(negative_residuals)

        new_weights = 1 / (1 + np.exp(2 * (residual - (2*std_residual - mean_residual))/std_residual))

        stop_criterion = np.linalg.norm(new_weights - weights) / np.linalg.norm(weights)
        weights = new_weights
        weight_matrix.setdiag(weights)

        iteration_count += 1

        if iteration_count > max_iterations:
            break

    return z