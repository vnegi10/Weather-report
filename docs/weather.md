# Weather report for Veldhoven, NL

## Data from [Open-Meteo.com](https://open-meteo.com/)

```js
const temp_forecast = FileAttachment("./data/temp.json").json();
```

```js
const rain_forecast = FileAttachment("./data/rain.json").json();
```

```js
display(
  Plot.plot({
    title: "Hourly temperature forecast",
    x: {type: "utc", ticks: "day", label: "Time [days]"},
    y: {grid: true, label: "Degrees (C)"},
    marks: [
      Plot.lineY(temp_forecast, {
        x: "time",
        y: "temp",
        stroke: "red"
        })
    ]
  })
);
```

```js
// Convert x-axis to Date object so that we make a bar plot later
var rain_forecast_dates
rain_forecast_dates = rain_forecast.map(({time, ...rest}) => {
  return {
    time: new Date(time),
    ...rest
  };
})
```

```js
display(
  Plot.plot({
    title: "Hourly rain forecast",
    x: {label: "Time [days]"},
    y: {grid: true, label: "Rain [mm]"},
    marks: [
      Plot.rectY(rain_forecast_dates, {
        x: "time",
        interval: d3.utcHour,
        y: "rain",
        fill: "green"
        })
    ]
  })
);
```