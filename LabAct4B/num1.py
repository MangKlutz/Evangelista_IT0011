A = {'a', 'g', 'b', 'd', 'f', 'j', 'i'}
B = {'l', 'm', 'o', 'b', 'c', 'h', 'd', 'f', 'j', 'i'}
C = {'c', 'd', 'f', 'h', 'k', 'j', 'i'}

A_union_B = A | B
print("(a) Elements in A and B:", len(A_union_B))

B_minus_A_C = B - (A | C)
print("(b) Elements in B not in A and C:", B_minus_A_C)

subset_1 = {'h', 'i', 'j', 'k'}
subset_2 = {'c', 'd', 'f'}
subset_3 = {'b', 'c', 'h'}
subset_4 = {'d', 'f'}
subset_5 = {'c'}
subset_6 = {'l', 'm', 'o'}

print("(c) i:", subset_1)
print("(c) ii:", subset_2)
print("(c) iii:", subset_3)
print("(c) iv:", subset_4)
print("(c) v:", subset_5)
print("(c) vi:", subset_6)
