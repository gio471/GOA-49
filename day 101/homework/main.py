def burner(c, h, o):
    h2o = min(h // 2, o)
    h -= 2 * h2o
    o -= h2o
    co2 = min(c, o // 2)
    c -= co2
    o -= 2 * co2
    ch4 = min(c, h // 4)
    
    return (h2o, co2, ch4)






def stack_height_2d(layers):
    if layers == 0:
        return 0.0
    sqrt_3_over_2 = 0.86602540378  
    return 1 + (layers - 1) * sqrt_3_over_2
    





def height(n):
    if n < 0:
        return '0.000'
    total_cats = n + 1  
    sum_series = (1 - (0.4 ** total_cats)) / 0.6
    total_height = 2000000 * sum_series
    return '{0:.3f}'.format(total_height)