# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
# Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
# Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument for this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
# Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of nucleotides seen so far.
g_count = 0
c_count = 0
a_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    if bp == 'C':
        c_count += 1
    elif bp == 'G':
        c_count += 1
    elif bp == 'A':
        a_count += 1
    elif bp == 'T':
        t_count += 1

gc_count = c_count + g_count
at_count = a_count + t_count
gcat_count = gc_count + at_count

# divide the gc_count by the total_count
gc_content = float(gc_count) / gcat_count
at_content = float(at_count) / gcat_count
c_content = float(c_count) / gcat_count
g_content = float(g_count) / gcat_count
a_content = float(a_count) / gcat_count
t_content = float(t_count) / gcat_count

# Print the answer
# print 'GC-content:', gc_content
# print 'AT-content:', at_content
# print 'C-content:', c_content
# print 'G-content:', g_content
# print 'A-content:', a_content
# print 'T-content:', t_content
# print '---------------------'
print 'Sum of all contents: ', sum((c_count, g_count, a_count, t_count))
print 'total_count variable:', total_count
print 'Length of seq variable:', len(seq)
