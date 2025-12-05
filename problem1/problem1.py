min_value = 0
max_value = 99
P = 50
clicks = 0
part2 = True


# New helper function because I'm stupid
# Loop through and calculate the changes
def loops(position):
    maxv = 99
    minv = 0
    if position<minv:
        while position<minv:
            position+=maxv
    elif position>maxv:
            while position>maxv:
                position-=maxv
    return position


# So every "pass" inceases the value
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # line processed
        linep = line.split("\n")
        delta = int(linep[0][1:])
        if "L" in line:
            delta = -1*delta
            while delta != 0:
                P -= 1
                if P == 0 and part2:
                    clicks += 1
                if P == -1:
                    P = 99
                delta += 1
        else:
            while delta != 0:
                P += 1
                if P == 100:
                    P = 0
                    if part2:
                        clicks += 1
                delta -= 1
        # if P+delta<0 or P+delta>99:
        #     P += delta
        #     P = loops(P)
            # clicks+=1
        if P == 0 and not part2:
            clicks += 1

        # if "L" in line:
        #     # Can use regex to split and filter, I'm just gonna check length
        #     # print(val)
        #     val += delta
        #     if val < min_value:
        #         val = (abs(val)+max_value)%max_value
        #         val = max_value-val
        #         # clicks += 1
        # else:
        #     val += delta
        #     if val >max_value:
        #         val = val%max_value
        #         # clicks += 1
        # if val == 0:
        #     clicks += 1
print(clicks)
# P = 50
# d1 = 20
# d2 = -20
# d3 = -60
# d4 = 999
# print("="*80)
# vals = [d1, d2, d3, d4, -100, 101]
# for v in vals:
#     if P+v<0 or P+v>99:
#         P+=v
#         P = abs(P)%99