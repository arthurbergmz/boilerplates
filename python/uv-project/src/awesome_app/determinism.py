from __future__ import annotations

import os
import random


def set_deterministic(seed: int) -> int:
    """Configure deterministic behavior for local Python workflows."""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

    try:
        import numpy as np  # type: ignore
    except Exception:
        return seed

    np.random.seed(seed)
    return seed
