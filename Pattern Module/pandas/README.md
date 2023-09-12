# Pandas
```python
import pandas as pd
print(pd.__version__)
```

    2.1.0
    


```python
db=pd.DataFrame()
print(db)
```

    Empty DataFrame
    Columns: []
    Index: []
    


```python
data=['Abhinav','Singh','Anushka']
df=pd.DataFrame(data)
print(df)
```

             0
    0  Abhinav
    1    Singh
    2  Anushka
    


```python
data=[['Rahul', 35], ['vasu' , 8]]
df =pd.DataFrame(data,columns=['Name','Age'])
df['Age'] = df['Age'].astype(float)
print(df)
```

        Name   Age
    0  Rahul  35.0
    1   vasu   8.0
    


```python
data={'Name':['Abhinav','Anushka','Vishal'],'Age':[20,22,19]}
df=pd.DataFrame(data)
print(df)
```

          Name  Age
    0  Abhinav   20
    1  Anushka   22
    2   Vishal   19
    


```python
data=[{'a':1,'b':2},{'a':7,'b':8,'c':9}]
df =pd.DataFrame(data)
print(df)
```

       a  b    c
    0  1  2  NaN
    1  7  8  9.0
    


```python
db=pd.read_json('data.json')
print(db)
```

        Duration  Pulse  Maxpulse  Calories
    0         60    110       130       409
    1         60    117       145       479
    2         60    103       135       340
    3         45    109       175       282
    4         45    117       148       406
    5         60    102       127       300
    6         55    105       155       355
    7         45    120       145       245
    8         50    117       150       350
    9         55     98       155       455
    10        55    111       155       255
    

### Tail Function & reading CSV


```python
db=pd.read_csv('nyc_weather.csv')
print(db.tail(10))#To Get only 10 details
```

              EST  Temperature  DewPoint  Humidity  Sea Level PressureIn  \
    21  1/22/2016           26         6        41                 30.21   
    22  1/23/2016           26        21        78                 29.77   
    23  1/24/2016           28        11        53                 29.92   
    24  1/25/2016           34        18        54                 30.25   
    25  1/26/2016           43        29        56                 30.03   
    26  1/27/2016           41        22        45                 30.03   
    27  1/28/2016           37        20        51                 29.90   
    28  1/29/2016           36        21        50                 29.58   
    29  1/30/2016           34        16        46                 30.01   
    30  1/31/2016           46        28        52                 29.90   
    
        VisibilityMiles  WindSpeedMPH PrecipitationIn  CloudCover    Events  \
    21                9           NaN            0.01           3      Snow   
    22                1          16.0            2.31           8  Fog-Snow   
    23                8           6.0               T           3      Snow   
    24               10           3.0               0           2       NaN   
    25               10           7.0               0           2       NaN   
    26               10           7.0               T           3      Rain   
    27               10           5.0               0           1       NaN   
    28               10           8.0               0           4       NaN   
    29               10           7.0               0           0       NaN   
    30               10           5.0               0           0       NaN   
    
        WindDirDegrees  
    21              34  
    22              42  
    23             327  
    24             286  
    25             244  
    26             311  
    27             234  
    28             298  
    29             257  
    30             241  
    


```python
db.columns
for _ in db.columns:
    print(_)
```

    EST
    Temperature
    DewPoint
    Humidity
    Sea Level PressureIn
    VisibilityMiles
    WindSpeedMPH
    PrecipitationIn
    CloudCover
    Events
    WindDirDegrees
    


