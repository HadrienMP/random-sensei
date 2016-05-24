import random
import itertools
import bisect

def pick(senseis):
    min_times_picked, max_times_picked = _get_min_max_time_picked(senseis)
    weights = _get_weights(senseis, min_times_picked, max_times_picked)
    
    return _random_pick_senseis(senseis, weights)
    
    
def _get_min_max_time_picked(senseis):
    max_times_picked = 0
    min_times_picked = senseis[0]['times_picked']
    
    for sensei in senseis:
        if sensei['times_picked'] > max_times_picked:
            max_times_picked = sensei['times_picked']
        if sensei['times_picked'] < min_times_picked:
            min_times_picked = sensei['times_picked']
            
    return (min_times_picked, max_times_picked)
    
    
def _get_weights(senseis, min_times_picked, max_times_picked):
    
    if not min_times_picked:
        min_times_picked = 1
        
    print(max_times_picked,min_times_picked)
        
    return [int((max_times_picked + 1 - sensei['times_picked']) / min_times_picked ) for sensei in senseis]
    
    
def _random_pick_senseis(senseis, weights):
    even_chance_senseis = list()
    for i, sensei in enumerate(senseis):
        even_chance_senseis.extend([sensei] * weights[i])
    
    print(weights)
    print(len(even_chance_senseis))
    print(senseis)
        
    sensei1 = random.choice(even_chance_senseis)
    sensei2 = sensei1
    
    while sensei2 is sensei1:
        sensei2 = random.choice(even_chance_senseis)
        
    return [sensei1, sensei2]
