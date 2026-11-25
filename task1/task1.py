import sys

def build_path(n, m):
    if m == 1: 
        return "1" 
    path = []
    current = 0
    while True:
        path.append(str(current + 1))
        last = (current + m - 1) % n
        if last == 0:
            break
        current = last
    return "".join(path)

def main():
    if len(sys.argv) != 5:
        print("Использование: python script.py n1 m1 n2 m2", file=sys.stderr)
    else:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])
        result = build_path(n1, m1) + build_path(n2, m2)
        print(result)

if __name__ == "__main__":
    main()