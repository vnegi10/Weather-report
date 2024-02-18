# Weather report

```js
const forecast = FileAttachment("./data/temp.json").json();
```

```js
display(forecast)
```

```js
display(
  Plot.plot({
    title: "Hourly temperature forecast",
    x: {type: "utc", ticks: "day", label: "Time [days]"},
    y: {grid: true, label: "Degrees (C)"},
    marks: [
      Plot.lineY(forecast, {
        x: "time",
        y: "temp",
        stroke: "red"
        })
    ]
  })
);
```