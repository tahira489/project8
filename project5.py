def logic_circuit(A, B, C):
    part1 = A and B
    part2 = (B or C) and (B and C)
    Q = part1 or part2
    return Q

print("A B C | Q")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            output = logic_circuit(A, B, C)
            print(A, B, C, "|", int(output))
