## Buffer Overflows
- 32 bit computer is 4 bytes.
- 64 bit 8 bytes
- big string
- pattern create
- pattern offset
- buncha As buncha Bs and Cs
- replace C's with every character
- Find badchars
- find a FFE4
- Find exploitable DLL
- Put in that memory location
- Badchars
  - Take your time with badchars.
  - You must go through the entire list.
  - The badchar will break your shellcode.
  - Two types
    - Ones that break the program
    - Ones that are "filtered" and the rest of the badchars continue to execute.
  - Trampoline
  - Exploitable DLLs are a great place to use jump commands.
    - DLL must not have ASLR on (randomization)
    - Find somewhere that has the four characters you need.
    - Replace the Bs with this address

### The Stack
   - EBP - Base Stack Pointer the base address of the stack.
   - ESP - register - the **stack pointer** or top of the stack
   - EIP - Current reading frame. **Instruction pointer**.
     - first byte **after** the CALL instruction.
     - EIP shows you what is going to be done. It points to the next **INSTRUCTION**
- Write to EIP **and** another register. Then put something in that other register that 
![](images/stack.jpg)
### DEP
  - Data Execution Protection
  - Memory can be declared as **executable** or **data for storage**
### ASLR
  - Memory is handled entirely by the OS and assigned upon request and is randomized in placement each time it is requested.
  - You can easily find a non-ASLR DLL so not as good as DEP.

### Steps of performing a buffer overflow.
1. Run vulnerable application and attach it to immunity debugger.
2. Ensure you have a sript that can normally communicate to target protocol
3. Perform fuzzing on that script with a single character until the application crashes. You want to see EIP cleanly overwritten. Pattern creates can be too similar to OS instructions.
   * Figure out which registers contain mem addresses that are overriden
   * Figure out which registers are overridden themselves. (EIP is the best)
4. Locate the bytes at which EIP was overriden.

### Steps to execute
1. Ensure you have enough room to hide a payload that is your reverse shell but do not make it yet. > 350 bytes would be perfect.
2. Determine bad characters.
   * Can be different all the time because it is determined by the protocol.
   * hex 00 - FF. 
3. Work on redirection, need to find DLL. Use mona.
   * `!mona modules`
   * Make sure you look for at least 4 falses. (Hopefully 5) 
   * `!mona find -s "\xff\xe4" -m SLMFC.dll`
   * prepend payload by 12 NOPs
4. Generate payload and update your exploit code.