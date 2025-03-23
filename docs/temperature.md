---
theme: dashboard
toc: false
---

# Temperature (Veldhoven, NL)

## Data from [Open-Meteo.com](https://open-meteo.com/)

```js
import {plot_temp} from "./components/plots.js";
```

```js
const temp_forecast = FileAttachment("./data/temp.json").json();
```

<!--- Re-render whenever the container resizes --->
<div class="grid grid-cols-1">
    <div class="card">${resize((width) => plot_temp(temp_forecast, {width}))} </div>
</div>