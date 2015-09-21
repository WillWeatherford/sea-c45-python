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

    if bp == 'G':
        g_count += 1
    elif bp == 'C':
        c_count += 1
    elif bp == 'A':
        a_count += 1
    elif bp == 'T':
        t_count += 1

gc_count = g_count + c_count
at_count = a_count + t_count
sum_count = gc_count + at_count

# divide the gc_count by the total_count
gc_content = float(gc_count) / sum_count
at_content = float(at_count) / sum_count
g_content = float(g_count) / sum_count
c_content = float(c_count) / sum_count
a_content = float(a_count) / sum_count
t_content = float(t_count) / sum_count
if gc_content > 0.6:
    gc_cls = 'high GC content'
elif gc_content < 0.4:
    gc_cls = 'low GC content'
else:
    gc_cls = 'moderate GC content'

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G-content:', g_count
print 'C count:', c_count
print 'A-content:', a_count
print 'T-content:', t_count
print 'Sum count: ', sum_count
print 'Total count:', total_count
print 'seq length:', len(seq)
print 'AT/GC Ratio:', float(a_count) / gc_count
print 'GC Classification:', gc_cls
