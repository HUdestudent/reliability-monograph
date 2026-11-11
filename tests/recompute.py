"""R05 numerical checks. All times are represented numerically in hours."""
import json
import math
import platform

import scipy
from scipy.integrate import quad

eta = 2.0
epsabs = epsrel = 1e-12
before, before_error = quad(
    lambda t: math.exp(-t / eta), 0.0, math.inf,
    epsabs=epsabs, epsrel=epsrel,
)
after, after_error = quad(
    lambda t: math.exp(-t / eta) / eta, 0.0, math.inf,
    epsabs=epsabs, epsrel=epsrel,
)
result = {
    "python": platform.python_version(),
    "platform": platform.platform(),
    "scipy": scipy.__version__,
    "method": "scipy.integrate.quad, interval [0, infinity)",
    "eta_h": eta,
    "epsabs": epsabs,
    "epsrel": epsrel,
    "before_integral": before,
    "before_estimated_abs_error": before_error,
    "before_integral_unit": "h (integrand is dimensionless)",
    "after_integral": after,
    "after_estimated_abs_error": after_error,
    "after_integral_unit": "dimensionless",
    "D_illustrative_gamma_shape": 2,
    "D_illustrative_gamma_scale_h": 500.0,
    "D_illustrative_gamma_mean_h": 1000.0,
    "D_illustrative_hazards_per_h": {
        str(t): t / (500.0 * (500.0 + t))
        for t in [0.0, 500.0, 1000.0]
    },
}
print(json.dumps(result, indent=2, ensure_ascii=False))
