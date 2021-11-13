import argparse

parser = argparse.ArgumentParser(
      description = "Solve TSP using Ant Colony Optimisation")

parser.add_argument (
      "-f"
    , "--fitness-limit"
    , dest    = "fitness_limit"
    , default = -1
    , help    = "The number of total fitness evalautions"
    , type    = int
    )


parser.add_argument (
      "-p"
    , "--population-size"
    , dest    = "population_size"
    , default = -1
    , help    = "The size of ant population for ACO"
    , type    = int
    )


parser.add_argument (
      "-d"
    , "--debug"
    , dest    = "debug"
    , default = False
    , help    = "Debug flag"
    , type    = bool
    )

parser.add_argument (
    "--plot"
    , dest    = "plot"
    , default = False
    , help    = "Create pheromone and tour images"
    , type    = bool
    )


parser.add_argument (
      "tsp_file"
    , help    = "Path to .tsp file."
    )