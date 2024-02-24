P=float(input("Enter principal amount:"))
R=float(input("Enter rate of interest per annum:"))
MR=R/(12*100)      #monthly rate of interest
N=int(input("Enter the number of installments:"))
EMI=(P*MR*(1+MR)**N)/(((1+MR)**N)-1)

print("\tEMI Calculation")
print("Principal Amount:",P)
print("rate of interest(per annum):",R)
print("Number of installments:",N)
print("EMI amount:",EMI)
