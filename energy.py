import csv

# global scope
P_N = [1380, 1450, 1200, 880, 1250, 1750, 1170] # Nuclear
P_C = [2880, 1640, 2000, 1400, 1320, 2210, 1760, 1480, 1026, 1680, 1400, \
      1460, 810, 851, 750, 700, 443, 37.5, 25, 1070, 340, 208, 208, 135] # Coal
CF_N = 0.926 # Nuclear
CF_C = 0.475 # Coal

# header global declaration
h = ['MWea', 'MWeh', 'PJ_(10^15J)']

def main():
    # csv parsing
    with open('energy.csv', 'w') as f:
        # construction (excel standardization)
        w = csv.DictWriter(f, fieldnames=h, extrasaction='raise', dialect='excel')
        w.writeheader()

        # iterable row construction
        for P in P_N:
            w.writerow({h[0]: str(round(P*CF_N, 2)), \
                        h[1]: str(round(P*CF_N*8760, 2)), \
                        h[2]: str(round((P*CF_N*8760*3.6)/(10**6), 2))})

        w.writerow({h[0]:'',h[1]:'',h[2]:''}) # content seperation

        # second iterable construction step
        for P in P_C:
            w.writerow({h[0]: str(round(P*CF_C, 2)), \
                        h[1]: str(round(P*CF_C*8760, 2)), \
                        h[2]: str(round((P*CF_C*8760*3.6)/(10**6), 2))})

    data = ''
    # unoptimized cleaning addition
    # read
    with open('energy.csv', 'r') as f:
        data = f.read(-1)
    # overwrite
    with open('energy.csv', 'w') as f:
        f.write(data.replace(',', ', ').replace('\n\n', '\n'))

if __name__ == '__main__':
    main()
