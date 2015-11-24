
import numpy as np


def ellipse_extent(a, b, theta):
    """
    Calculates the extent of a box encapsulating a rotated 2D ellipse.

    Function from astropy.modelling.utils: https://github.com/astropy/astropy/blob/master/astropy/modeling/utils.py#L571
    This local copy is temporary and will be removed after the next astropy release.

    Parameters
    ----------
    a : float
        Major axis.
    b : float
        Minor axis.
    theta : float
        Rotation angle in radians.
    Returns
    -------
    offsets : tuple
        The absolute value of the offset distances from the ellipse center that
        define its bounding box region, ``(dx, dy)``.
    Examples
    --------
    .. plot::
        :include-source:
        import numpy as np
        import matplotlib.pyplot as plt
        from astropy.modeling.models import Ellipse2D
        from astropy.modeling.utils import ellipse_extent, render_model
        amplitude = 1
        x0 = 50
        y0 = 50
        a = 30
        b = 10
        theta = np.pi/4
        model = Ellipse2D(amplitude, x0, y0, a, b, theta)
        dx, dy = ellipse_extent(a, b, theta)
        limits = [x0 - dx, x0 + dx, y0 - dy, y0 + dy]
        model.bounding_box = limits
        image = render_model(model)
        plt.imshow(image, cmap='binary', interpolation='nearest', alpha=.5,
                  extent = limits)
        plt.show()
    """

    t = np.arctan2(-b * np.tan(theta), a)
    dx = a * np.cos(t) * np.cos(theta) - b * np.sin(t) * np.sin(theta)

    t = np.arctan2(b, a * np.tan(theta))
    dy = b * np.sin(t) * np.cos(theta) + a * np.cos(t) * np.sin(theta)

    return np.abs([dx, dy])
