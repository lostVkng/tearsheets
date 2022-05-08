# Configure

TearSheets is extremely minimal. GET/POST requests allow you to retrieve and add new tearsheets. Deletes/updates should be done from the actual file system. All interaction is done via REST api.

### Create new Saved Sheet
Send POST request to api endpoint with echarts options as json. The url should include the directory and filename of the sheet. 

##### Example:
```shell
POST localhost:8020/sheet/s/econ/gdp
```

##### JSON:
Pass the name of the tearsheet in `name`. `charts` holds echarts option. The `size` attribute is added to each chart to configure the size of the charts. Each row in TearSheet is on a 100 scale, and by setting the size you can configure how many to add to the row.

```json
{
  "name": "test name",
  "charts": [
    {
      "size": 100,
      "option": {
        "title": {
          "text": "Stacked Line"
        },
        "tooltip": {
          "trigger": "axis"
        },
        "legend": {
          "data": [
            "Email",
            "Union Ads",
            "Video Ads",
            "Direct",
            "Search Engine"
          ]
        },
        "grid": {
          "left": "3%",
          "right": "4%",
          "bottom": "3%",
          "containLabel": true
        },
        "xAxis": {
          "type": "category",
          "boundaryGap": false,
          "data": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
          ]
        },
        "yAxis": {
          "type": "value"
        },
        "series": [
          {
            "name": "Email",
            "type": "line",
            "stack": "Total",
            "data": [
              120,
              132,
              101,
              134,
              90,
              230,
              210
            ]
          },
          {
            "name": "Union Ads",
            "type": "line",
            "stack": "Total",
            "data": [
              220,
              182,
              191,
              234,
              290,
              330,
              310
            ]
          },
          {
            "name": "Video Ads",
            "type": "line",
            "stack": "Total",
            "data": [
              150,
              232,
              201,
              154,
              190,
              330,
              410
            ]
          },
          {
            "name": "Direct",
            "type": "line",
            "stack": "Total",
            "data": [
              320,
              332,
              301,
              334,
              390,
              330,
              320
            ]
          },
          {
            "name": "Search Engine",
            "type": "line",
            "stack": "Total",
            "data": [
              820,
              932,
              901,
              934,
              1290,
              1330,
              1320
            ]
          }
        ]
      }
    }
  ]
}
```


### Create new Temporary Sheet
TearSheets saves 20 temporary sheets at a time, they are reachable from the front page. To add to this list, send POST request to api endpoint with echarts options as json. The process is similar to saving a sheet except you do not specify directory/filename, instead just use `/t/new` in the url. 

Example:
```shell
POST localhost:8020/sheet/t/new
```

### Apache ECharts
[Apache ECharts](https://echarts.apache.org/)

ECharts was selected for the large library of charts. The echarts option is passed directly to frontend rendering from TearSheets.
