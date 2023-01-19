def contains(x: float, platform: list[int]) -> bool:
    """Checks if a particular x-coordinate is contained with the x-coordinates of a platform.

      Args:
        x float: x-coordinate being checked
        platform list[int]: platform being checked

    Returns:
      Bool: True if x is contained inside the x-coordinates of the platform
    """
    return platform[1] <= x <= platform[2]


assert (contains(20.0, [100, 5, 10])) == False  # Works
assert (contains(7.3, [100, 5, 10])) == True  # Works


platforms = []
supports = 0

# Get input and store into list
# N = int(input())
# for i in range(N):
#   platforms.append(list(map(int, input().split())))


platforms = [[50, 50, 90],
             [40, 40, 80],
             [30, 30, 70],
             [20, 20, 60],
             [10, 10, 50]]
platforms.sort(key=lambda x: x[0], reverse=True)
print(platforms)


for idx, platform in enumerate(platforms):
    supports += platform[0] * 2
    if idx > 1:
        if contains(platform[1], platforms[idx-1]) or contains(platform[2], platforms[idx-1]):
            supports -= abs(platforms[idx-1][0] - platform[0])

print(supports)
