<p float="left">
<img src="https://img.shields.io/badge/license-GPLv2-lightgrey.svg" width="80" height="25">
<img src="https://github.com/sagemath/artwork/blob/master/sage-logo-2018.svg" width="80" height="25"> 
</p>


# Compact knapsack Problem

In the preprint paper [arXiv:2303.08973](https://arxiv.org/abs/2303.08973), we present a novel approach to constructing a three-move id scheme, utilizing the compact knapsack problem as a foundation. The corresponding digital signature is created using the Fiat-Shamir transform. The compact knapsack problem involves finding integer solutions to a linear system that satisfies specific constraints. For example, given an integer matrix, we aim to find an integer solution from a specific set. This problem is related to integer-programming problems, which focus on identifying positive integer solutions. Integer Linear Problems, of which the compact knapsack problem is a subset, are utilized in various practical applications such as capital budgeting, warehouse location, and scheduling.

In [^1] we were concerned for compact knapsack problems defined by one equation. Thus, one question that arises from [^1] is why not to use a linear system instead of one linear equation. For instance we do not know if the compact knapsack problem becomes harder or easier when we increase the number of equations $m$. This problem is of independent interest in arithmetic linear algebra and complexity.  To answer this question we study the hardness of compact knapsack problem for linear systems using similar methods as in [^1].

[^1]: K.A.Draziotis, Anastasia Papadopoulou, _Improved attacks on knapsack problem with their variants and a knapsack type ID-scheme._ Advances in Mathematics of Communication 2018, 12(3), Pages 429-449, American Institute of Mathematical Sciences.

In `main.ipynb` we provide `sagemath code` for attacking compact knapsack by using lattices. In fact we apply the following CVP-attack to it. 
![2022-11-16_22-42](https://user-images.githubusercontent.com/7658241/202289817-95c6b93a-ed62-4cda-b7cc-14b180763ba7.png)

An improvement is provided in `improvement.ipynb`.

