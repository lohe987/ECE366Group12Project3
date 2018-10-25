
# coding: utf-8

# In[32]:


# Author Group 17
# Machine code to FAST
# Disassembler

input_file = open("project2_group_17_p2_bin.txt", "r")
output_file = open("project2_group_x_p2_asm.txt", "w")

for line in input_file:
    if (line == "\n"):              # empty lines ignored
        continue

    line = line.replace("\n","")    # remove 'endline' character
    print("Instr: ", line)          # show the asm instruction to screen
    line = line.replace(" ","")     # remove spaces anywhere in line
    
    if(line[0:3] == '000'):         # init instruction
        r = line[3:4]
        imm = line[4:]
        
        r = str(int(r, 2)) # convert to decimal 
        imm = str(int(imm, 2))
       
        
        # update screen and output file
        print("init r",r,", ", imm)
        output_file.write("init r" + r + ", " + imm + "\n")
        
    elif(line[0:3] == '001'):         # load instruction
        r1 = line[3:5]
        r2 = line[5:]
        
        r1 = str(int(r1, 2)) # convert to decimal 
        r2 = str(int(r2, 2)) 
    
       
        
        # update screen and output file
        print("ld r",r1,", r", r2)
        output_file.write("ld r" + r1 + ",r " + r2 + "\n")
        
    elif(line[0:3] == '010'):         # store instruction
        r1 = line[3:5]
        r2 = line[5:]
        
        r1 = str(int(r1, 2)) # convert to decimal 
        r2 = str(int(r2, 2)) 
    
       
        
        # update screen and output file
        print("str r",r1,", r", r2)
        output_file.write("str r" + r1 + ",r " + r2 + "\n")
    
    elif(line[0:5] == '01100'):         # addR instruction
        r = line[5:]
        
        r = str(int(r, 2)) # convert to decimal 
        
        # update screen and output file
        print("addR r",r)
        output_file.write("addR" + r + "\n")
    
    elif(line[0:5] == '01110'):         # addR2 instruction
        r = line[5:]
        
        r = str(int(r, 2)) # convert to decimal 
         
        # update screen and output file
        print("addR2",r)
        output_file.write("addR2" + r + "\n")

    elif(line[0:5] == '01111'):         # addR3 instruction
        r = line[5:]
        
        r = str(int(r, 2)) # convert to decimal 
    
       
        
        # update screen and output file
        print("addR3",r)
        output_file.write("addR3" + r + "\n")
    
    elif(line[0:5] == '01101'):         # subR3 instruction
        r = line[5:]
        
        r = str(int(r, 2)) # convert to decimal 
    
       
        
        # update screen and output file
        print("subR3",r)
        output_file.write("subR3" + r + "\n")
    
    elif(line[0:3] == '100'):         # addi instruction
        r1 = line[3:5]
        imm = line[5:]
        
        r1 = str(int(r1, 2)) # convert to decimal 
        imm = str(int(imm, 2)) 
    
       
        
        # update screen and output file
        print("addi r",r1,",", imm)
        output_file.write("addi r" + r1 + ",r " + r2 + "\n")
    
    elif(line[0:3] == '101'):         # sltR0 instruction
        r1 = line[3:5]
        r2 = line[5:]
        
        r1 = str(int(r1, 2)) # convert to decimal 
        r2 = str(int(r2, 2)) 
    
       
        
        # update screen and output file
        print("sltR0 r",r1,", r", r2)
        output_file.write("sltR0 r" + r1 + ",r " + r2 + "\n")
        
    elif(line[0:3] == '010'):         # store instruction
        r1 = line[3:5]
        r2 = line[5:]
        
        r1 = str(int(r1, 2)) # convert to decimal 
        r2 = str(int(r2, 2)) 
    
       
        
        # update screen and output file
        print("str r",r1,", r", r2)
        output_file.write("str r" + r1 + ",r " + r2 + "\n")
    
    elif(line[0:7] == '11111111'):         # score instruction
        r1 = line[4:]
        r1 = str(int(r1, 2))           # convert to decimal  
    
       
        
        # update screen and output file
        print("scrR3R2")
        output_file.write("scrR3R2" + "\n")
    
    elif(line[0:2] == '11'):         # beqR0 instruction
        r = line[2:4]
        imm = line[4:]
        
        r = str(int(r, 2)) # convert to decimal 
        imm = str(int(imm, 2)) 
    
       
        
        # update screen and output file
        print("beqR0 r",r1,",", imm)
        output_file.write("beqR0 r" + r1 + "," + imm + "\n")    
    
    
        

