a0_max = 0
a0_pred = 0
a0_predpred = 0
a1_max = 0
a1_pred = 0
a1_predpred = 0
a2_max = 0
a2_pred = 0
a2_predpred = 0

for i in range(int(input())):
    a = int(input())
    if a%3 == 0:
        if a>a0_max:
            a0_predpred = a0_pred
            a0_pred = a0_max
            a0_max = a
        elif a>a0_pred and a<a0_max:
            a0_predpred = a0_pred
            a0_pred = a
        elif a>a0_predpred and a<a0_pred:
            a0_predpred = a
        
