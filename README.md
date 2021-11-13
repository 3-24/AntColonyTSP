# Ant Colony Optimisation on Traveling Salesman Problem

Install the Python dependencies through

```sh
pip3 install -r requirements.txt
```

berfore running `tsp_solver.py`.

## Directory Structure
Everything is Python 3.9 based.
- `tsp_solver.py` - To run the evaluation, run `python3 tsp_solver.py (problem.tsp)`
- `tsp_parser.py` - tsp problem file parser
- `random_search.py` - random search for hyperparameter optimisation
- `ant_colony.py` - core implementation of ant colony optimisation


## Advanced Usages

To debug the best cost in each stage,

```
python3 solver.py (problem.tsp) --debug=True
```
To draw the pheromone graph and best tour,

```
python3 solver.py (problem.tsp) --plot=True
```

To set the population Size and the fitness limit,

```
python3 solver.py (problem.tsp) -p 4 -f 50000
```
