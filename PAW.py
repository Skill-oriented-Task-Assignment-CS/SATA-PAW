import pandas as pd
import numpy as np
import random, math,json
from pandas.errors import DataError


# from pandas.core.base import DataError


def find_min_max_on_the_fly(new_number):
    if find_min_max_on_the_fly.min_val is None or new_number < find_min_max_on_the_fly.min_val:
        find_min_max_on_the_fly.min_val = new_number

    if find_min_max_on_the_fly.max_val is None or new_number > find_min_max_on_the_fly.max_val:
        find_min_max_on_the_fly.max_val = new_number


# Initialize the minimum and maximum values to None
find_min_max_on_the_fly.min_val = None
find_min_max_on_the_fly.max_val = None

# def normalise_old(score):
#     return score/(score+1)

def normalise(score):
    # Retrieve the final minimum and maximum values
    min_value = find_min_max_on_the_fly.min_val
    max_value = find_min_max_on_the_fly.max_val
    normalized_value = (score - min_value) / (max_value - min_value)
    return normalized_value





def retentionScore(cand, dt_cands, tot_num_of_rounds):
    gamma = 0.5
    r = tot_num_of_rounds
    CI = float(dt_cands.loc[cand, "payments"]) 
    # print("taskdone overall,", taskDone) 
    # print("cand counted tasks",taskDone['cand'])
    # count= random.randint(0,50)
    expense=0.1*CI
    if ( (dt_cands.loc[cand, "tags"]) == "C"):
         count= random.randint(1,10)
    else:
        count=0

    score = (CI + gamma) / (
        r + gamma + count + expense
    )  # calculating the competency allowance
    if(CI>0):
     print("cand CI ",CI)
     print("count ", count)
     print("expense", expense)
     print("retention score", score)
    return score


def updateBudget(ca, budget):
    budget = budget - ca
    return budget


def checkBudgetCompetency(ca, budget):
    if ca <= budget:
        decision = 1
    else:
        decision = 0
    return decision


def computeCA(plevel, minPay):
    return plevel * minPay


def WCB_algo(tot_num_of_rounds, dt_cands, dt_tasks, r_curr, r_prev, budget):
    c_b = []
    caDict = {}  # to track record of the sanctioned competency allowances
    dropOuts = []
    retained = []
    plevels = {}  # to track the plevels
    test_retained1={}
    t1=list()
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    t6=[]
    t7=[]
    t8=[]
    t9=[]
    t0=[]
    c=0
    cn=0
    # minPay=float(dt_cands["payments"].mean()) # TO THINK
    minPay = 50
    print("Minpay--------", minPay)
    if tot_num_of_rounds <= 2:
        print("Less than 2 rounds have executed ")
        print("Check status of the current round only")
        for i in range(0, dt_cands.shape[0]):

            if r_curr.iloc[i, 1] == 0:
                c_b.append(i)
                plevel = float(dt_cands.loc[i, "potential"])
                print("pot in WCB", plevel)

                ca = computeCA(
                    plevel, minPay
                )  # getting the min of cand's received payments

                decision = checkBudgetCompetency(ca, budget)

                if decision == 1:  # if budget compatible
                    caDict[i] = ca
                    plevels[i] = plevel
                    budget = updateBudget(ca, budget)
                    # print("Updated budget---->",budget)
                else:
                    print("Reject ", dt_cands.loc[i, "candidates"])

                if budget <= 1000:
                    print("Exceeds Budget", budget)
                    break
        print("caList -->", caDict)
        
        for cand in c_b:
            score = retentionScore(cand, dt_cands, tot_num_of_rounds)
            print("Score of ",cand,"is ",score)
            find_min_max_on_the_fly(score)
            norm_score=normalise(score)
            print("Norm Score of ",cand,"is ",norm_score)
            if norm_score >0.9:
                 t9.append(cand)
            elif norm_score<=0.9 and norm_score>0.8:
                 t8.append(cand)
            elif norm_score<=0.8 and norm_score>0.7:
                 t7.append(cand)
            elif norm_score<=0.7 and norm_score>0.6:
                 t6.append(cand)
            elif norm_score<=0.6 and norm_score>0.5:
                 t5.append(cand)
            elif norm_score<=0.5 and norm_score>0.4:
                 t4.append(cand)
            elif norm_score<=0.4 and norm_score>0.3:
                 t3.append(cand)
            elif norm_score<=0.3 and norm_score>0.2:
                 t2.append(cand)
            elif norm_score<=0.2 and norm_score>0.1:
                 t1.append(cand)
            elif norm_score<=0.1:
                 t0.append(cand)

            if norm_score >0.6:
                retained.append(cand)
                cn=cn+1
            else:
                dropOuts.append(cand)
                if caDict:
                    caDict.pop(cand)
                    plevels.pop(cand)

        # print("Drop outs list--",dropOuts)
        # print("Retained List-->",retained)
        # print("Updated CA-->",caDict)

    else:
        print("rounds--->", tot_num_of_rounds)
        print("Check the status of both current round:r and prev round (r-1) ")
        # r_prev_=r_curr+2
        # print("r_curr",r_curr,"r_prev",r_prev,"r_first",r_prev_)
        for i in range(0, dt_cands.shape[0]):
            # To check candidate has been unallocated in both r and (r-1)
            # But at least been allocatted once so far
            # print("For candidate -->",i)
            if r_curr.iloc[i, 1] == 0 and r_prev.iloc[i, 1] == 0:

                # print("*****In loop 1*****")
                # if dt_cands.iloc[i,r_prev]==0:
                c_b.append(i)
                plevel = float(dt_cands.loc[i, "potential"])

                ca = computeCA(
                    plevel, minPay
                )  # getting the min of cand's received payments

                decision = checkBudgetCompetency(ca, budget)

                if decision == 1:  # if budget compatible
                    # print("**********")
                    caDict[i] = ca
                    plevels[i] = plevel
                    budget = updateBudget(ca, budget)
                    # print("Updated budget-->",budget)
                else:
                    print("Reject ", dt_cands.loc[i, "candidates"])

            if budget <= 1000:
                print("Exceeds Budget", budget)
                break
        
        for cand in c_b:
            score = retentionScore(cand, dt_cands, tot_num_of_rounds)
            print("Score of ",cand,"is ",score)
            norm_score=normalise(score)
            print("Norm Score of ",cand,"is ",norm_score)
            print("Score of ",cand,"is ",score)
            find_min_max_on_the_fly(score)
            norm_score=normalise(score)
            
            if norm_score >0.9:
                 t9.append(cand)
            elif norm_score<=0.9 and norm_score>0.8:
                 t8.append(cand)
            elif norm_score<=0.8 and norm_score>0.7:
                 t7.append(cand)
            elif norm_score<=0.7 and norm_score>0.6:
                 t6.append(cand)
            elif norm_score<=0.6 and norm_score>0.5:
                 t5.append(cand)
            elif norm_score<=0.5 and norm_score>0.4:
                 t4.append(cand)
            elif norm_score<=0.4 and norm_score>0.3:
                 t3.append(cand)
            elif norm_score<=0.3 and norm_score>0.2:
                 t2.append(cand)
            elif norm_score<=0.2 and norm_score>0.1:
                 t1.append(cand)
            elif norm_score<=0.1:
                 t0.append(cand)


            if norm_score >0.5:
                retained.append(cand)
                cn=cn+1
            else:
                    dropOuts.append(cand)
                    if len(caDict):
                        caDict.pop(cand)
                        plevels.pop(cand)

    test_retained1[0.9]=len(t9)
    test_retained1[0.8]=len(t8) 
    test_retained1[0.7]=len(t7)
    test_retained1[0.6]=len(t6)
    test_retained1[0.5]=len(t5)
    test_retained1[0.4]=len(t4) 
    test_retained1[0.3]=len(t3)  
    test_retained1[0.2]=len(t2) 
    test_retained1[0.1]=len(t1)  
    test_retained1[0.0]=len(t0)
   
    return caDict, retained, dropOuts, plevels,test_retained1, c,cn


