[![Documentation](https://img.shields.io/badge/Docs-blue.svg)](https://galilai-group.github.io/stable-worldmodel/)
![Tests](https://img.shields.io/github/actions/workflow/status/hpenedones/stable-worldmodel/tests.yaml?label=Tests)
[![PyPI](https://img.shields.io/pypi/v/stable-worldmodel.svg)](https://pypi.python.org/pypi/stable-worldmodel/#history)
[![PyTorch](https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# stable-worldmodel

World model research made simple. From data collection to training and evaluation.

```bash
pip install stable-worldmodel
```

> **Note:** The library is still in active development.

See the full documentation at [here](https://galilai-group.github.io/stable-worldmodel/).

## Installation

### Basic Installation

For basic usage (inference and evaluation):

```bash
pip install stable-worldmodel
```

### With Training Support

To train world models:

```bash
pip install stable-worldmodel[train]
```

### With Environment Support

To use all supported environments:

```bash
pip install stable-worldmodel[env]
```

### Full Installation

For development with all features:

```bash
pip install stable-worldmodel[train,env]
```

### Troubleshooting

- **PyTorch Installation**: If you encounter issues with PyTorch, install it separately first following the [official PyTorch installation guide](https://pytorch.org/get-started/locally/)
- **Environment-specific issues**: Some environments may require additional system dependencies. Refer to the [documentation](https://galilai-group.github.io/stable-worldmodel/) for environment-specific setup instructions.


## Quick Example

```python
import stable_worldmodel as swm
from stable_worldmodel.data import HDF5Dataset
from stable_worldmodel.policy import WorldModelPolicy, PlanConfig
from stable_worldmodel.solver import CEMSolver

# collect a dataset
world = swm.World('swm/PushT-v1', num_envs=8)
world.set_policy(your_expert_policy)
world.record_dataset(dataset_name='pusht_demo', episodes=100)

# load dataset and train your world model
dataset = HDF5Dataset(name='pusht_demo', num_steps=16)
world_model = ...  # your world-model

# evaluate with model predictive control
solver = CEMSolver(model=world_model, num_samples=300)
policy = WorldModelPolicy(solver=solver, config=PlanConfig(horizon=10))

world.set_policy(policy)
results = world.evaluate(episodes=50)
print(f"Success Rate: {results['success_rate']:.1f}%")
```

## Supported Environments

<p align="center">
  <img src="docs/assets/envs_grid_1.gif" alt="Environments Grid 1">
  <br>
  <img src="docs/assets/envs_grid_2.gif" alt="Environments Grid 2">
</p>

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Quick setup for development:

```bash
uv venv --python=3.10
source .venv/bin/activate
uv sync --all-extras --group dev
```

## Questions

If you have a question, please [file an issue](https://github.com/hpenedones/stable-worldmodel/issues).


## Citation

```bibtex
@misc{maes_lelidec2026swm-1,
      title={stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation}, 
      author = {Lucas Maes and Quentin Le Lidec and Dan Haramati and
                Nassim Massaudi and Damien Scieur and Yann LeCun and
                Randall Balestriero},
      year={2026},
      eprint={2602.08968},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2602.08968}, 
}
```