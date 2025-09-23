"""Utility function tests for immune mutation."""

import numpy as np
import pytest

from aisp.base.mutation import (
    clone_and_mutate_continuous,
    clone_and_mutate_binary,
    clone_and_mutate_ranged,
    clone_and_mutate_permutation
)


@pytest.mark.parametrize(
    "vector, n, mutate_as_binary",
    [
        (np.array([True, False, False, True]), 5, True),
        (np.array([0.1, 0.3, 0.3, 0.4, 0.5]), 5, False),
        (np.array([2.1, -0.3, 4.3, 1.4, 0.5]), 5, False),
        (np.array([1, 2, 3, 4, 5], dtype=np.int64), 5, False)
    ],
    ids=[
        "Generate 5 clones with binary features",
        "Generate 5 clones with continuous features",
        "Generate 5 clones with ranged continuous features",
        "Generate 5 clones with permutation features"
    ]
)
def test_generate_mutated_clones(vector, n, mutate_as_binary):
    """
    Test that generate_mutated_clones returns the correct number of clones 
    for both binary and continuous feature vectors.
    """
    if mutate_as_binary:
        result = clone_and_mutate_binary(vector, n)
    else:
        if np.all(vector >= 0.0) and np.all(vector <= 1.0):
            result = clone_and_mutate_continuous(vector, n, np.float64(1.0))
        elif vector.dtype == np.int64:
            result = clone_and_mutate_permutation(vector, n, 1)
        else:
            result = clone_and_mutate_ranged(
                vector, n, np.vstack([np.min(vector), np.max(vector)]), np.float64(1.0)
            )
    assert len(result) == n
