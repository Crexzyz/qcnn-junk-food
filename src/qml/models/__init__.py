"""
Hybrid quantum-classical neural network models.
"""

from .binary import BatchedGPUHybridQuantumCNN
from .multilabel import BatchedGPUHybridQuantumMultiLabelCNN

__all__ = [
    "BatchedGPUHybridQuantumCNN",
    "BatchedGPUHybridQuantumMultiLabelCNN",
]
