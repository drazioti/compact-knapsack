# Compact knapsack Problem

See the preprint paper [arXiv:2303.08973](https://arxiv.org/abs/2303.08973)<br>
With Compact knapsack problem we mean the problem of finding integer solutions to a linear system, that satisfy some constraints. Say, $AX=B$ such a system, for some integer matrix $A$ and we want to find an integer solution $X$ that belongs to a special set ${\mathcal{S}}.$ This problem appears to integer-programming problems, where we have to find positive integer solutions, i.e. ${\mathcal{S}}={\mathbb{Z}}_{\ge 0}^n.$ Integer Linear Problems have many practical applications, for instance in _Capital Budgeting, Warehouse Location and _Scheduling_.

In [^1] we were concerned for compact knapsack problems defined by one equation. Thus, one question that arises from [^1] is why not to use a linear system instead of one linear equation. For instance we do not know if the compact knapsack problem becomes harder or easier when we increase the number of equations $m$. This problem is of independent interest in arithmetic linear algebra and complexity.  To answer this question we study the hardness of compact knapsack problem for linear systems using similar methods as in [^1].

[^1]: K.A.Draziotis, Anastasia Papadopoulou, _Improved attacks on knapsack problem with their variants and a knapsack type ID-scheme._ Advances in Mathematics of Communication 2018, 12(3), Pages 429-449, American Institute of Mathematical Sciences.

In `main.ipynb` we provide `sagemath code` for attacking compact knapsack by using lattices. In fact we apply the following CVP-attack to it. 
![2022-11-16_22-42](https://user-images.githubusercontent.com/7658241/202289817-95c6b93a-ed62-4cda-b7cc-14b180763ba7.png)

An improvement is provided in `improvement.ipynb`.

Finally, in [arXiv 2303.08973](https://arxiv.org/abs/2303.08973), we provide a three-move id scheme based on compact knapsack problem and also the corresponding digital signature using Fiat-Shamir transform.

