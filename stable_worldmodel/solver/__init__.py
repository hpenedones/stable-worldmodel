"""Optimization solvers for model predictive control.

This module provides various solver implementations for optimizing action
sequences in world models, including Cross-Entropy Method (CEM), gradient-based
optimization, Model Predictive Path Integral (MPPI), and discrete solvers.
"""

from .cem import CEMSolver
from .gd import GradientSolver
from .mppi import MPPISolver
from .solver import Solver
from .discrete_solvers import PGDSolver

__all__ = [
    'Solver',
    'GradientSolver',
    'CEMSolver',
    'PGDSolver',
    'MPPISolver',
]
