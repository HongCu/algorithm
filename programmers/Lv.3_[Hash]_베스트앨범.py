def solution(genres, plays):
    answer = []
    genres_sum = defaultdict(int)
    playlist = defaultdict(list)
    
    for i, g, p in zip(range(len(genres)), genres, plays) :
        genres_sum[g] += p
        playlist[g].append([i, p])
        
    items = sorted(genres_sum.items(), key = lambda x : x[1], reverse = True)
    
    for k, v in items:
        playtime = sorted(playlist[k], key = lambda x : x[1], reverse = True)
        for i, p in playtime[:2]:
            answer.append(i)
    return answer
  
  
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	
# return [4, 1, 3, 0]

print(solution(genres, plays))
