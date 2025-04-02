import math
import os
import random
import re
import sys

# Complete the 'luckyYear' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# {"2": "import math\nimport os\nimport random\nimport re\nimport sys\n\n#\n# Complete the 'luckyYear' function below.\n#\n# The function is expected to return an INTEGER.\n# The function accepts INTEGER n as parameter.\n#\n\ndef luckyYear(n):\n    # Write your code here\n    return math.floor(math.log10(n))\n\nif __name__ == '__main__':\n    fptr = open(os.environ['OUTPUT_PATH'], 'w')\n\n    t = int(input().strip())\n\n    for t_itr in range(t):\n        n = int(input().strip())\n\n        result = luckyYear(n)\n\n        fptr.write(str(result) + '\\n')\n\n    fptr.close()\n\nif __name__ == '__main__':\n    t = int(input().strip())\n\n    for t_itr in range(t):\n        n = int(input().strip())\n\n        result = luckyYear(n)\n\n        fptr.write(str(result) + '\\n')\n\n    fptr.close()\n"}
def luckyYear(n):
    """
    Calculate the lucky year based on the logarithm of the input number.
    
    Args:
        n: An integer input
        
    Returns:
        The floor value of log10(n), which is the number of digits in n minus 1
    """
    return math.floor(math.log10(n))

if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Read the number of test cases
    t = int(input().strip())
    
    # Process each test case
    for t_itr in range(t):
        # Read the input value
        n = int(input().strip())
        
        # Calculate the result
        result = luckyYear(n)
        
        # Write the result to the output file
        fptr.write(str(result) + '\n')
    
    # Close the output file
    fptr.close()

###########################################################################################################################