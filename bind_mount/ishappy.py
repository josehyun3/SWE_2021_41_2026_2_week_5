def isHappy(n):
    def process(n):
        sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum += digit ** 2
        return sum

    slow = n
    fast = process(n)

    while fast != 1 and slow != fast:
        slow = process(slow)
        fast = process(process(fast))

    return fast == 1

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
        
    print("Results saved to /app/bind_mount/output.txt")