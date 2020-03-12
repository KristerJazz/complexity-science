# Complexity Science Package

This package is created mainly for convenience in doing complex systems research.

The design implementation and structure of the package is motivated for scalability and ease of use.
Optimization maybe limited by the design, or the language itself.

## Download

`pip install complexity-science`

-------------------------------------------------------------------------------------

## Cellular Automata

Basic usage:

`import complexity_science.ca as cs`

### 1-D CA

`ca = cs.wolfram(N, 20) #creates a 1-Dimensional CA of N cells with wolfram rule number 20`

`ca.initialize([50]) #initializes the 50th cell of the CA`

`ca.run(100) #returns the resulting state of the CA for 100 iterations following the rule and plots the result with a default colormap`



### 2-D CA

`model = cs.brians_brain([128,128], toroidal=False)` 

Initializes a CA based on brians brain with toroidal boundary conditions



#### *Available models*

`cs.game([dim], toroidal=True)`

`cs.applause([dim],  alpha=1)`

`cs.mpa([dim], percent_mpa=0)`

The `dim` parameter is the only required parameter for all models, others are optional. Parameters are set to default value if not specified.

`alpha` and `percent_mpa` are examples of model specific parameters. 

**See model documentation for more information.**


#### *Modifying Parameters* 

Models can be initialized randomly, binary, by index, using different functions
e.g.

`model.initialize_random()`

`model.initialize_random_bin(0.5)`

`model.initialize_random_int(0,2)`


Models with specific parameters can be modified by this function.

`model.modify_rule(parameter = new_value)` 

*See model documentation for more information on available parameters*



### Adding rules and models

Please contact the author for more information.


## *Animation*  

`model.animate(iteration=100)`

If `iteration` is not set, animation will continue infinitely. 

### Animation in jupyter notebook
```
import complexity_science.ca as cs
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML
```

An example `Game Of Life` animation will be as follows

```
game = cs.game([50,50])
game.initialize_random_bin(0.5)
anim = game.jyp_anim()

HTML(anim.to_html5_video())
```


-----------------------------------------------------------------------------------------

## Network Fragmentation

COMING SOON!

# Contributing:

`git clone https://github.com/KristerJazz/complexity-science.git`

