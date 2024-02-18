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
display(
  Plot.plot({
    title: "Hourly rain forecast",
    x: {type: "utc", ticks: "day", label: "Time [days]"},
    y: {grid: true, label: "Rain [mm]"},
    marks: [
      Plot.lineY(rain_forecast, {
        x: "time",
        y: "rain",
        stroke: "white"
        })
    ]
  })
);
```