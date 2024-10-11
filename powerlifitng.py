max3S= int(input("What is your max triple Squat? " ))
max3B= int(input("What is your max triple Bench? " ))
max3D= int(input("What is your max triple deadlift? " ))

SBD_triple_max= [max3S, max3B, max3D]

SBD_3x3_Upper_wk4 = [round(i * 1.03, 1) for i in SBD_triple_max]
SBD_3x3_Lower_wk4 = [round(i * 0.97, 1) for i in SBD_triple_max]


SBD_3x3_Upper_wk4 = []
for i in SBD_triple_max:
    SBD_3x3_Upper_wk4.append(round(i * 1.03,1 ))

SBD_3x3_Lower_wk4 = []
for i in SBD_triple_max:
    SBD_3x3_Lower_wk4.append(round(i * 0.97, 1))

block =[SBD_3x3_Upper_wk4]

for i in range(4):
    last_values = block[-1]
    new_values = [round(val * 0.97, 1) for val in last_values]  
    block.append(new_values) 

block.reverse()

print("Calculated Training Weights for a 3x1 Upper set:")
for i, week in enumerate(block[-4:], start=1):
    print(f"Week {i}: {week}")
    
bottom4_weeks = block[:4]

# Output the final block of values for the lower set
print("Calculated Training Weights for a 3x2 Lower set:")
for i, week in enumerate(bottom4_weeks, start=1):
    print(f"Week {i}: {week}")

input("Press Enter to close...")

