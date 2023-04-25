import csv
import sys
from itertools import combinations 
from collections import Counter



#generate the first large 1 item set
def get_large_1_items(data,min_support):
    items = Counter(item for row in data for item in row)
    items = {(i,): j /len(data) for i, j in items.items() if j / len(data) > min_support}
    return dict(sorted(items.items(), key = lambda x: x[1])) #sort in lexi order

#generate Ck from Ck-1
def generate_c(L_k_minus_1):
    c = set(p + (q[-1],) for p in L_k_minus_1 for q in L_k_minus_1 if p[:-1] == q[:-1] and p[-1] < q[-1])
    return set(candidate_set for candidate_set in c
               if all(subset in L_k_minus_1 for subset in combinations(candidate_set, len(candidate_set) - 1)))

#compute the support of one cadidate set 
def cal_support(candidate_set,data):
    num_matching_rows = sum(all(item in row for item in candidate_set) for row in data)
    return num_matching_rows / len(data)



#the apriori algorithm in section 2.1.1 in the paper
#returns all potential set of items above min_support
def apriori(data,min_support):
    lk = get_large_1_items(data,min_support)
    potential_relations = []
    while lk:
        potential_relations.append(lk)
        c = generate_c(lk)
        lk = {candidate_set: cal_support(candidate_set,data) for candidate_set in c if cal_support(candidate_set,data) >=min_support}
        lk = dict(sorted(lk.items(), key = lambda x: x[1]))
    return potential_relations

#generate all association rules
def generate_rules(potential_relations,min_conf):
    rules = {}
    for k, item_set in enumerate(potential_relations[1:]):
        for item, sup in item_set.items():
            for i, antecedent in enumerate(combinations(item, r=len(item) - 1)): #enumerate all the combinations that use one item as consequent and the rest as antecdent.
                antecedent = tuple(antecedent)
                consequent = tuple(item[j] for j in range(len(item)) if j != i)
                confidence = sup / potential_relations[k][antecedent]
                if confidence >= min_conf:
                    rules[antecedent + consequent] = (confidence, sup)
    return rules 

def output_rule(potential_relations,rules,min_conf,min_sup,output_file="output.txt"):
    with open(output_file, "w") as f:
        # Output frequent itemsets
        f.write("==Frequent itemsets (min_sup=%.2f%%)\n" % (min_sup * 100))
        sorted_freq_items = []
        for item_set in potential_relations:
            for items in item_set:
                sorted_freq_items.append((items, item_set[items]))
        sorted_freq_items = sorted(sorted_freq_items, key=lambda x: x[1], reverse=True)
        for items, support in sorted_freq_items:
            f.write("[%s], %.4f%%\n" % (",".join(items), support * 100))
        
        # Output high-confidence association rules
        f.write("\n==High-confidence association rules (min_conf=%.2f%%)\n" % (min_conf * 100))
        sorted_rules = []
        for rule, (confidence, support) in rules.items():
            lhs, rhs = rule[:-1], rule[-1]
            sorted_rules.append((lhs, rhs, confidence, support))
        sorted_rules = sorted(sorted_rules, key=lambda x: x[2], reverse=True)
        for lhs, rhs, confidence, support in sorted_rules:
            f.write("[%s] => [%s] (Conf: %.2f%%, Supp: %.4f%%)\n" % (",".join(lhs), rhs, confidence * 100, support * 100))


def main():
    filename = sys.argv[1]
    min_sup = float(sys.argv[2])
    min_conf = float(sys.argv[3])
    sets_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # create a set from the row
            row_set = set(row)            
            # add the set to the list
            sets_list.append(row_set)
    #print(sets_list)
    large_1_set = get_large_1_items(sets_list,min_sup)
    #print(large_1_set)
    potential_relations = apriori(sets_list,min_sup)
    #print(potential_relations)
    all_rules = generate_rules(potential_relations,min_conf)
    #print(all_rules)
    output_rule(potential_relations,all_rules,min_conf,min_sup,output_file="output.txt")

if __name__ == '__main__':
    main()
