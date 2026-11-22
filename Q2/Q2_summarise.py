"""Route summarisation: find the one prefix that covers a list of networks."""

def to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d

def to_ip(n):
    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))

def summarise(networks):
    nets = [(to_int(n.split("/")[0]), int(n.split("/")[1])) for n in networks]
    first = min(a for a, _ in nets)
    last = max(a + 2 ** (32 - p) - 1 for a, p in nets)
    used = sum(2 ** (32 - p) for _, p in nets)
    # TODO 1: Find the longest prefix length (from 32 down to 0) for which first and
    # last have the same network part: (first >> (32 - length)) == (last >> (32 -
    # length)). Clear the host bits of first to get the summary address, and return the
    # text "a.b.c.d/length", the number of addresses it covers (2 ** (32 - length)) and
    # used
    for length in range(32, -1, -1):
        shift = 32 - length
        if (first >> shift) == (last >> shift):
            mask = (0xFFFFFFFF << shift) & 0xFFFFFFFF
            return f"{to_ip(first & mask)}/{length}", 2 ** shift, used

PLANS = {
    "Four regional offices": ["172.18.24.0/24", "172.18.25.0/24", "172.18.26.0/24",
                              "172.18.27.0/24"],
    "Fifth office added": ["172.18.24.0/24", "172.18.25.0/24", "172.18.26.0/24",
                           "172.18.27.0/24", "172.18.28.0/24"],
    "Gap in the numbering": ["10.4.0.0/24", "10.4.2.0/24", "10.4.3.0/24"],
}
for name, nets in PLANS.items():
    summary, covered, used = summarise(nets)
    extra = covered - used
    print(f"{name:<22} {summary:<16} covers {covered:5d} owned {used:5d} extra {extra}")
