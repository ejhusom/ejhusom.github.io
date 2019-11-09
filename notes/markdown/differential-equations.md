---
author:
- 'Erik Johannes B. L. G. Husom'
title: 'Differential equations'
---

**Contents**
* TOC
{:toc}

---

# Boundary conditions

Types of boundary conditions:

Dirichlet boundary conditions
: test of math in definition:
$$f(x) = x^2$$

Neumann boundary conditions
: pass


# Finite element method


- W: Interval/domain. Divide this into N_e non-overlapping subintervals W(e),
  e=(0,...,N_e - 1)
- W(e): Each of these subdomains is called an *element*, identified by a unique
  number e.
- Nodes: On each element W(e) we introduce a set of points called *nodes*.
  Assume that the nodes are uniformly space throoughout the element, and that
  the boundary points of the elements are also nodes. Nodes are given numbers
  both within an element (local node numbers: r = (0, ..., d)) and in the
  global domain (global node numbers: i = (0, ..., N_n - 1)).
- Nodes and elements uniquely define a *finite element mesh*. A common special
  case is that of a uniformly partitioned mesh, where each element has the same
  length and the distance between nodes is constant.
- Finite element basis functions: phi_i(x), where the index corresponds to the
  global node number.
- We distinguish between internal nodes (in an element) and shared nodes.



# Time-dependent solving


- Start with approximating time-derivative with finite different method
  (Forward Euler, Backwatd Euler, Crank-Nicolson).
- Express space derivative as stationary variational form.
- Find expression for residual.
- Integration by parts when we have second order derivative on space.



# Solving non-linear ODE and PDE problems


Methods of linearizing non-linear problems:

- Picard iterations
- Newton's method

## Example with logistic ODE

Logistic ODE:

$$u'(t) = u(1-u)$$

Reason for non-linearity: We have a term that is $u^2$.

Forward Euler:
$$\frac{u^{n+1} - u^{n}}{\Delta t} = u^n(1-u^n)$$

Backward Euler:
$$\frac{u^{n} - u^{n-1}}{\Delta t} = u^n(1-u^n)$$

We will get a nonlinear algebraic equation which we call $F(u)$:
$$\Delta t (u^n)^2 + (1-\Delta t)u^n - u^{n-1} = 0$$
We will need the derivative later:
$$F'(u) = 2\Delta t u^n + (1-\Delta t)$$

If you get a non-linear algebraic equation to solve, as above, you need to
linearize it into a series of linear problems.

One particular strategy is the Picard iterations:

$$u^{k,n}, k=0, 1, 2,...$$

- $n$: time level
- $k$: Picard iteration


$$\Delta t u^{k,n} \cdot u^{n, k-1} + (1-\Delta t) u^{n,k} - u^{n-1} = 0$$

To get this started you need to put $u^{n,0} = u{n-1}$.


$$u^{n,k} = \frac{u^{n-1}}{\Delta t u^{n,k-1} + (1-\Delta t)}$$

If you only need one Picard iteration you just replace $u^{n,k-1} = u^{n-1}$.

How to know when to stop? Compare to consecutive iterations, and if the
difference is small enough (it has converged), we stop. We then use $u^{n,K}
and insert it into the algebraic equation for the ODE.

Another method for knowing how to stop is to take the $u$ from each iteration
and insert it into the algebraic equation, and see how close we get to zero.


Linearizing an equation is an art, and there are many approaches that may work,
depending on how the original problem looks. A common method that usually works
on everything is the **Newton's method**.

1. Write the algebraic equation as $F(u) = 0$.
2. Linearize $F(u)$ by two terms from the Taylor series:

$$F(u) \approx F(u^-) + F'(u^-)(u - u^-) = \hat{F}(u)$$

3. The linear equation $\hat{F}(u) = 0 has the solution

$$u = u^- - F(u^-)/F'(u^-)$$

Note that $\hat{F}$ in Picard and Newton are different.

Newton's method has quadratic convergence if $u^k$ is sufficiently close to the
solution; otherwise it may diverge. The iteration goes like this:

$$u^{k+1} = u^k - F(u^k)/F'(u^k), k=0, 1, ...$$

A problem is that the Picard and Newton iterations may change the solution too
much. We can apply *relaxation*, which means less change in the solution, to
the problem. We set $u^*$ to be the suggested value from the Picard/Newton
iteration, and we use a relaxation parameter $\omega$ to regularize the value.
We have

$$u^* = u^- - \frac{F(u^-)}{F'(u^-)}$$
$$u = \omega u^* + (1-\omega) u^-, w \leq 1$$
$$u = \omega u^- - \omega \frac{F(u^-)}{F'(u^-)} + (1 - \omega)u^-$$

The formula for $u$ then becomes:

$$u = u^- - \omega\frac{F(u^-)}{F'(u^-)}$$

