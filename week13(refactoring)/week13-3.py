''' week6-1
def solution(players, callings):
    answer = []
    run = {players: i for i, players in enumerate(players)}

    for callings in callings:
        idx = run[callings]
        run[callings] -= 1
        run[players[idx - 1]] += 1

        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players'''


def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for name in callings:
        idx = rank[name]
        front = players[idx - 1]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        rank[name] -= 1
        rank[front] += 1

    return players