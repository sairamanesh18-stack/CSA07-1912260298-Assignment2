"""Distance-vector routing (Bellman-Ford) among five routers, with next hops."""

INF = 99
names = "PQRST"
cost = {("P", "Q"): 4, ("P", "R"): 1, ("Q", "R"): 2,
        ("Q", "S"): 6, ("R", "S"): 3, ("S", "T"): 5}
link = {}
for (u, v), c in cost.items():
    link[u, v] = link[v, u] = c

table = {u: {v: (0 if u == v else link.get((u, v), INF)) for v in names} for u in names}
nexthop = {u: {v: (v if (u, v) in link else "-") for v in names} for u in names}

rounds = 0
changed = True
while changed:
    changed = False
    rounds += 1
    old = {u: dict(table[u]) for u in names}      # vectors received this round
    for u in names:
        for n in names:
            if (u, n) not in link:
                continue
            for dest in names:
                # TODO 1: Bellman-Ford update: if going through neighbour n (link cost
                # to n + n's old distance to dest) is cheaper than table[u][dest], store
                # the new cost, set nexthop[u][dest] = n and set changed = True
                candidate = link[u, n] + old[n][dest]
                if candidate < table[u][dest]:
                    table[u][dest] = candidate
                    nexthop[u][dest] = n
                    changed = True

print(f"converged after {rounds} rounds")
for u in names:
    print(u, " ".join(f"{table[u][v]:2d}" for v in names))
print("forwarding table of P:")
for v in names[1:]:
    print(f"  to {v}: cost {table['P'][v]}, next hop {nexthop['P'][v]}")
