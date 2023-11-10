import numpy as np
import matplotlib.pyplot as plt

# Control points
control_points = np.array([[4, 6], [7, 12], [14, 14], [19, 11], [21, 4]])

# Basis function for B-Spline of degree 2
def B(i, k, t, knots):
    # The parameters are i (index of the control point), k (degree of the spline), t (parameter value), and knots (array of knot values).
    if k == 0:
        return 1.0 if knots[i] <= t < knots[i+1] else 0.0
    if i + k >= len(knots):  # Check to avoid going out of bounds
        return 0.0
    if knots[i+k] == knots[i]:
        c1 = 0.0
    else:
        c1 = (t - knots[i]) / (knots[i+k] - knots[i]) * B(i, k-1, t, knots)
    if i + k + 1 >= len(knots):  # Check to avoid going out of bounds
        return c1
    if knots[i+k+1] == knots[i+1]:
        c2 = 0.0
    else:
        c2 = (knots[i+k+1] - t) / (knots[i+k+1] - knots[i+1]) * B(i+1, k-1, t, knots)
    return c1 + c2

# Knot vector for degree 2 B-Spline
knots = [0, 0, 0, 1/3, 2/3, 1, 1, 1]  # Example clamped knot vector
# For a degree k B-spline with m control points, you should have a knot vector of size m + k + 1.
degree = 2
# Generate curve points
curve_points = []
# for t in np.linspace(0, 1, 100):
#     point = np.zeros(2)
#     for i in range(len(control_points)):
#         point += B(i, 2, t, knots) * control_points[i]
#     curve_points.append(point)
# Exclude the last knot by reducing the stop value by a small epsilon.
epsilon = 1e-6

# Start from the first non-zero knot value to the last non-zero knot value.
for t in np.linspace(knots[degree], knots[-(degree+1)]- epsilon, 100):
    point = np.zeros(2)
    for i in range(len(control_points)):
        # Only calculate the basis function for knots within the valid range.
        if knots[i] <= t <= knots[i + degree + 1]:
            point += B(i, 2, t, knots) * control_points[i]
    print(f"t={t:.2f}, point={point}")
    curve_points.append(point)

curve_points = np.array(curve_points)

# Plotting
plt.plot(control_points[:,0], control_points[:,1], 'ro-') # Control points
plt.plot(curve_points[:,0], curve_points[:,1], 'b-') # B-Spline curve
plt.title('Degree 2 B-Spline Curve')
plt.show()
