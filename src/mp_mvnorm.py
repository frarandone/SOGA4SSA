from mpmath import mp, matrix, sqrt,sqrtm, exp, pi, erf, powm,det

# Set the precision for mpmath
mp.dps = 50

def mvn_cdf(mean, covariance_matrix, point):
    print(point)
    print(mean)
    print(covariance_matrix)
    """
    Compute the multivariate normal CDF using mpmath.

    Parameters:
    - mean: Mean vector (mpmath matrix).
    - covariance_matrix: Covariance matrix (mpmath matrix).
    - point: Point in the multivariate space (mpmath matrix).

    Returns:
    - CDF value (mpmath mpf).
    """
    dim = len(mean)
    
    # Compute the Mahalanobis distance
    diff = point - mean
    inv_cov = powm(covariance_matrix, -1)
    mahalanobis_distance = sqrtm(diff.transpose() * inv_cov * diff)

    # Compute the CDF using the complementary error function (erfc)
    cdf_value = 0.5 * (1 + erf(mahalanobis_distance[0] / sqrt(2)))

    return cdf_value

def mvn_pdf(mean, covariance_matrix, point):
    """
    Compute the multivariate normal PDF using mpmath.

    Parameters:
    - mean: Mean vector (mpmath matrix).
    - covariance_matrix: Covariance matrix (mpmath matrix).
    - point: Point in the multivariate space (mpmath matrix).

    Returns:
    - PDF value (mpmath mpf).
    """
    dim = len(mean)

    # Compute the Mahalanobis distance
    diff = point - mean
    inv_cov = powm(covariance_matrix, -1)
    mahalanobis_distance = sqrtm(diff.transpose() * inv_cov * diff)

    # Compute the normalization constant
    norm_const = 1 / sqrt((2 * pi) ** dim * det(covariance_matrix))

    # Compute the PDF value
    pdf_value = norm_const * exp(-0.5 * mahalanobis_distance[0]**2)

    return pdf_value

if __name__ == '__main__':
    # Example usage:
    mean_vector = matrix([0, 0,0])
    covariance_matrix = matrix([[1, 0, 0], [0, 1,0],[0,0,1]])
    point_in_space = matrix([1, 1,1])

    cdf_result = mvn_cdf(mean_vector, covariance_matrix, point_in_space)
    pdf_result = mvn_pdf(mean_vector, covariance_matrix, point_in_space)
    print("Multivariate Gaussian CDF using mpmath:", pdf_result)