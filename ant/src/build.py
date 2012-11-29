# build file for the ant

# set up the id
MAX_ID = 1099511627775 # FF FF FF FF FF
INCREMENTATION = 1

current_val = 1;
# read in the current id
with open("id.c") as f:
  data = f.read().split("\n")[4:] # skip the first 5 lines
  val = ""
  for line in reversed(data):
    if len(line) > 1:
      # parse out the hex
      val += line.split(" ")[2].replace("0x", "")#.decode("hex")
    
  current_val = int(val, 16)
  print current_val

# increment the current val
current_val += INCREMENTATION
print current_val
current_val = hex(current_val).replace("0x", "").upper()
# split up current val into an array
current_vals = [current_val[i:i+2] for i in range(0, len(current_val), 2)]

print current_vals
#replace id.c


# /*
#  * THIS IS AN AUTOGENERATED FILE.
#  * DO NOT TOUCH.
# */

#define ID_1 0x0F
#define ID_2 0x01
#define ID_3 0x00
#define ID_4 0x00
#define ID_5 0x00

with open('id.c', 'w') as f:

  f.write("""/*
  * THIS IS AN AUTOGENERATED FILE.
  * DO NOT TOUCH.
  */

""")
  
  i = 1
  for val in reversed(current_vals):
    if val == "0": val = "00" 
    f.write("#define ID_" + str(i) + " 0x"+str(val) + "\n")
    i += 1

  # pad the rest with zeros
  while i < 6:
    f.write("#define ID_" + str(i) + " 0x00\n")
    i += 1


