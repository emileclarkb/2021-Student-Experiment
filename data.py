# emilecb - 4/6/2020 - data.py

# NATIVE ASSETS
from util import *

# constant declarations
dt = 0.05 # time increment
rnd = 2 # rounding
form = '{'+f':.{rnd}f'+'}' # formatting

headings = ['1', '2', '3', '4', '5', 'avg', 'abs', 'perc'] # headings
headings = ', '.join(headings) + '\n' # style

tmu = 0.01 # time measurement uncertainty



def main():
    # 3 for loops and 6 files open simulataneously... this really is the most
    # optimized algorithm i've ever written...

    # iterate test & trial data
    for i in range(1, 6):
        # reference cutoff distance
        cutoff = i*0.2

        for j in range(1, 6):
            fn1 = f'./Test-{i*2}0/'
            fn2 = f'incline-{i*2}0_{j}.csv'
            # raw position data analysis
            with open(fn1+'rPosition/'+fn2, 'r') as f:
                # styled position data writing
                with open(fn1+'sPosition/s'+fn2, 'w') as fs:
                    # (cutoff) styled position data writing
                    with open(fn1+'scPosition/sc'+fn2, 'w') as cfs:
                        # velocity data writing
                        with open(fn1+'rVelocity/v'+fn2, 'w') as vf:
                            # styled velocity data writing
                            with open(fn1+'sVelocity/sv'+fn2, 'w') as vfs:
                                # (cutoff) styled velocity data writing
                                with open(fn1+'scVelocity/scv'+fn2, 'w') as cvfs:
                                    # short term position memory (last)
                                    pmem = -1
                                    # intial position
                                    xi = -1
                                    # drop detected
                                    drop = False
                                    # has reached the base
                                    grounded = False


                                    lines = f.readlines()
                                    # line iteration
                                    for k, line in enumerate(lines):
                                        # ignore header
                                        if k < 2:
                                            temp = f'{line.strip()}\n'
                                            fs.write(temp)
                                            cfs.write(temp)
                                            vf.write(temp)
                                            vfs.write(temp)
                                            cvfs.write(temp)
                                            continue

                                        # str->float type casting
                                        line = [float(x) for x in line.strip().split(',')]
                                        # initialize memory
                                        if pmem == -1:
                                            pmem = xi = line[1]

                                        # simple drop detection
                                        if (not drop) and (line[1] > xi):
                                            drop = True

                                            # previous data (before pmem)
                                            pre = float(lines[k-2].strip().split(',')[1])
                                            # write last datapoint
                                            fs.write(form.format(round(line[0] - 0.05, rnd)) + ',' + \
                                                     form.format(round(pmem, rnd)) + '\n')
                                            vfs.write(form.format(round(line[0] - 0.05, rnd)) + ',' + \
                                                      form.format(round((pmem-pre)/dt, rnd)) + '\n')

                                            cfs.write(form.format(round(line[0] - 0.05, rnd)) + ',' + \
                                                      form.format(round(pmem, rnd)) + '\n')
                                            cvfs.write(form.format(round(line[0] - 0.05, rnd)) + ',' + \
                                                       form.format(round((pmem-pre)/dt, rnd)) + '\n')


                                        # RAW
                                        # velocity writing
                                        vf.write(form.format(round(line[0], rnd)) + ',' + \
                                                 form.format(round((line[1]-pmem)/dt, rnd)) + '\n')

                                        # STYLED
                                        # displacement didn't decrease and a drop occured
                                        if (line[1] >= pmem) and drop:
                                            # position styling
                                            fs.write(form.format(round(line[0], rnd)) + ',' + \
                                                     form.format(round(line[1], rnd)) + '\n')
                                            # velocity styling
                                            vfs.write(form.format(round(line[0], rnd)) + ',' + \
                                                      form.format(round((line[1]-pmem)/dt, rnd)) + '\n')

                                            # CUTOFF
                                            if not grounded:
                                                # position styling
                                                cfs.write(form.format(round(line[0], rnd)) + ',' + \
                                                          form.format(round(line[1], rnd)) + '\n')
                                                # velocity styling
                                                cvfs.write(form.format(round(line[0], rnd)) + ',' + \
                                                           form.format(round((line[1]-pmem)/dt, rnd)) + '\n')

                                        # simple cutoff detection
                                        # detection run after to allow at most one
                                        # datapoint to "finish" the table
                                        if (line[1] >= cutoff):
                                            grounded = True

                                        # set new memory
                                        pmem = line[1]


    # data briefs
    with open('brief.csv', 'w') as b: # position
        with open('vbrief.csv', 'w') as vb: # velocity
            b.write(headings)
            vb.write(headings)

            # re-iterate test & trial data
            for i in range(1, 6):
                # data row
                data = []
                # velocity data row
                vdata = []

                for j in range(1, 6):
                    fn1 = f'./Test-{i*2}0/'
                    fn2 = f'incline-{i*2}0_{j}.csv'

                    # (cutoff) styled position data writing
                    with open(fn1+'scPosition/sc'+fn2, 'r') as cfs:
                        lines = cfs.readlines()

                        # initial data point
                        dpi = lines[2].strip().split(',')
                        # final datapoint
                        dpf = lines[len(lines)-1].strip().split(',')

                        # time taken
                        t = float(dpf[0]) - float(dpi[0])
                        data.append(form.format(round(t, rnd)))

                        # distance travelled
                        s = float(dpf[1]) - float(dpi[1])
                        vdata.append(form.format(round(s/t, rnd)))

                # mean of a n-tuple
                mean = tmean(data)
                vmean = tmean(vdata)
                data.append(form.format(round(mean, rnd)))
                vdata.append(form.format(round(vmean, rnd)))

                # absolute uncertainty
                abs = tmax(data) - tmin(data)
                vabs = tmax(vdata) - tmin(vdata)
                # account for measurement uncertainty
                if tmu > abs:
                    abs = tmu
                data.append(form.format(round(abs, rnd)))
                vdata.append(form.format(round(vabs, rnd)))

                # percentage uncertainty (of the mean)
                data.append(form.format(round(abs/mean, rnd)))
                vdata.append(form.format(round(vabs/vmean, rnd)))


                # write brief
                b.write(', '.join(data)+'\n')
                vb.write(', '.join(vdata)+'\n')



if __name__ == '__main__':
    main()
