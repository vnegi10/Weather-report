---
theme: dashboard
toc: false
---

# Rain (Veldhoven, NL)

## Data from [Open-Meteo.com](https://open-meteo.com/)

```js
import {plot_rain} from "./components/plots.js";
```

```js
const rain_forecast = FileAttachment("./data/rain.json").json();
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

<div class="grid grid-cols-1">
    <div class="card">${resize((width) => plot_rain(rain_forecast_dates, {width}))} </div>
</div>