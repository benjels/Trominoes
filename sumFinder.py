val = 9
LIST = [5, 3, 2, 1, 4]

def evaluateList(numbers):
	lo = 0
	hi = len(numbers)-1
	while lo < hi:
		if numbers[lo] + numbers[hi] == val:
			return True
		else:
			if numbers[lo] + numbers[hi] > val:
				hi = hi-1
			else:
				lo = lo+1
	return False

def main():
	LIST.sort()
	print(evaluateList(LIST))

if __name__ == "__main__":
	main()