```python
db.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 31 entries, 0 to 30
    Data columns (total 11 columns):
     #   Column                Non-Null Count  Dtype  
    ---  ------                --------------  -----  
     0   EST                   31 non-null     object 
     1   Temperature           31 non-null     int64  
     2   DewPoint              31 non-null     int64  
     3   Humidity              31 non-null     int64  
     4   Sea Level PressureIn  31 non-null     float64
     5   VisibilityMiles       31 non-null     int64  
     6   WindSpeedMPH          28 non-null     float64
     7   PrecipitationIn       31 non-null     object 
     8   CloudCover            31 non-null     int64  
     9   Events                9 non-null      object 
     10  WindDirDegrees        31 non-null     int64  
    dtypes: float64(2), int64(6), object(3)
    memory usage: 2.8+ KB
    


```python
print(db['EST'].tail(10))
print(type(db['EST']))
```

    21    1/22/2016
    22    1/23/2016
    23    1/24/2016
    24    1/25/2016
    25    1/26/2016
    26    1/27/2016
    27    1/28/2016
    28    1/29/2016
    29    1/30/2016
    30    1/31/2016
    Name: EST, dtype: object
    <class 'pandas.core.series.Series'>
    


```python
print(db['Temperature'].max())
```

    50
    


```python
print(db[['Temperature','EST','Events']][db['Temperature']==db['Temperature'].max()])
```

       Temperature        EST Events
    9           50  1/10/2016   Rain
    


```python
print(db.shape)
```

    (31, 11)
    

### Describe Function


```python
db.describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temperature</th>
      <th>DewPoint</th>
      <th>Humidity</th>
      <th>Sea Level PressureIn</th>
      <th>VisibilityMiles</th>
      <th>WindSpeedMPH</th>
      <th>CloudCover</th>
      <th>WindDirDegrees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>31.000000</td>
      <td>31.000000</td>
      <td>31.000000</td>
      <td>31.000000</td>
      <td>31.000000</td>
      <td>28.000000</td>
      <td>31.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>34.677419</td>
      <td>17.838710</td>
      <td>51.677419</td>
      <td>29.992903</td>
      <td>9.193548</td>
      <td>6.892857</td>
      <td>3.129032</td>
      <td>247.129032</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.639315</td>
      <td>11.378626</td>
      <td>11.634395</td>
      <td>0.237237</td>
      <td>1.939405</td>
      <td>2.871821</td>
      <td>2.629853</td>
      <td>92.308086</td>
    </tr>
    <tr>
      <th>min</th>
      <td>20.000000</td>
      <td>-3.000000</td>
      <td>33.000000</td>
      <td>29.520000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>29.000000</td>
      <td>10.000000</td>
      <td>44.500000</td>
      <td>29.855000</td>
      <td>9.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
      <td>238.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>35.000000</td>
      <td>18.000000</td>
      <td>50.000000</td>
      <td>30.010000</td>
      <td>10.000000</td>
      <td>6.500000</td>
      <td>3.000000</td>
      <td>281.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>39.500000</td>
      <td>23.000000</td>
      <td>55.000000</td>
      <td>30.140000</td>
      <td>10.000000</td>
      <td>8.000000</td>
      <td>4.500000</td>
      <td>300.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.000000</td>
      <td>46.000000</td>
      <td>78.000000</td>
      <td>30.570000</td>
      <td>10.000000</td>
      <td>16.000000</td>
      <td>8.000000</td>
      <td>345.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
db.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EST</th>
      <th>Temperature</th>
      <th>DewPoint</th>
      <th>Humidity</th>
      <th>Sea Level PressureIn</th>
      <th>VisibilityMiles</th>
      <th>WindSpeedMPH</th>
      <th>PrecipitationIn</th>
      <th>CloudCover</th>
      <th>Events</th>
      <th>WindDirDegrees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2016</td>
      <td>38</td>
      <td>23</td>
      <td>52</td>
      <td>30.03</td>
      <td>10</td>
      <td>8.0</td>
      <td>0</td>
      <td>5</td>
      <td>NaN</td>
      <td>281</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2016</td>
      <td>36</td>
      <td>18</td>
      <td>46</td>
      <td>30.02</td>
      <td>10</td>
      <td>7.0</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>275</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2016</td>
      <td>40</td>
      <td>21</td>
      <td>47</td>
      <td>29.86</td>
      <td>10</td>
      <td>8.0</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>277</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2016</td>
      <td>25</td>
      <td>9</td>
      <td>44</td>
      <td>30.05</td>
      <td>10</td>
      <td>9.0</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>345</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2016</td>
      <td>20</td>
      <td>-3</td>
      <td>41</td>
      <td>30.57</td>
      <td>10</td>
      <td>5.0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>333</td>
    </tr>
  </tbody>
</table>
</div>



## 11-09-23
#### ETL- Extract, Transfer and Load 
#### PDA
1. Mobile App
2. PC, etc
* Data warehouses



```python
db.to_csv('abhinav.csv',index=False)
```

### Pandas Group By


```python
db=pd.read_csv('weather_data_cities.csv')
print(db)
```

             day      city  temperature  windspeed   event
    0   1/1/2017  new york           32          6    Rain
    1   1/2/2017  new york           36          7   Sunny
    2   1/3/2017  new york           28         12    Snow
    3   1/4/2017  new york           33          7   Sunny
    4   1/1/2017    mumbai           90          5   Sunny
    5   1/2/2017    mumbai           85         12     Fog
    6   1/3/2017    mumbai           87         15     Fog
    7   1/4/2017    mumbai           92          5    Rain
    8   1/1/2017     paris           45         20   Sunny
    9   1/2/2017     paris           50         13  Cloudy
    10  1/3/2017     paris           54          8  Cloudy
    11  1/4/2017     paris           42         10  Cloudy
    


```python
g=db.groupby('city')
for city,city_dataframe in g:
    print(city)
    print("data frame of city is ")
    print(city_dataframe)
```

    mumbai
    data frame of city is 
            day    city  temperature  windspeed  event
    4  1/1/2017  mumbai           90          5  Sunny
    5  1/2/2017  mumbai           85         12    Fog
    6  1/3/2017  mumbai           87         15    Fog
    7  1/4/2017  mumbai           92          5   Rain
    new york
    data frame of city is 
            day      city  temperature  windspeed  event
    0  1/1/2017  new york           32          6   Rain
    1  1/2/2017  new york           36          7  Sunny
    2  1/3/2017  new york           28         12   Snow
    3  1/4/2017  new york           33          7  Sunny
    paris
    data frame of city is 
             day   city  temperature  windspeed   event
    8   1/1/2017  paris           45         20   Sunny
    9   1/2/2017  paris           50         13  Cloudy
    10  1/3/2017  paris           54          8  Cloudy
    11  1/4/2017  paris           42         10  Cloudy
    


