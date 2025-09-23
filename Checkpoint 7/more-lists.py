# names = ["Bob", "Alex", "Kevin"]
# names.append("Joseph")
# for name in sorted(names):
#     print(name)

# List with floates
# measurements = [-2.5, 1.1, 7.6, 14.6, 21.0, 19.2]
# mean = sum(measurements) / len(measurements)
# print(f"The mean is: {mean:.1f}")

# List within lists
# super_list = [[5, 2, 3], [4, 1,], [2, 2, 5, 1]]
# print(super_list[1][0])

# grades = [["Shakira", 8, "D"], ["Melissa", 0, "C"], ["Shensi", 10, "A"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     group = student[2]
#     print(f"{name} from group {group} got a grade of {grade}")

# Matrices 
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
# Print rows
# for row in matrix:
#     print(row)

# print(matrix[0][0])
# print(matrix[1][0])
# print(matrix[2][0])
# print(matrix[0][1])

for column in matrix:
    for row in range(3):
        print(matrix[row])
        