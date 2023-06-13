"""  Not: ~
     Imply: ->
     And: and
     Or: or  """
def negate(premise):
    #inverse
    if premise.startswith('~'):
        return None
    return '~' + premise

def modus_tollens(premises, a_implies_b, not_b):
    # -q and p -> q returns q
    if not_b == a_implies_b.split('->')[1].strip():
        return negate(a_implies_b.split('->')[0].strip())
    return None

def modus_ponens(premises, a_implies_b):
    # p and p -> q, returns q
    antecedent = a_implies_b.split('->')[0].strip()
    consequent = a_implies_b.split('->')[1].strip()
    if antecedent in premises:
        return consequent
    return None

def hypothetical_syllogism(premises, a_implies_b, b_implies_c):
    # p -> q and q -> r returns p -> r
    a = a_implies_b.split('->')[0].strip()
    b = a_implies_b.split('->')[1].strip()
    c = b_implies_c.split('->')[1].strip()
    if b == b_implies_c.split('->')[0].strip() and a in premises:
        return a + ' -> ' + c
    return None

def disjunctive_syllogism(premises, a_or_b, not_a):
    # p or q and ~p returns q"""
    if not_a == negate(a_or_b.split(' or ')[0].strip()):
        return a_or_b.split(' or ')[1].strip()
    return None

def addition(premises, a):
    # p or any variable
    return a + ' or ' + a

def simplification(premises, a_and_b):
    # p and q returns p
    if ' and ' in a_and_b:
        a = a_and_b.split(' and ')[0].strip()
        b = a_and_b.split(' and ')[1].strip()
        if a in premises:
            return a
    return None

def conjunction(premises, a, b):
    # p and q
    if a in premises and b in premises:
        return a + ' and ' + b
    return None

def resolution(premises, a_or_b, not_a_or_c):
    # p or q and ~p or r, returns q or r
    a = a_or_b.split(' or ')[0].strip()
    b = a_or_b.split(' or ')[1].strip()
    not_a = not_a_or_c.split(' or ')[0].strip()
    c = not_a_or_c.split(' or ')[1].strip()
    if a == negate(not_a) and b == c:
        return b + ' or ' + c
    return None

def apply_rules_of_inference(premises):
    # Iterating over all possible combinations of premises applying all the inference rules
    conclusions = set()

    for premise in premises:
        conclusions.add(premise)

    for premise1 in premises:
        for premise2 in premises:
            if premise1 != premise2: #same premise is not used twice in the same rule of inference
                conclusion = modus_ponens(premises, premise1 + ' -> ' + premise2)
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = hypothetical_syllogism(premises, premise1 + ' -> ' + premise2, premise2 + ' -> ' + 'C')
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = hypothetical_syllogism(premises, premise2 + ' -> ' + 'C', premise1 + ' -> ' + premise2)
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = modus_tollens(premises, premise1 + ' -> ' + premise2, negate(premise2))
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = disjunctive_syllogism(premises, premise1 + ' or ' + premise2, negate(premise1))
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = disjunctive_syllogism(premises, premise1 + ' or ' + premise2, negate(premise2))
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = addition(premises, premise1)
                if conclusion is not None:
                    conclusions.add(conclusion)

                conclusion = simplification(premises, premise1 + ' and ' + premise2)
                if conclusion is not None:
                    conclusions.add(conclusion)

                for premise3 in premises:
                    conclusion = conjunction(premises, premise1, premise3)
                    if conclusion is not None:
                        conclusions.add(conclusion)

                    conclusion = conjunction(premises, premise2, premise3)
                    if conclusion is not None:
                        conclusions.add(conclusion)

                    conclusion = resolution(premises, premise1 + ' or ' + premise2, negate(premise1) + ' or ' + premise3)
                    if conclusion is not None:
                        conclusions.add(conclusion)

                    conclusion = resolution(premises, premise1 + ' or ' + premise2, negate(premise2) + ' or ' + premise3)
                    if conclusion is not None:
                        conclusions.add(conclusion)

    return conclusions

def print_conclusions(conclusions):
    if len(conclusions) == 0:
        print('Enter at least one formula.')
    else:
        for conclusion in conclusions:
            print(conclusion)

            
premises = []
while True:
    premise = input('Enter a premise (enter empty line to stop): ')
    if premise == '':
        break
    premises.append(premise)

conclusions = apply_rules_of_inference(premises)
print_conclusions(conclusions)