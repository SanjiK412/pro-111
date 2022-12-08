import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random
data = pd.read_csv("medium_data.csv")
dataList = data["sample2.csv"].tolist()

populationMean = statistics.mean(dataList)
print("Population Mean:",populationMean)

def random_mean_set(counter):
  dataSet = []
  for i in range(0,counter):
    random_index = random.randint(0,len(dataList))
    value = dataList[random_index]
    dataSet.append(value)
  mean = statistics.mean(dataSet)
  return mean

def show_fig(mean_list):
  figData = mean_list
  fig = ff.create_distplot([df],["temp"],show_hist = False)
  fig.show()
  
  samplingMean = statistics.mean(meanList)
  sd = statistics.stdev(meanList)
  
  sd1_str,sd1_end = samplingMean - sd,samplingMean + sd
  sd2_str,sd2_end = samplingMean - (2*sd),samplingMean + (2*sd)
  sd3_str,sd3_end = samplingMean - (3*sd),samplingMean + (3*sd)
  
  print("Standard Deviation 1:",sd1_str,",",sd1_end)
  print("Standard Deviation 2:",sd2_str,",",sd2_end)
  print("Standard Deviation 3:",sd3_str,",",sd3_end)

  #plotting the graph with traces
  fig = ff.create_distplot([mean_list],["reading_list"],show_hist = False)
  fig.add_trace(go.Scatter(x = [sd1_str,sd1_str],y = [0,0.17], mode="lines", name="mean"))
  fig.add_trace(go.Scatter(x = [sd1_end,sd1_end],y = [0,0.17], mode="lines", name="mean"))
  fig.add_trace(go.Scatter(x = [sd2_str,sd2_str],y = [0,0.17], mode="lines", name="mean"))
  fig.add_trace(go.Scatter(x = [sd2_end,sd2_end],y = [0,0.17], mode="lines", name="mean"))
  fig.add_trace(go.Scatter(x = [sd3_str,sd3_str],y = [0,0.17], mode="lines", name="mean"))
  fig.add_trace(go.Scatter(x = [sd3_end,sd3_end],y = [0,0.17], mode="lines", name="mean"))


  fig.add_trace(go.Scatter(x = [samplingMean,samplingMean],y = [0,0.8]))
  sampleMean = statistics.mean(dataList)
  fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.8]))
  
  zTest = (sampleMean - samplingMean)/sd
  print("Z Test:",zTest)

  fig.show()
