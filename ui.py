def diamond(n):
  """
  Draws a diamond shape with the given number of rows.

  Args:
    n: The number of rows in the diamond.
  """

  # Print the top half of the diamond
  for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

  # Print the bottom half of the diamond (excluding the last row)
  for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Draw the diamond
diamond(rows)