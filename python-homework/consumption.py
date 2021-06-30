x = input("országúti fogyasztás (l/100km): ")
y = input("városi fogyasztás (l/100km): ")
s1 = input("országúton megtett út (km): ")
s2 = input("városban megtett út (km): ")
ar = input("benzin ára (Ft/l): ")

fogy1 = (int(s1)*int(x)/100 + int(s2)*int(y)/100)

print("autó fogyasztása oda (l): " + str(fogy1))
print("autó fogyasztása oda-vissza (l): " + str(2*fogy1))
print("teljes út költsége (Ft): " + str(2*fogy1*int(ar)))