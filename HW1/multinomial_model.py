from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("--data", type=str, default=None,
                    help="the path of data file.")
parser.add_argument("--m", type=int, default=None,
                    help="the level of multinomial")
parser.add_argument("--d", type=int, default=None,
                    help="dimensions of data")
parser.add_argument("--n", type=int, default=None,
                    help="the amount of data")
args = parser.parse_args()




class multinomial_model():
    def __init__(self,m,d,n): #m is the level of multinomial，d is dimensions of data，n is the amount of data
        self.m = m
        self.d = d
        self.n = n

        self.P0 = 0
        self.P = [None]*m
        for i in range(len(self.P)):
            self.P[i] = [0]*d

        self.X = [None]*n
        for i in range(len(self.X)):
            self.X[i] = [0]*d

        self.Y = [0]*n
    def data_input(self,dir):
        with open(dir, "r") as f:
            line_n = 0                  #代表维度
            for line in f.readlines():
                line = line.strip('\n').split()  # 去掉列表中每一个元素的换行符
                if line[0]=='x':
                    for i in range(len(self.X)):
                        self.X[i][line_n] = line[i+1]
                elif line[0]=='y':
                    self.Y = line[1:]
                line_n = line_n + 1
    def show_data(self):
        print("X:")
        print(self.X)

        print("Y:")
        print(self.Y)
    def algorithm(self):
        pass

def main():
    model = multinomial_model(args.m,args.d,args.n)
    model.data_input(args.data)
    model.show_data()


if __name__ == '__main__':
    main()
