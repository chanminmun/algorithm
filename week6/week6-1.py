# https://school.programmers.co.kr/learn/courses/30/lessons/178871
#  def solution(players, callings):
#    answer = []

#    for i in range(len(callings)):
#       for j in range(len(players)):
#            if callings[i] == players[j]:
#                players[j - 1], players[j] = players[j], players[j - 1]
#
#   return players

#--------------------------------------------------------------------------

def solution(players, callings):
    answer = []
    run = {players: i for i, players in enumerate(players)}

    for callings in callings:
        idx = run[callings]
        run[callings] -= 1
        run[players[idx - 1]] += 1

        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players