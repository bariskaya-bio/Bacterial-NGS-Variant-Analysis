import pysam
import matplotlib.pyplot as plt

# Opening the BAM file (Using your file name from ls -l)
bamfile = pysam.AlignmentFile("mutant_final.sorted.bam", "rb")

# Calculating depth for each position (Your original logic)
depths = [col.nsegments for col in bamfile.pileup()]

# Print basic statistics
print(f"Average Read Depth: {sum(depths) / len(depths):.2f}")

# Plotting
plt.plot(depths)
plt.title("Read Depth Across Genome")
plt.xlabel("Position")
plt.ylabel("Read Count (Depth)")

# Saving the output
plt.savefig("coverage_plot.png")
print("Plot saved as 'coverage_plot.png'.")
