#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    def get(tup, idx):
        return tup[idx] if idx < len(tup) else 0

    tupA_0, tupA_1 = get(tuple_a, 0), get(tuple_a, 1)
    tupB_0, tupB_1 = get(tuple_b, 0), get(tuple_b, 1)

    return (tupA_0 + tupB_0, tupA_1 + tupB_1)
