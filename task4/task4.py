import sys

def main():
    if len(sys.argv) != 2:
        print("Использование: python script.py <файл_с_числами>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        nums = [int(line.strip()) for line in f if line.strip()]

    if not nums:
        print("Файл не содержит чисел")
        return

    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(x - median) for x in nums)

    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()