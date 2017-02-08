# Disease Spreading Simulation
This project simulates a model of disease spreading in a unidimensional lattice inspired by the paper "Criticality and scaling in evolutionary ecology,
R.V. Solé et. al. TREE 1999". The goal is to show the power of non-linear interactions between the individuals at a very basic level. This model is set as follows: 
 - Initial population of N individuals that can be in just two states, sick or healthy, is distributed at random on an unidimensional lattice.
 - A sick individual infects each neighbour with a probability *β* in the next time step. It is important that each interaction is accounted separately.
 - A sick individual heals in the next time step with probability *γ* provided that it has not been infected in that time step.
 
The results of the program are shown in fraction of sick population *p* against the infecting ratio *β*. Over hundred realisations over the same infecting ratio have been done to avoid stochasticity when computing each *p*. The expected results will have two different regions separated by a critical value of *β*. Before this critical value the infected population ratio will be zero. At about *β*=0.4 the infection no longer dissipates and *p* starts to grow monotonically when increasing *β*. This is somehow an unexpected results because one could very well predict a linear increase in *p* when increasing the infected ratio even at low values. Here it is shown that the non-linear interactions are strong when treating complex systems, even as simple as the one in this model.
 
