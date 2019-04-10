def flipCards(cards, index, position, solution):
  if position == -1:
    position = index

  if len(cards) > 1:
    if cards[index] == 1:
      if (index > 0 and index < len(cards) - 1) and (cards[:index].count(1)%2 == 0 and cards[index+1:].count(1)%2 == 0):
        cards[index - 1] = 1 - cards[index - 1]
        return solution.append(flipCards(cards[:index],0,index,solution))
        
        cards[index + 1] = 1 - cards[index + 1]
        return solution.append(flipCards(cards[index+1:],0,index,solution))

      elif index == 0 and cards[index+1:].count(1)%2 == 0:
        cards[index + 1] = 1 - cards[index + 1]
        return solution.append(flipCards(cards[index+1:],0,index,solution))

      elif index == len(cards) - 1 and cards[:index].count(1)%2 == 0:
        cards[index - 1] = 1 - cards[index - 1]
        return solution.append(flipCards(cards[:index],0,index,solution))

    elif index < len(cards)-1:
      return solution.append(flipCards(cards, index + 1, position, solution))

    else:
      return solution
  else:
    return [position - (len(cards) - index)]


cardSet = list(map(int,input()))

if cardSet.count(1)%2 == 0:
  print('no solution')
else:
  solution = flipCards(cardSet, 0, -1, [])
  print(solution)
