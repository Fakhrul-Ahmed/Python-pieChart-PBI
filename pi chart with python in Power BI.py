# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Bears)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

# import only matplotlib for changing the text size
import matplotlib as mb
mb.rcParams ['font.size']=18.0 # need to define the rc Parameters

# To show the pi chart we need matplotlib and pyplot
import matplotlib.pyplot as plt

# Sheet1 is my data set
# location is to grab the columns
# There are 6 rows, the column name is bears, then I want to make it a list
num = dataset.loc[0:5,'Bears'].tolist()
y = dataset.loc[0:5,'Year'].tolist()

# Bringing numbers rather than percentage
# Dividing the nunmers by 100
# For distribution with the slices we need lambda, create a variable p
# giving format of the number and multiplying percentage (p) with total
# we have to give a comment mark to the below (next) pct
# I can change the floating value
total = sum(num)/100
#pct = lambda p: '{:,.0f}'.format(p*total)
# If the value is a large number then I can devide the total
pct = lambda p: '{:,.1f}'.format(p*total/100)

# Creating data label as percentage, the format is floating up to 0.1 decimal points
# Then pct function is added in plt.pie
#pct = '%0.1f%%'

# Adding preferred colors and inserting it to the plt.pie.
# We can add colors from color pickers also such as #ff6666
colors = ['Skyblue','#ff6666','green','red','lightblue','pink']

# Exploding (Separating) any part
# At first giving zeros to all rows. And then exploding the required one
# Such as one slide is exploded by 0.1 and another one by 0.3
# Then add it in the plt.pie
explode = (0,0.1,0,0,0.3,0)

# Adding shadow to the chart and it is a boolean. Just write it in the plot (plt.pie)

# Now create the chart
plt.pie (num, labels = y, autopct=pct, colors=colors, explode=explode, shadow=True)
plt.show()
