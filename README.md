# Efficiency

This repository contains some boilerplate repetitive code that Ojasv Kamal wrote to fasten his ML workflow. It contains some of the most common functions that he uses in his ML projects.

## Installation

```bash
pip install --upgrade  git+https://github.com/kamalojasv181/efficiency.git
```

## Features

1. Currently there is only one feature in this package called Config. It supports both nested and non-nested configuration files. Furthermore, you can also override the configuration file using command line arguments. This is useful when you want to vary a few hyperparameters (say to do a grid search) using a single bash script.

## Usage

```python
from efficiency.config import Config

# create a config object
config = Config('config.yaml')

# access variables from the config object (can be nested)
print(config.model.name)

# View the config object
print(config)

# Update the config object
config.update({'model': {'name': 'resnet'}}) # this won't affect other parameters of model variable

# save the config as a yaml file
config.save('config.yaml')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please tag @kamalojasv181 to review your pull request.

## TODOs

- [x] Make it pip installable
- [ ] Add tests
- [ ] Add reading and writing csv, json, txt, mp3 etc.
- [ ] Add logging
- [ ] Add wandb support
