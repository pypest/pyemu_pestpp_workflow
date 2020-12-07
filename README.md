# pyemu_pestpp_workflow
Demonstration of pyEMU and pest++ workflow with a mf6 freyberg model

### Demo notebooks:
`setup_pestpp_interface.ipynb` for a walkthrough of the steps required to set up a basic PEST interface, including:
* construction of PEST environment directory structure
* adding observations (model outputs) with automatic construction of PEST instruction files (.ins), 
* adding parameters with automatic construction of PEST template files (.tpl),
* defining prior parameter covariance,
* Monte-Carlo sampling of paramter realisations.
`prior_monte_carlo.ipynb` for a rapid fire demonstration of a prior Monte-Carlo uncertainty analysis on the interface constructed in `setup_pestpp_interface.ipynb`

### Don't fancy setting up a local python environment? 
Explore and run demo right from your browser:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pypest/pyemu_pestpp_workflow.git/feat_binder)