def naiveRetention(tot_num_of_rounds, dt_cands, dt_tasks, r_curr, r_prev, budget):
    dropOuts = []
    retained = []
    caDict = {}
    c_b = []
    minPay = 50
    print("Minpay--------", minPay)
    if tot_num_of_rounds <= 2:
        print("Less than 2 rounds have executed ")
        print("Check status of the current round only")
        for i in range(0, dt_cands.shape[0]):
            if r_curr.iloc[i, 1] == 0:
                c_b.append(i)  # fisrt consider all unalllocated workers

        ca = minPay  # ca is directly set as minpay
        seed = int(len(c_b) / 2)  # loop through |seed|
        # print("CA--->",ca)
        print("seed --->", seed)
        print("c_b", c_b)
        for j in range(0, seed):
            pick_random = np.random.randint(0, len(c_b))  # to pick any jth index
            # print("random choice--->",pick_random)
            # print("Appended dropout--->",c_b[pick_random])
            item = c_b[pick_random]
            dropOuts.append(item)
            c_b.remove(item)
            print("removed from c_b", item)
            # print("Poped from c_b-->",k)

        print("length of c_b**************", len(c_b))
        for cand in c_b:
            retained.append(cand)
            print("retained cand-->", cand)
            caDict[cand] = ca
            budget = updateBudget(ca, budget)
            if budget <= 1:
                print("Budget Exceeds")
                break

    else:
        print("More than 2 ropunds")
        print("Check status of the current round and prev rounds")
        for i in range(0, dt_cands.shape[0]):
            if r_curr.iloc[i, 1] == 0 and r_prev.iloc[i, 1] == 0:
                c_b.append(i)  # fisrt consider all unalllocated workers

        ca = minPay  # ca is directly set as minpay
        seed = int(len(c_b) / 2)  # loop through |seed|
        # print("seed --->",seed)
        for j in range(0, seed):
            pick_random = np.random.randint(0, len(c_b))  # to pick any jth index
            # print("random choice--->",pick_random)
            # print("Appended dropout--->",c_b[pick_random])
            item = c_b[pick_random]
            dropOuts.append(item)
            c_b.remove(item)
            print("removed from c_b", item)

            # print("Poped from c_b-->",k)

        for cand in c_b:
            retained.append(cand)
            print("retained cand-->", cand)
            caDict[cand] = ca
            budget = updateBudget(ca, budget)
            if budget <= 1000:
                print("Budget Exceeds")
                break

    print("bye bye--------------")
    return caDict, retained, dropOuts, 0

