import random
import sys

jenis = "kertas","batu","gunting"
data = random.choice(jenis)

msk = input("Kamu pilih apa: ").lower()
print("═════════════════════════════")
print("PILIHANMU\tBOT")
print("═════════════════════════════")
besar1 = msk.upper()
besar2 = data.upper()
print(besar1,"\t\t",besar2)

print()
# Kertas
if msk == "kertas" and data == "kertas":
  print("Seri")
elif msk == "kertas" and data == "batu":
  print("Kamu Menang")
elif msk == "kertas" and data == "gunting":
  print("Kamu Kalah")
  
# Batu
elif msk == "batu" and data == "batu":
  print ("Seri")
elif msk == "batu" and data == "gunting":
  print ("Kamu Menang")
elif msk == "batu" and data == "kertas":
  print ("Kamu Kalah")
  
# Gunting
elif msk == "gunting" and data == "gunting":
  print("Seri")
elif msk == "gunting" and data == "batu":
  print("Kamu Kalah")
elif msk == "gunting" and data == "kertas":
  print("Kamu Menang")
  
else:
  print("Pilihan Salah")

print()

