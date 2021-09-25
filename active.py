def solution(A):

  if max(A) < 1:
    return 1

  if len(A) == 1 and A[0] != 1:
    return 1

  s = set()
  for a in A:
    if a > 0:
      s.add(a)


  for i in range(1, len(A)):
    if i not in s:
      return i

  return len(s) + 1
A = [1,3,6,4,1,2]

print(solution(A))