```python
getG=g.get_group('mumbai')
print(getG)
```

            day    city  temperature  windspeed  event
    4  1/1/2017  mumbai           90          5  Sunny
    5  1/2/2017  mumbai           85         12    Fog
    6  1/3/2017  mumbai           87         15    Fog
    7  1/4/2017  mumbai           92          5   Rain
    


```python
getG.to_csv('mumbar weather.csv',index=False)
```


```python
g.head(2)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>city</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>new york</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>new york</td>
      <td>36</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2017</td>
      <td>mumbai</td>
      <td>90</td>
      <td>5</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/2/2017</td>
      <td>mumbai</td>
      <td>85</td>
      <td>12</td>
      <td>Fog</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/1/2017</td>
      <td>paris</td>
      <td>45</td>
      <td>20</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1/2/2017</td>
      <td>paris</td>
      <td>50</td>
      <td>13</td>
      <td>Cloudy</td>
    </tr>
  </tbody>
</table>
</div>




```python
g.describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">temperature</th>
      <th colspan="8" halign="left">windspeed</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mumbai</th>
      <td>4.0</td>
      <td>88.50</td>
      <td>3.109126</td>
      <td>85.0</td>
      <td>86.50</td>
      <td>88.5</td>
      <td>90.50</td>
      <td>92.0</td>
      <td>4.0</td>
      <td>9.25</td>
      <td>5.057997</td>
      <td>5.0</td>
      <td>5.00</td>
      <td>8.5</td>
      <td>12.75</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>4.0</td>
      <td>32.25</td>
      <td>3.304038</td>
      <td>28.0</td>
      <td>31.00</td>
      <td>32.5</td>
      <td>33.75</td>
      <td>36.0</td>
      <td>4.0</td>
      <td>8.00</td>
      <td>2.708013</td>
      <td>6.0</td>
      <td>6.75</td>
      <td>7.0</td>
      <td>8.25</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>paris</th>
      <td>4.0</td>
      <td>47.75</td>
      <td>5.315073</td>
      <td>42.0</td>
      <td>44.25</td>
      <td>47.5</td>
      <td>51.00</td>
      <td>54.0</td>
      <td>4.0</td>
      <td>12.75</td>
      <td>5.251984</td>
      <td>8.0</td>
      <td>9.50</td>
      <td>11.5</td>
      <td>14.75</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>



### Concatenate Data frames


```python
india_weather=pd.DataFrame({'city': ['hydrabad', 'banglore', 'pune'], 'humidity': [80,60,78],'temprature': [33,28,40],})

print(india_weather)
```

           city  humidity  temprature
    0  hydrabad        80          33
    1  banglore        60          28
    2      pune        78          40
    


```python
us_weather=pd.DataFrame({'city': ['newyork', 'washington', 'arizona'], 'humidity': [75,86,70],'temprature': [30,36,34],})

print(us_weather)
```

             city  humidity  temprature
    0     newyork        75          30
    1  washington        86          36
    2     arizona        70          34
    


```python
df=pd.concat([india_weather,us_weather],ignore_index=True)
print(df)
```

             city  humidity  temprature
    0    hydrabad        80          33
    1    banglore        60          28
    2        pune        78          40
    3     newyork        75          30
    4  washington        86          36
    5     arizona        70          34
    


```python
temp_df=pd.DataFrame({
    'city':['Hyderabad', 'Banglore','Pune'],
    'temperature':[30,28,35]
    
})
humidity_df=pd.DataFrame({
    'city':['Hyderabad', 'Banglore','Chennai'],
    'humidity':[63,78,70]
    
})
print(temp_df)
print(humidity_df)
```

            city  temperature
    0  Hyderabad           30
    1   Banglore           28
    2       Pune           35
            city  humidity
    0  Hyderabad        63
    1   Banglore        78
    2    Chennai        70
    

#### Natural Join


```python
df=pd.merge(humidity_df,temp_df,on='city')
print(df)
```

            city  humidity  temperature
    0  Hyderabad        63           30
    1   Banglore        78           28
    

#### left outer join


```python
df=pd.merge(humidity_df,temp_df,on='city',how='left')
print(df)
```

            city  humidity  temperature
    0  Hyderabad        63         30.0
    1   Banglore        78         28.0
    2    Chennai        70          NaN
    

#### Right Outer Join


```python
df=pd.merge(humidity_df,temp_df,on='city',how='right')
print(df)
```

            city  humidity  temperature
    0  Hyderabad      63.0           30
    1   Banglore      78.0           28
    2       Pune       NaN           35
    

#### use of loc and iloc


```python
s=pd.Series(list('abcde'),index=[49,48,47,0,1])
print(s)
print(s.loc[49])
print(s.iloc[0])
```

    49    a
    48    b
    47    c
    0     d
    1     e
    dtype: object
    a
    a
    


