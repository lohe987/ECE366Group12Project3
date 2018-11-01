
def disassemble(I):
    pass

def assemble(I, lineCount1):
    file = open("i_machine_mem.txt", "w")
    print("******* Assember Starts ********")
    for i in range(lineCount1):
        fetch = I[i]
        fetch = fetch.replace("R","")
        fetch = fetch.replace(" ","")
        #print(fetch[0:4])
        if (fetch[0:3] == "init"):
            fetch = fetch.replace("init","")
            fetch = fetch.split(",")
            R = format(int(fetch[0]),"02b")
            if (fetch[1] == "6"):
                imm = "10"
            elif (fetch[1] == "108"):
                imm = "11"
            else:
                imm = format(int(fetch[1]),"02b")
            op = "000"
            print(op + R + imm)
            file.write(op + R + imm)

        elif (fetch[0:2] == "ld"):
            fetch = fetch.replace("ld","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "001"
            file.write(op + Rx + Ry)

        elif (fetch[0:2] == "st"):
            fetch = fetch.replace("st","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "010"
            file.write(op + Rx + Ry)

        elif (fetch[0:3] == "add"):
            fetch = fetch.replace("add","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "011"
            file.write(op + Rx + Ry)        

        elif (fetch[0:4] == "jpu1"):
            fetch = fetch.replace("jpu1","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"01b")
            Ry = format((int(fetch[1]) - 2),"01b")
            print(fetch[2])
            if (fetch[2] == "9"):
                imm = "00"    
            elif (fetch[2] == "6"):
                imm = "01"
            elif (fetch[2] == "24"):
                imm = "10"
            elif (fetch[2] == "18"):
                imm = "11"
            print(imm)
            op = "100"
            file.write(op + Rx + Ry + imm)

        elif (fetch[0:4] == "jpu2"):
            fetch = fetch.replace("jpu2","")
            fetch = fetch.split(",")
            Rx = format((int(fetch[0]) - 2),"01b")
            Ry = format(int(fetch[1]),"01b")
            if (fetch[2] == "14"):
                imm = "00"    
            elif (fetch[2] == "8"):
                imm = "01"
            elif (fetch[2] == "27"):
                imm = "10"
            op = "101"
            file.write(op + Rx + Ry + imm)    
 #       elif (fetch[0:4] == "subR3"):
 
            file.close()


def simulate(I,Nsteps,debug_mode,Memory):
    PC = 0              # Program-counter
    DIC = 0
    Reg = [0,0,0,0]     # 4 registers, init to all 0
    print("******** Simulation starts *********")
    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        if(debug_mode):
            print(fetch)
        if (fetch[0:3] == "000"):  # init
            MUX = [0,1,6,108]
            R = int(fetch[3:5],2)
            MUXindex = int(fetch[5:7],2)
            imm = MUX[MUXindex]
            Reg[R] = imm
            PC += 1
        elif (fetch[0:3] == "001"):  # ld
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            Reg[Rx] = Memory[Reg[Ry]]
            PC += 1
        elif (fetch[0:3] == "010"):  # st
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            Memory[Reg[Ry]] = Reg[Rx]
            PC += 1
        elif (fetch[0:3] == "011"):  # add
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[0:3] == "100"):  # jpu1
            MUX = [9,6,24,18]
            Rx = int(fetch[3],2)
            Ry = 2 + int(fetch[4],2)
            imm = MUX[int(fetch[5:7],2)]
            if Reg[Rx] < Reg[Ry]:
                PC = imm
            else:
                PC += 1
        elif (fetch[0:3] == "101"):  # jpu2
            MUX = [14,8,27]
            Rx = 2 + int(fetch[3],2)
            Ry = int(fetch[4],2)
            imm = MUX[int(fetch[5:7],2)]
            if Reg[Rx] < Reg[Ry]:
                PC = imm
            else:
                PC += 1
        elif (fetch[0:5] == "11100"): # subR3
            Ry = int(fetch[5:7],2)
            Reg[3] = Reg[3] - Reg[Ry]
            PC += 1
        elif (fetch[0:5] == "11101"):   # inc
            Rx = int(fetch[5:7],2)
            Reg[Rx] = Reg[Rx] + 1
            PC += 1
        elif (fetch == "1111110"):
            Reg[3] = Reg[3]*6
            PC += 1
        elif (fetch == "1111111"):
            Rx = Reg[3]
            Ry = Reg[2]
            binRx = bin(Rx).replace('0b','')
            binRy = bin(Ry).replace('0b','')

            some0 = ''
            for i in range(16-len(binRx)):
                some0 += '0'
            binRx = some0 + binRx

            some0 = ''
            for i in range(16-len(binRy)):
                some0 += '0'
            binRy = some0 + binRy

            score = 0
            for i in range(0,16):
                if binRx[i] == binRy[i]:
                    score +=1
            Reg[3] = score
            PC += 1

        elif(PC == len(I)):
            finished = True
        if(debug_mode):
            if ( (DIC % Nsteps) == 0): # print stats every Nsteps
                print("Registers R0-R3: ", Reg)
                print("Program Counter : ",PC)
                #print("Memory: ",Memory)   # Dont print memory atm.
                                            # Too much cluster
                input("Press any key to continue")
                print()
        else:
            continue

    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    #print("Memory :",Memory)

    data = open("d_mem.txt","w")    # Write data back into d_mem.txt
    for i in range(len(Memory)):
        data.write(format(Memory[i],"016b"))
        data.write("\n")
    data.close()

def main():
    print("Welcome to ECE366 Project3 Group12 ISA Simulator!")
    
    program = int( input("Enter which program to run: ") )
    if ( program == 1 ):
        instr_file = open("prog1.txt","r")
    elif ( program == 2 ):
        instr_file = open("prog2.txt","r") 
    data_file = open("d_mem.txt","r")
    Memory = []
    debug_mode = False  # is machine in debug mode?
    Nsteps = 3          # How many cycle to run before output statistics
    Instruction = []    # all instructions will be stored here
    machineInstruction = [] 
    print(" 1 = simulator")
    print(" 2 = disassembler")
    print(" 3 = assembler")
    mode = int(input("Please enter the mode of program: "))
    print("Mode selected: ",end="")
    if( mode == 1):
        print("Simulator")
        print("Simulator has 2 modes: ")
        print(" 1] Normal execution")
        print(" 2] Debug mode")
        simMode = int(input("Please select simulator's mode: "))
        if ( simMode == 1):
            debug_mode = False
        elif (simMode == 2):
            debug_mode = True
            Nsteps = int(input("Debug Mode selected. Please enter # of debugging steps: "))
        else:
            print("Error, unrecognized input. Exiting")
            exit()
    elif ( mode == 2):
        print("Disassembler is unready!")
    elif ( mode == 3):
        print("Assembler is unready!")
    else:
        print("Error. Unrecognized mode. Exiting")
        exit()
    #mode = 1            # 1 = Simulation
                        # 2 = disassembler
                        # 3 = assembler
    lineCount = 0
    for line in instr_file: # Read in instr
        if (line == "\n" or line[0] =='#' or ':' in line):              # empty lines,comments ignored
            continue
        line = line.strip()
        Instruction.append(line)                        # Copy all instruction into a list
        lineCount += 1
        
    print("Calling assembler...")
    assemble(Instruction, lineCount)
    m_instr_file = open("i_machine_mem.txt", "r")
    for line in m_instr_file:
        machineInstruction.append(line)
    m_instr_file.close() 

    for line in data_file:  # Read in data memory
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        line = line.strip()
        Memory.append(int(line,2))

    if(mode == 1):   # Check wether to use disasembler or assembler or simulation
        simulate(machineInstruction,Nsteps,debug_mode,Memory)
    elif(mode == 2):
        disassemble(Instruction)
    else:
        assemble(Instruction, lineCount)

    instr_file.close()
    data_file.close()

if __name__ == "__main__":
    main()
