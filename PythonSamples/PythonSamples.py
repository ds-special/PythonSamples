import Pmf
import matplotlib.pyplot as pyplot
import myplot

def main(name, data_dir='.'):
    hist = Pmf.MakeHistFromList([1, 2, 2, 3, 5])
    print(hist.Freq(2))

    myplot.Hist(hist)
    myplot.Show()

    #vals, freqs = hist.Render()
    #rectangles = pyplot.bar(vals, freqs)
    #pyplot.show()    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
