import csv

# Open the CSV file
with open(r"G:\My Drive\data analysis\data analysis projects\New folder\Panasonic 18650PF Data\Panasonic 18650PF Data\25degC\EIS\3541_EIS00014.csv") as csvfile:
    reader = csv.reader(csvfile)

    # Find the row that contains "Zreal1" and "Zimg1"
    for row in reader:
        if "Zreal1" in row and "Zimg1" in row:
            # Get the indices of the cells containing "Zreal1" and "Zimg1"
            real_index = row.index("Zreal1")
            img_index = row.index("Zimg1")

            # Create two empty lists to store the numbers under the cells
            real_list = []
            img_list = []

            # Loop over the remaining rows and extract the numbers
            for row in reader:
                if row[real_index] and row[img_index]:
                    try:
                        real_list.append(float(row[real_index]))
                        img_list.append(-1*float(row[img_index]))
                    except:
                        pass
            # Print the two lists
            

            # Exit the loop since we've found what we were looking for
            break
import matplotlib.pyplot as plt

# Plot the two lists as a scatter plot
plt.scatter(real_list, img_list)

# Set the x and y axis labels
plt.xlabel("Real part")
plt.ylabel("Imaginary part")

# Show the plot
plt.show()
