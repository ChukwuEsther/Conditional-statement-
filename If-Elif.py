# if statement
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
nwh = input("Enter nwh:")
nwh = float(nwh)
r = float(rate)
if h > nwh:
    print(((h - nwh)*r*1.5)+nwh*r)
else:
    print(nwh*r)

# elif statement
score = input("Enter Score: ")
score = float(score)
if score>=0.9:
    print('A')
elif score>=0.8:
    print('B')
