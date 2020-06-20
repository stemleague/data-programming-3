# You're a bioinformatician working in a genetic engineering research lab! One day, the lab's DNA analysis software breaks and your colleagues are distraught because they will no longer be able to clone a sheep. You decide to help them out by coding your own DNA analysis program from scratch. Given a DNA sequence, your program should be able to output its GC content, reverse complement, and primary transcript. While your colleagues stare forlornly at their cell cultures, you get to work...

# For testing purposes, we will use a randomly generated DNA sequence. Feel free to change the length of the sequence using the 'length' variable. The code you will write should work for any length of DNA.
import random
nucleotides = ['A', 'G', 'C', 'T']
length = 150 
sequence = ''.join([random.choice(nucleotides) for x in range(length)])
# Our randomly generated DNA sequence is stored in the variable 'sequence'. 
print("DNA Sequence (5'->3'):")
print(sequence + "\n")

# Let's calculate the GC-content of our sequence. In other words, what percentage of the sequence contains G's or C's? Do this using a for loop and one conditional and store your answer in the variable 'percent_GC'. 
percent_GC = "I do not work."
# Answer:
GC_count = 0
for nt in sequence:
    if nt == "C" or nt == "G":
        GC_count += 1
percent_GC = 100. * GC_count / length
###
print("GC-Content: " + str(percent_GC) + " %\n")

# How would you find the reverse complement of this sequence? Do this using a for loop and conditionals. (Hint: Use the reversed() function to loop backwards through a list) 
reverse_complement = ""
# Answer:
for nt in reversed(sequence):
    if nt == 'A':
        reverse_complement += 'T'
    elif nt == 'G':
        reverse_complement += 'C'
    elif nt == 'C':
        reverse_complement += 'G'
    elif nt == 'T':
        reverse_complement += 'A'
###
print("Reverse Complement (5'->3'):")
print(reverse_complement + "\n")

# What if we wanted to transcribe the sequence to RNA?
mRNA = ""
# Answer:
for nt in sequence:
    if nt == 'A':
        mRNA += 'U'
    elif nt == 'G':
        mRNA += 'C'
    elif nt == 'C':
        mRNA += 'G'
    elif nt == 'T':
        mRNA += 'A'
###
print("mRNA Transcript (5'->3'):")
print(mRNA)

# Challenge Question! Can you think of a more efficient way to get the reverse complement and transcript? (Hint: use a dictionary)
# reverse_complement = ""
# base_pair_dict = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
# for nt in reversed(sequence):
#     reverse_complement += base_pair_dict[nt]
    
# print("Reverse Complement:")
# print(reverse_complement + "\n")

# transcription_dict = {'A':'U', 'G':'C', 'C':'G', 'T':'A'}
# mRNA = ""
# for nt in range(sequence):
#     mRNA += transcription_dict[nt]
    
# print("mRNA Transcript:")
# print(mRNA)
