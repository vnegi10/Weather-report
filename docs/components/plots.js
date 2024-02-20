import * as Plot from "npm:@observablehq/plot";
import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

export function plot_temp(temp_forecast, {width} = {}) {

    return Plot.plot({
      width,
      title: "Hourly temperature forecast",
      x: {type: "utc", ticks: "day", label: "Time [days]"},
      y: {grid: true, inset: 10, label: "Degrees (C)"},
      marks: [
        Plot.lineY(temp_forecast, {
          x: "time",
          y: "temp",
          stroke: "red",
          }),
        Plot.lineY(temp_forecast, {
          x: "time",
          y: "app_temp",
          stroke: "blue",
          }),
        Plot.text(temp_forecast, Plot.selectLast({
          x: "time",
          y: "temp",
          text: "legend_1",
          textAnchor: "middle",
          dx: 10,
          fontSize: 12
        })),
        Plot.text(temp_forecast, Plot.selectLast({
          x: "time",
          y: "app_temp",
          text: "legend_2",
          textAnchor: "middle",
          dx: 10,
          fontSize: 12
        }))
      ]
    });

}

export function plot_rain(rain_forecast_dates, {width} = {}) {

  return Plot.plot({
    width,
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
  });

}