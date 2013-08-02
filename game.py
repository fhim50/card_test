RANKS = {"A":14,"K":13,"Q":12,"J":11,"10":10,"9":9,"8":8,"7":7,"6":6}

def rank(card):
    """<rank><suite>
    """
    return RANKS.get(card[:-1], None)

    
def suite(card):
    """<rank><suite>
    """
    return card[-1] or None

def lead_card(c1, c2):
    return c2 if suite(c2) == suite(c1) and rank(c2) > rank(c1) else c1


def valid(h,c):
    if suite(c) not in [suite(i) for i in h]:
        return h
    new = []
    for i in h:
        if suite(i) == suite(c):
            new.append(i)
    return new

 
def contains_suite(h,s):
    return suite(s) in [suite(i) for i in h]

    
def winner(lc,pc):
    if suite(lc) != suite(pc):
        return lc
    return lc if rank(lc) > rank(pc) else pc

def is_last_card(h):
    return not len(h) 

def highest_rank(c):
    dic = dict()
    for item in c:
        dic[item] = rank(item)
    h = max(dic.values())
    for key,value in dic.iteritems():
        if h == value:
            return key


def play(hand,leading_card=None):
    if leading_card:
        if contains_suite(hand,suite(leading_card)):
            p = valid(hand,leading_card)
            hand.remove(p[0])
            return p.pop(0),len(hand)
    return hand.pop(0),len(hand)

    