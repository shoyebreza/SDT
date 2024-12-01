# Python3 Program to check whether the
# Array is palindromic or not
def palindrome(arr, n):

	# Initialise flag to zero.
	flag = 0;

	# Loop till array size n/2.
	i = 0;
	while (i <= n // 2 and n != 0):

		# Check if first and last element 
		# are different. Then set flag to 1.
		if (arr[i] != arr[n - i - 1]):
			flag = 1;
			break;
		i += 1;

	# If flag is set then print Not Palindrome
	# else print Palindrome.
	if (flag == 1):
		print("Not Palindrome");
	else:
		print("Palindrome");

# Driver code.
arr = [ 1, 2, 3, 2, 1 ];
n = len(arr);

palindrome(arr, n);

# This code is contributed
