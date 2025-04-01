import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set(palette='bright')
cp = sns.color_palette()

#Đọc dữ liệu
data = pd.read_excel('Messi vs Ronaldo Stat (1).xlsx')
print(data)

# đọc từng sheet
'''df_sheet_name = pd.read_excel('sample.xlsx', sheet_name='sheet2')
print(df_sheet_name)'''

#Hiện thỉ biểu đồ cột từng nhân tố

df_sheet_FactorsStat = pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='Factors Stat')
df_sheet_FactorsStat.columns = df_sheet_FactorsStat.columns.str.strip()
print(df_sheet_FactorsStat)

sns.set(palette='bright')
# sns.set(palette='dark')

df_melt = pd.melt(df_sheet_FactorsStat, id_vars=['Factors'], value_vars=['Messi', 'Ronaldo'], var_name='Player')
plt.figure(figsize = (14, 5))

# create the bar plot
sns.barplot(data=df_melt, x='Factors', y='value', hue='Player', alpha = 1)
sns.despine()

# set the title and axes labels
plt.title('Comparison of Messi and Ronaldo')
plt.xlabel('Factors', fontsize=12)
plt.xticks(rotation = 45, ha = 'right')
plt.ylabel('Values')

plt.show()

#Biểu đồ cột thành tích cá nhân của Messi và Ronaldo theo từng năm

data1=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='All Compitition Exclude Country')
sns.set(palette='bright')
# sns.set(palette='dark')

df_melt = pd.melt(data1, id_vars=['Year'], value_vars=['Messi Games', 'Messi Goals', 'Messi Assists',
                                                       'Ronaldo Games', 'Ronaldo Goals', 'Ronaldo Assists'], var_name='Player')
plt.figure(figsize = (14, 5))

# create the bar plot
sns.barplot(data=df_melt, x='Year', y='value', hue='Player', alpha = 1)
# sns.despine()

# # set the title and axes labels
plt.title('Comparison of Messi and Ronaldo')
plt.xlabel('Factors', fontsize=12)
plt.xticks(rotation = 45, ha = 'right')
plt.ylabel('Values')
plt.legend()
# labels

plt.show()

#Biểu đồ cột hiển thị thành tích world cup của 2 cầu thủ

data2=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='World Cup Stat')
sns.set(palette='bright')
# sns.set(palette='dark')

df_worldcup = pd.melt(data2, id_vars=['Year'], value_vars=['Messi Games', 'Messi Goals', 'Messi Assists',
                                                       ' Ronaldo Games', 'Ronaldo Goals', 'Ronaldo Assists'], var_name='Player')
plt.figure(figsize = (14, 5))

# create the bar plot
sns.barplot(data=df_worldcup, x='Year', y='value', hue='Player', alpha = 1)
 # sns.despine()
# # set the title and axes labels
plt.title('Comparison of Messi and Ronaldo in world cup')
plt.xlabel('Factors', fontsize=12)
plt.xticks(rotation = 45, ha = 'right')
plt.ylabel('Values')
plt.legend()
 # labels =

plt.show()

#Biểu đồ tròn hiển thị tỉ lệ số bàn thắng giữa 2 cầu thủ

df=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='all')
print(df)
# Tính tổng số bàn thắng của Messi và Ronaldo
total_goals = df['Goals'].sum()

# Tính tỷ lệ số bàn thắng của Messi và Ronaldo so với tổng số bàn thắng của cả hai cầu thủ
messi_goals_ratio = df.loc[df['Name'] == 'Messi', 'Goals'].sum() / total_goals
ronaldo_goals_ratio = df.loc[df['Name'] == 'Ronaldo', 'Goals'].sum() / total_goals

# Tạo biểu đồ tròn
labels = ['Messi', 'Ronaldo']
sizes = [messi_goals_ratio, ronaldo_goals_ratio]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # phân cách phần của biểu đồ

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
ax1.axis('equal')
plt.tight_layout()
plt.title('Tỷ lệ số bàn thắng của Messi và Ronaldo')

plt.show()

#Biểu đồ tròn biểu thị tỉ lệ số kiến tạo giữa 2 cầu thủ

df=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='all')
print(df)
# Tính tổng số kiến tạo của Messi và Ronaldo
total_Assists = df['Assists'].sum()

# Tính tỷ lệ số kiến tạo của Messi và Ronaldo so với tổng số kiến tạo của cả hai cầu thủ
messi_Assists_ratio = df.loc[df['Name'] == 'Messi', 'Assists'].sum() / total_Assists
ronaldo_Assists_ratio = df.loc[df['Name'] == 'Ronaldo', 'Assists'].sum() / total_Assists

