with open("input_day_5.txt", "r") as file:
    content = file.read()

updates, orders = content.split('\n\n')

manual = {}
for entry in updates.split('\n'):
    before, after = entry.split('|')
    if before in manual:
        manual[before].add(after)
    else:
        manual[before] = set([after])

# Part 1

res = 0
for entry in orders.split('\n'):
    nums = entry.split(',')
    for i in range(1, len(nums)):
        num = nums[i]
        # Check if curr num should be before at least one previous element in the list 
        if set(nums[:i]).intersection(manual.get(num,set())):
            break
    # If the loop go through
    else:
        res += int(nums[(len(nums))//2])

print(res)

# Part 2

res = 0
for entry in orders.split('\n'):
    nums = entry.split(',')
    flag = False
    for i in range(1, len(nums)):
        num = nums[i]
        if set(nums[:i]).intersection(manual.get(num,set())):
            flag = True
            j = 0
            while j < i and nums[j] not in manual[num]:
                j += 1
            aux = nums[j:i]
            nums[j] = num
            nums[j+1:i+1] = aux
    if flag:
        res += int(nums[(len(nums))//2])

print(res)

