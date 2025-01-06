def two_sets(n):
    # Calculate the total sum of numbers from 1 to n
    total_sum = (n * (n + 1)) // 2

    # Check if the total sum is odd, if so, it's not possible to divide into two equal halves
    if total_sum % 2 != 0:
        print("NO")
    else:
        print("YES")

        # Initialize lists for set1, set2, and a list to keep track of visited elements
        set1, set2 = [], []
        vis = [0] * (n + 1)

        # Initialize set1_sum and max_element
        set1_sum = 0
        max_element = n

        # Loop to fill set1
        while set1_sum < total_sum // 2:
            # Calculate remaining sum needed to make set1_sum equal to total_sum / 2
            remaining_sum = total_sum // 2 - set1_sum

            # If remaining_sum is greater than the maximum element, add the maximum element to set1
            if remaining_sum > max_element:
                set1.append(max_element)
                vis[max_element] = 1
                set1_sum += max_element
                max_element -= 1
            else:
                # If remaining_sum is less than or equal to the maximum element, add remaining_sum to set1
                set1.append(remaining_sum)
                vis[remaining_sum] = 1
                set1_sum = total_sum // 2

        # Loop to fill set2 with non-picked elements
        for i in range(1, n + 1):
            if vis[i] == 0:
                set2.append(i)

        # Print the size and elements of set1
        print(len(set1))
        print(" ".join(map(str, set1)))

        # Print the size and elements of set2
        print(len(set2))
        print(" ".join(map(str, set2)))


# Driver Code
if __name__ == "__main__":
    n = 7
    two_sets(n)