# Tạo biểu đồ tròn
labels = ['Messi', 'Ronaldo']
sizes = [messi_Assists_ratio, ronaldo_Assists_ratio]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # phân cách phần của biểu đồ

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
ax1.axis('equal')
plt.tight_layout()
plt.title('Tỷ lệ số kiến tạo của Messi và Ronaldo')

plt.show()


#Biểu đồ đường thể hiện bàn thắng của messi và ronaldo trong 5 mùa gần nhất

# Dữ liệu số bàn thắng của Messi và Ronaldo
data1=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='All Compitition Exclude Country')
messi_goals = data1['Messi Goals'][:5]
ronaldo_goals = data1['Ronaldo Goals'][:5]

# Mùa giải tương ứng
seasons=data1.Year[:5]

# Tạo biểu đồ đường
plt.plot(seasons, messi_goals, marker='o', label='Messi')
plt.plot(seasons, ronaldo_goals, marker='o', label='Ronaldo')

# Đặt tên cho các trục và tiêu đề biểu đồ
plt.xlabel('Seasons')
plt.ylabel('Goals')
plt.title('Goals of Messi and Ronaldo by Season')

# Hiển thị chú thích
plt.legend()

# Hiển thị biểu đồ đường
plt.show()

#Biểu đồ đường thể hiện kiến tạo của messi và ronaldo trong 5 mùa gần nhất
# Dữ liệu số kiến tạo của Messi và Ronaldo
data1=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='All Compitition Exclude Country')
messi_Assists = data1['Messi Assists'][:5]
ronaldo_Assists = data1['Ronaldo Assists'][:5]

# Mùa giải tương ứng
seasons=data1.Year[:5]

# Tạo biểu đồ đường
plt.plot(seasons, messi_Assists, marker='o', label='Messi')
plt.plot(seasons, ronaldo_Assists, marker='o', label='Ronaldo')

# Đặt tên cho các trục và tiêu đề biểu đồ
plt.xlabel('Seasons')
plt.ylabel('Assists')
plt.title('Assists of Messi and Ronaldo by Season')

# Hiển thị chú thích
plt.legend()

# Hiển thị biểu đồ đường
plt.show()

#biểu đồ scatter
data1=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='All Compitition Exclude Country')

messi_goals = data1['Messi Goals']
messi_assists = data1['Messi Assists']

ronaldo_goals = data1['Ronaldo Goals']
ronaldo_assists = data1['Ronaldo Assists']

# Tạo biểu đồ scatter giữa số bàn thắng và kiến tạo của 2 cầu thủ
plt.scatter(messi_goals, messi_assists, color='blue', label='Messi')
plt.scatter(ronaldo_goals, ronaldo_assists, color='red', label='Ronaldo')

# Đặt tên cho các trục và tiêu đề biểu đồ
plt.xlabel('Goals')
plt.ylabel('Assists')
plt.title('Goals vs Assists')

# Hiển thị chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()

#Vẽ biểu đồ hiển thi tổng số giải thưởng cá nhân của Messi và Ronaldo

df1=pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='Awards')
messi_award = df1['Messi'].sum()
ronaldo_award = df1['Ronaldo'].sum()

# Tạo biểu đồ cột
x=['Messi', 'Ronaldo']
y=[messi_award,ronaldo_award]

plt.bar(x,y)
# Đặt tiêu đề và nhãn trục
plt.title('Tổng số lượng giải thưởng cá nhân của Messi và Ronaldo')
plt.xlabel('Cầu thủ')
plt.ylabel('Số giải thưởng ')

# Hiển thị biểu đồ
plt.show()


my_palette = {"Messi": "#7D3C98", "Ronaldo": "#3498DB"}
awards = pd.read_excel('Messi vs Ronaldo Stat (1).xlsx', sheet_name='Awards')
awards = awards.iloc[[0,1,2], :]
awards.columns = awards.columns.str.strip()
awards = pd.melt(awards, id_vars='Awards', value_vars=['Messi', 'Ronaldo'], var_name='Player')

plt.figure(figsize=[4,6])

ax = sns.barplot(awards, y='value', x='Awards', hue='Player', palette=my_palette)
for i, bar in enumerate(ax.containers):
    ax.bar_label(bar, label=awards['value'][i])

plt.title('Most important awards')
plt.ylabel('Won')
plt.xticks(rotation=20)
plt.legend(loc='center left')
#plt.ylim(0, 350)
plt.show()

