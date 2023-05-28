def sweeten(min_sweetness, cookies, count = 0):
     
    if min(cookies) >= min_sweetness:
        return count
    if len(cookies) < 2:
        return -1
    cookies.sort()
    if cookies[0] >= min_sweetness:
        return count + 1
    else:
        cookies.append(cookies[0] + (2 * cookies[1]))
        count += 1
        return sweeten(min_sweetness, cookies[2:], count)

print(sweeten(9, [2, 7, 3, 6, 4, 6]))
    

