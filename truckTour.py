
def truckTour(petrolpumps, stop = 0):
  currentPump = petrolpumps[0]

  if len(petrolpumps) == 1:
    return stop
  if cantReachNext(currentPump[0], currentPump[1]):
    petrolpumps.append(petrolpumps.pop(0))
    return truckTour(petrolpumps, stop + 1)
  else:
    gasLeft = currentPump[0] - currentPump[1]
    petrolpumps[1][0] += gasLeft
    return truckTour(petrolpumps[1:], stop)
    
def cantReachNext(gas, kms):
  return gas < kms

def main(): 
  n = int(input().strip())
  petrolpumps = []

  for _ in range(n):
    petrolpumps.append(list(map(int, input().rstrip().split())))

  result = truckTour(petrolpumps)
  print(result)

main()