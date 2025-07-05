+++
title = "plotly.jsのheatmapグラフ"
author = ["K"]
date = 2025-07-05T17:03:01+09:00
lastmod = 2025-07-05T18:26:35+09:00
tags = ["javascript", "plotly.js"]
categories = ["tech"]
draft = false
showtoc = true
+++

<a id="code-snippet--plotly-heatmap"></a>
```html
<div id="plot"></div>

<script>
const x = [0.20403972570131645, 0.4916764106252982, 0.77931309554928]
const y = [0.16395561645008805, 0.4571736709682602, 0.7503917254864324]
const z = [
    [0.0, 0.0, 1.0],
    [1.0, 0.0, 2.0],
    [2.0, 2.0, 2.0]
]

const trace = {
    type: "heatmap",
    x: x,
    y: y,
    z: z,
    colorscale: "Viridis"
}

const layout = {
    title: {text: "heatmap sample"},
    xaxis: {
        title: {
            text: "X",
            font: {size: 24}
        },
        tickfont: {size: 24},
    },
    yaxis: {
        title: {
            text: "Y",
            font: {size: 24}
        },
        tickfont: {size: 24},
    },
}

Plotly.newPlot("plot", [trace], layout);
</script>
```

<div id="plot"></div>

<script>
const x = [0.20403972570131645, 0.4916764106252982, 0.77931309554928]
const y = [0.16395561645008805, 0.4571736709682602, 0.7503917254864324]
const z = [
    [0.0, 0.0, 1.0],
    [1.0, 0.0, 2.0],
    [2.0, 2.0, 2.0]
]

const trace = {
    type: "heatmap",
    x: x,
    y: y,
    z: z,
    colorscale: "Viridis"
}

const layout = {
    title: {text: "heatmap sample"},
    xaxis: {
        title: {
            text: "X",
            font: {size: 24}
        },
        tickfont: {size: 24},
    },
    yaxis: {
        title: {
            text: "Y",
            font: {size: 24}
        },
        tickfont: {size: 24},
    },
}

Plotly.newPlot("plot", [trace], layout);
</script>

python、numpyを使うと二次元ヒストグラムを簡単に作成できる

```python
def heatmap_data():
    x = np.random.random(10).tolist()
    y = np.random.random(10).tolist()
    H, xedges, yedges = np.histogram2d(x, y, bins=(3, 3))

    xcenters = ((xedges[:-1] + xedges[1:]) / 2).tolist()
    ycenters = ((yedges[:-1] + yedges[1:]) / 2).tolist()

    print(xcenters)
    print(ycenters)
    print(H.T.tolist())
```

x, yは実際に使いたいデータにして。
