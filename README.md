# AcoTsp

![Pheromone Graph](https://imgur.com/naX7AIv.gif)

Traveling Salesman Problem solver with Ant Colony Optimisation.

## TSP Problem

The problem file format is same as [TSPLIB](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html).

## Usage

Clone this repository and install the Python dependencies through:

```sh
pip3 install -r requirements.txt
```

With prepared problem.tsp file from TSPLIB, run:

```
python3 tsp_solver.py {problem.tsp}
```

It prints the cost and the tour is saved as `solution.csv` file.

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
