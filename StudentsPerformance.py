import pandas as pd,plotly.figure_factory as pff, statistics as stt, plotly.graph_objects as pgo

data = pd.read_csv("StudentsPerformance.csv")

math = data["math score"].to_list()
reading = data["reading score"].to_list()
writing = data["writing score"].to_list()

mean =     stt.mean(math)
median = stt.median(math)
mode = stt.mode(math)
standard_deviation = stt.stdev(math)

print("mean of height is ", str(mean))
print ( "median = " , str(median))
print("mode = " , str(mode))
print("standard_deviation = " , str(standard_deviation))

first_std_dev_start = mean - standard_deviation
first_std_dev_end = mean + standard_deviation

second_std_dev_start = mean - (2*standard_deviation)
second_std_dev_end = mean + (2*standard_deviation)

Third_std_dev_start = mean - (3*standard_deviation)
Third_std_dev_end = mean + (3*standard_deviation)

list_of_data_within_1_std_deviation = [result for result in math if result>first_std_dev_start and result <first_std_dev_end]
list_of_data_within_2_std_deviation = [result for result in math if result>second_std_dev_start and result <second_std_dev_end]
list_of_data_within_3_std_deviation = [result for result in math if result>Third_std_dev_start and result <Third_std_dev_end]
print ("{}% of data that lies within 1 standard deviation is ". format(len(list_of_data_within_1_std_deviation)*100/len(math)))
print ("{}% of data that lies within 2 standard deviation is ". format(len(list_of_data_within_2_std_deviation)*100/len(math)))
print ("{}% of data that lies within 3 standard deviation is ". format(len(list_of_data_within_3_std_deviation)*100/len(math)))

fig = pff.create_distplot([math],["Height Result"], show_hist=False)
fig.add_trace(pgo.Scatter(x = [mean, mean], y=[0, 0.17], mode= "lines", name = "MEAN"))
fig.add_trace(pgo.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name = "1st Std Dev"))
fig.add_trace(pgo.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name = "1st Std Dev"))
fig.add_trace(pgo.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name = "2nd Std Dev"))
fig.add_trace(pgo.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name = "2nd Std Dev"))
fig.show()