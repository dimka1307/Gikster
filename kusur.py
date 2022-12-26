def main(k):
    import numpy as np
    x1=0
    x2=0
    x5=0
    v = [x1,x2,x5]
    x5 = np.fix(k/5)
    k = k-x5*5
    if k==0:
        k=0
    else:
        x2 = np.fix(k/2)
        k=k-x2*2
        if k==0:
            k=0
        else:
            x1 = np.fix(k/1)
    v=[int(x1),int(x2),int(x5)]
    return v

if __name__ == "__main__":
    main()