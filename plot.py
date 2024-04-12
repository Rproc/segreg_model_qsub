import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

def plotIntervalConfidence(title, listValue, ciValue, listMethods, path):

    n = len(listValue)
    fig = plt.figure(figsize=(25, 11))

    bars = []
    barsLabels = []
    barWidth = 0.3
    ci = []
    for i in range(0, n):
        bars.append(listValue[i])
        barsLabels.append(listMethods[i])
        ci.append(ciValue[i][1] - ciValue[i][0])

    # The x position of bars
    r1 = np.arange(len(bars))
    # r2 = [x + barWidth for x in r1]

    # Create blue bars
    plt.bar(r1, bars, width = barWidth, edgecolor = 'black', yerr=ci, ecolor= 'xkcd:mustard', capsize=7)

    # Create cyan bars
    # plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='sorgho')

    # general layout
    plt.xticks([r for r in range(len(bars))], listMethods)
    plt.xticks(rotation=90)
    plt.ylabel('Média e intervalo de erro')
    plt.title(title)
    plt.tight_layout()

    # plt.legend()
    name_l = title.replace(' ', '_')
    name_l = name_l.replace('/', '_')
    name = path + name_l + '.png'
    plt.savefig(name)
    plt.close(fig)

    # Show graphic
    # plt.show()

def processPlot2(listFiles, path, outpath, dirfile):

    listDiss = []
    listEntropy = []
    listIndexH = []
    listMethods = []
    ciDiss = []
    ciEntropy = []
    ciIndexH =[]
    title = ''
    j = 0
    for inst in listFiles:
        name = inst + '.csv'

        with open(name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # print(reader)
            i = 0
            next(reader, None)
            # print(reader[1][4])
            for row in reader:
                if i == 0:
                    listMethods.append(dirfile[j])
                    listDiss.append(float(row[4]))
                    ciDiss.append( [float(row[7]), float(row[8])] )
                if i == 1:
                    listEntropy.append(float(row[4]))
                    # listMethods.append(dirfile[j])
                    ciEntropy.append( [float(row[7]), float(row[8])] )

                if i == 2:
                    listIndexH.append(float(row[4]))
                    # listMethods.append(dirfile[j])
                    ciIndexH.append( [float(row[7]), float(row[8])] )

                i += 1
                # print(row[4])
        j += 1

    title_d = 'Comparação da dissimilaridade entre cenarios'
    title_e = 'Comparação da entropia entre cenarios'
    title_i = 'Comparação do indice H entre cenarios'

    # print(listDiss)#, listEntropy, listIndexH)

    plotIntervalConfidence(title_d, listDiss, ciDiss, listMethods, outpath)
    plotIntervalConfidence(title_e, listEntropy, ciEntropy, listMethods, outpath)
    plotIntervalConfidence(title_i, listIndexH, ciIndexH, listMethods, outpath)

def processPlotColor(listFiles, path, outpath, dirfile, color):

    listRed = []
    listYellow = []
    listBlue = []
    listCyan = []
    listMethods = []
    ciRed = []
    ciYellow = []
    ciBlue = []
    ciCyan = []
    title = ''
    j = 0
    for inst in listFiles:
        name = inst + '.csv'

        with open(name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # print(reader)
            i = 0
            next(reader, None)
            # print(reader[1][4])
            for row in reader:
                if i == 0:
                    listMethods.append(dirfile[j])
                    listRed.append(float(row[4]))
                    ciRed.append( [float(row[7]), float(row[8])] )
                if i == 1:
                    listYellow.append(float(row[4]))
                    # listMethods.append(dirfile[j])
                    ciYellow.append( [float(row[7]), float(row[8])] )

                if i == 2:
                    listBlue.append(float(row[4]))
                    # listMethods.append(dirfile[j])
                    ciBlue.append( [float(row[7]), float(row[8])] )

                if i == 3:
                    listCyan.append(float(row[4]))
                    # listMethods.append(dirfile[j])
                    ciCyan.append( [float(row[7]), float(row[8])] )
                i += 1
                # print(row[4])
        j += 1

    title_r = 'Comparação da Exposição do agente ' + color[1:] + ' em relação ao red entre cenarios'
    title_y = 'Comparação da Exposição do agente ' + color[1:] + ' em relação ao yellow entre cenarios'
    title_b = 'Comparação da Exposição do agente ' + color[1:] + ' em relação ao blue entre cenarios'
    title_c = 'Comparação da Exposição do agente ' + color[1:] + ' em relação ao cyan entre cenarios'

    # print(listDiss)#, listEntropy, listIndexH)

    plotIntervalConfidence(title_r, listRed, ciRed, listMethods, outpath)
    plotIntervalConfidence(title_y, listYellow, ciYellow, listMethods, outpath)
    plotIntervalConfidence(title_b, listBlue, ciBlue, listMethods, outpath)
    plotIntervalConfidence(title_c, listCyan, ciCyan, listMethods, outpath)


args = sys.argv
path = args[1]
dirfile = args[2]
var = args[3:]

# # print(var)
# outpathmeasures = path + dirfile+ '/results/'
# outpathplots = path + '/plots/'
# listFiles = []
# lap = ['_segreg']#, '_red', '_yellow', '_blue', '_cyan']
# for i in range(0, len(var)):
#     listFiles.append(path + var[i] + '/results/tabelas/' + var[i] + lap[0])

# print(listFiles)
# processPlot2(listFiles, outpathmeasures, outpathplots, var)


# print(var)
outpathmeasures = path + dirfile+ '/results/'
outpathplots = path + '/plots/'
lap = ['_red', '_yellow', '_blue', '_cyan']

for j in range(0, 4):
    listFiles = []
    for i in range(0, len(var)):
        listFiles.append(path + var[i] + '/results/tabelas/' + var[i] + lap[j])

        # print(listFiles)
        processPlotColor(listFiles, outpathmeasures, outpathplots, var, lap[j])
