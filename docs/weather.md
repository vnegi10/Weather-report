---
theme: [ocean-floor, alt, wide]
toc: false
---

# Weather report for Veldhoven, NL

## Data from [Open-Meteo.com](https://open-meteo.com/)

```js
import {plot_temp, plot_rain} from "./components/plots.js";
```

```js
const temp_forecast = FileAttachment("./data/temp.json").json();
```

```js
const rain_forecast = FileAttachment("./data/rain.json").json();
```

```js
plot_temp(temp_forecast)
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
plot_rain(rain_forecast_dates)
```