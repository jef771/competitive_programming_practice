import sys
import collections

def get_balance(s):
    closing = ['}', ']', ')']
    opening = ['{', '[', '(']
    deque_front = collections.deque()
    deque_back = collections.deque()

    for i in s:
        if i in opening:
            deque_front.appendleft(i)
        elif i in closing:
            deque_back.appendleft(i)
            
            try:
                if deque_back[0] == '}' and deque_front[0] == '{':
                    deque_front.popleft()
                    deque_back.popleft()
                elif deque_back[0] == ']' and deque_front[0] == '[':
                    deque_front.popleft()
                    deque_back.popleft()
                elif deque_back[0] == ')' and deque_front[0] == '(':
                    deque_front.popleft()
                    deque_back.popleft()
            except IndexError:
                return 'NO\n'

    
    if not deque_front and not deque_back:
        return 'YES\n'
    else:
        return 'NO\n'



def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    q = int(sys_in.readline().rstrip())

    for _ in range(q):
        s = sys_in.readline().rstrip()
        sys_out.write(f'{get_balance(s)}')

if __name__ == '__main__':
    main()