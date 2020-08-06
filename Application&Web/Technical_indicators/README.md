### Трендовые индикаторы
|Индикатор|Ф/О|Название|Части|
|:---:    |:---|:---:|:---:|
|MACD|:white_check_mark::white_check_mark:|Moving Average Convergence Divergence|`MACD_fast (ema)`, `MACD_signal (ema)` |
|MA|:white_check_mark::negative_squared_cross_mark:|Moving Averages|`EMA`, `SMA`|
|MM|:white_check_mark::negative_squared_cross_mark:|MINMAX|`MIN_Volume`, `MAX_Volume`|
|KAMA|:white_check_mark::negative_squared_cross_mark:|Adaptive Moving Average|`EMA (2~30)`|
|Trix|:white_check_mark::white_check_mark:|Triple Exponential Moving Average|`EMA(EMA)`|
|SR|:white_check_mark::white_check_mark:|Stochastic Oscillator|`%K`, `%D (SMA)`|
|WR|:white_check_mark::white_check_mark:|Williams percent range|`%R`|
|RSI|:white_check_mark::white_check_mark:|Relative Strength Index|`%RSI (avgM)`|
|AO|:white_check_mark::white_check_mark:|Aroon Oscillator|`%Aroon Up (period)`, `%Aroon Down (period)`|
|SAR|:white_check_mark::negative_squared_cross_mark:|Parabolic Stop And Reverse|`dots under trend`|
|ROC|:white_check_mark::white_check_mark:|Rate of Change|`%ROC (line)`|
|Momentum|:white_check_mark::white_check_mark:|Momentum|`%momentum (line)`|
|CCI|:white_check_mark::white_check_mark:|Commodity Channel Index|`line (sma/avg)`|
|ADX|:white_check_mark::white_check_mark:|Average Directional Movement Index|`%line (ema)`|
|MFI|:white_check_mark::white_check_mark:|Money Flow Index|`%line (TP*Volume)`|
|Ichimoku Cloud|:white_check_mark::negative_squared_cross_mark:|Ichimoku kinkou-hyou|`turning_line [9]`, `standard_line [26]`, `ichimoku_span1 [26]`, `ichimoku_span2 [26 of 52]`, `chikou_span (close[-22])`|



###  Индикаторы волатильности
|Индикатор|Ф/О|Название|Части|
|:---:    |:---|:---:|:---:|
|BB|:white_check_mark::negative_squared_cross_mark:|Bollinger Bands |`BB_Middle (avg)`, `BB_Upper (avg+std)`, `BB_Lower (avg-std)`|
|AB|:white_check_mark::negative_squared_cross_mark:|Acceleration Bands|`AB_Middle (sma)`, `AB_Upper (sma)`, `AB_Lower (sma)`|
|KC|:white_check_mark::negative_squared_cross_mark:|Keltner Channel|`KC_Middle sma(TP)`, `KC_Upper sma(TP+TR)`, `KC_Lower sma(TP-TR)`|
|ATR|:white_check_mark::white_check_mark:|Normalized Average True Range|`~%~ATR sma(TrueRange)`|

## Индикаторы связанные с объёмом
|Индикатор|Ф/О|Название|Части|
|:---:    |:---|:---:|:---:|
|PVT|:white_check_mark::white_check_mark:|Price Volume Trend |`%pvt (line)`|
|CMF|:white_check_mark::white_check_mark:|Chaikin Money Flow  |`line`|
|VWAP|:white_check_mark::negative_squared_cross_mark:|Volume Weighted Average Price|`line (based on cumsum)`|
|OBV|:white_check_mark::white_check_mark:|On-Balance Volume|`line (based on cumsum volume)`|


### Виды графиков
|График|Смысл|
|:-----|:---:|
|OHLC|  столбиковый график, показывает `open  high low close` 1 свечи|
