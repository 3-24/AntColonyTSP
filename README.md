# AntColonyTSP

<div float="left" align="center">
    <img align="top" src="https://imgur.com/9bv0ZOa.gif" alt="Updating Pheromone" width="45%"/>
    <img align="top" src="https://imgur.com/MRQ26XV.gif" alt="Updating Tour" width="45%"/>
    <p>Pheromone Graph (left) and Tour (right) on <a href="http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/berlin52.tsp">berlin52</a> as time advanced</p>
</div>

**Traveling Salesman Problem solver with Ant Colony Optimisation**

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
