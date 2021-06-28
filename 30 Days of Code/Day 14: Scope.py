class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        output_list = []
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                diff = abs(self.__elements[i]-self.__elements[j])
                output_list.append(diff)
                
        self.maximumDifference = max(output_list)
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
