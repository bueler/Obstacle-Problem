# Obstacle-Problem

## Synopsis

This package contains solvers for obstacle problems of the form

u(x) >= psi(x), x in Omega

Lu(x) <= f(x), x in Omega

u(x)[f(x) - Lu(x)] = 0, x in Omega

u(x) = g(x), x on the boundary of Omega,

where L is a second-order elliptic operator, Omega is closed region in R^2, and psi and g are twice differentiable with psi <= g on the boundary. Included is a geometric multigrid solver, designed to solve elliptic PDEs such as Poisson's equation,  and an implementation of the projected full approximation scheme (PFAS), which solves free boundary problems arising from elliptic PDEs.

The codes in this package were created as part of my MS thesis at the University of Alaska Fairbanks.

## Code Example

A general examples for PFAS is provided in test.py. Specific examples are provided in PFAS_examples, which can be run from a Python 3 console.
