#This code automate the process of cleaning imported text files 

import json

#we first get all the line from the preproinsulin file

with open("preproinsulin_seq.txt", "r", encoding="utf8") as file:
    lines=file.read()
    print(len(lines))
    print(lines)
    
#We then remove "ORIGIN" "61" "1" "//" and the spaces in between the text and the return carriage.

    lines=lines.replace(' ','')
    lines=lines.replace('61','')
    lines=lines.replace('1','')
    lines=lines.replace('//','')
    lines=lines.replace('\n','')
    lines=lines.replace('\t','')
    lines=lines.replace('ORIGIN','')
    
#Next we open the file preproinsulin_seq_clean.txt to write the cleaned sequence into the file

with open("preproinsulin_seq_clean.txt", "w") as file:
    file.writelines(lines)
    print(len(lines))
#print(len(lines))    
#save amino acids sequence 1-24
    amino_seqA=lines[0:24]
    
#open the file Isinsulin_seq_clean.txt to write the amino acid sequence

with open("Isinsulin_seq_clean.txt", "w") as file:
    file.writelines(amino_seqA)
    print(amino_seqA)
    print(len(amino_seqA))  

#save amino acids sequence 25-54
    amino_seqB=lines[24:54]
    
#open the file binsulin_seq_clean.txt to write the amino acid sequence 25 - 54

with open("binsulin_seq_clean.txt", "w") as file:
    file.writelines(amino_seqB)
    print(len(amino_seqB))     


#save amino acids sequence 55-89
    amino_seqC=lines[54:89]
    
#open the file binsulin_seq_clean.txt to write the amino acid sequence 55-89

with open("cinsulin_seq_clean.txt", "w") as file:
    file.writelines(amino_seqC)
    print(len(amino_seqC))

#save amino acids sequence 90-110
    amino_last_seq=lines[89:110]
    
    
#open the file binsulin_seq_clean.txt to write the amino acid sequence

with open("ainsulin_seq_clean.txt", "w") as file:
    file.writelines(amino_last_seq)
    print(len(amino_last_seq))
