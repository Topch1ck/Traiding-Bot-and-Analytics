Rus:

# Привет ! 

#### Все скрипты из этой папки показываю одну итерацию для скриптов из папки gridsearch. 
#### Чтобы мы явно могли посмотреть на сделки и проерить их в ручную. 

## Скрипты: 

***simple_strategy*** -> Цель стратегии заключется просто найти просидание цены в X% и на этом падении зайти в лонг на Y%. 

***simple_MACD*** -> Простая стратегия по MACD, вход в лонг сделку на X%, когда линия MACD пересекает сигнальную снизу вверх.  

***macd_solo_logic*** -> Тоже самое что и simple_MACD, но учитывется пересечения только ниже 0 линии. 

***ZL_MACD_solo*** -> Точно также как simple_MACD, но от другого автора "https://ru.tradingview.com/script/kfFN7M7u/" 
Полное название "Zero Lag MACD Enhanced - Version 1.2"
Автор: albert.callisto, "https://ru.tradingview.com/u/albert.callisto/"

***ZL_MACD_with_logic_99pc_solo*** -> Основана на ZL_MACD_solo, но более жесткие  условия фильтрации входа:
- ниже 0 линии 
- Ниже 99 перентиля линии MACD  (ниже чем 99% значений индикатора)

***RSI_solo*** -> Стратегия по RSI, есть значение ниже которого спускаеться индикатор и на возврате когда поднимается выше, мы входим в лонг сделку. Из параметров период и значени этого корридора. 

! Эти скрипты, могут содержать ошибку! При нахождении прошу сообщить.  

===================================================================================================

Eng:

# Hello!

#### I show all the scripts from this folder as one iteration for the scripts from the gridsearch folder.
#### So that we can clearly look at the trades and check them manually.

## Scripts:

***simple_strategy*** -> The goal of the strategy is to simply find a price drop of X% and enter a long at this drop by Y%.

***simple_MACD*** -> A simple strategy for MACD, entering a long trade at X% when the MACD line crosses the signal line from bottom to top.

***macd_solo_logic*** -> The same as simple_MACD, but only crossings below the 0 line are taken into account.

***ZL_MACD_solo*** -> Just like simple_MACD, but from another author "https://ru.tradingview.com/script/kfFN7M7u/"
Full name "Zero Lag MACD Enhanced - Version 1.2"
Author: albert.callisto, "https://ru.tradingview.com/u/albert.callisto/"

***ZL_MACD_with_logic_99pc_solo*** -> Based on ZL_MACD_solo, but stricter entry filtering conditions:
- below 0 line
- Below 99 percentile of MACD line (lower than 99% of indicator values)

***RSI_solo*** -> Strategy based on RSI, there is a value below which the indicator goes down and when it goes back up, we enter a long deal. From the parameters, the period and value of this corridor.

! These scripts may contain an error! If you find it, please let me know.
