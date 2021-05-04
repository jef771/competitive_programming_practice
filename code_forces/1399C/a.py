# import sys


# def boats_competition(w, n):

    

    


#     return sum_1, sum_2

# def main():
#     sys_in = sys.stdin
#     sys_out = sys.stdout

#     t = int(sys_in.readline())
#     for i in range(t):
#         n = int(sys_in.readline())
#         w = list(map(int, sys_in.readline().split()))

#         sys_out.write(f'{boats_competition(w, n)}\n')


# if __name__ == '__main__':
#     main()



import sys
import string



def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    ans = []
    ans2 = {}
    if not doc_list or not keywords:
        return ans2
    
    for i in keywords:
        ans2[i] = []
    
    temp = '\n'.join(doc_list)
    temp = temp.translate(temp.maketrans('','', string.punctuation))

    ans = temp.split('\n')
        
    for keyword in keywords:
        for i in range(len(ans)):
            temp = ans[i].split()
            for j in temp:
                if j.upper() == keyword.upper():
                    ans2[keyword].append(i)
                        

    return ans2


def main():
    print(multi_word_search(['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?'], ['casino']))
    

if __name__ == '__main__':
    main()