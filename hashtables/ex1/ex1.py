def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i, x in enumerate(weights):
        if limit - x in weights:
            cache[i] = limit - x 
    
    result = list(cache.items())
    result.sort(reverse=True)

    pair_item = [x[0] for x in result] if len(result) == 2 else None
    
    return pair_item
