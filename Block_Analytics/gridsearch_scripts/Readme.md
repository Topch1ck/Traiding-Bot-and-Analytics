Rus:

# Привет ! 

#### Скрипты из этой папки это продолжение из папки solo_scripts, но уже 
#### в формате gridsearch где мы перебираем тысячи комбинаций параметров, 
#### чтобы опрделить наилучший вариант. 

Еще раз по стратегиям которые тут проверяем. 

## Скрипты: 

***imple_strategy_calculations*** -> ***simple_strategy*** -> Цель стратегии заключется просто найти просидание цены в X% и на этом падении зайти в лонг на Y%. 

***calculation_simple_MACD*** -> ***simple_MACD*** -> Простая стратегия по MACD, вход в лонг сделку на X%, когда линия MACD пересекает сигнальную снизу вверх.  

***calc_MACD_with_logic*** -> ***macd_solo_logic*** -> Тоже самое что и simple_MACD, но учитывется пересечения только ниже 0 линии. 

***ZL_MACD_gridsearch*** -> ***ZL_MACD_solo*** -> Точно также как simple_MACD, но от другого автора "https://ru.tradingview.com/script/kfFN7M7u/" 
Полное название "Zero Lag MACD Enhanced - Version 1.2"
Автор: albert.callisto, "https://ru.tradingview.com/u/albert.callisto/"

***ZeroLag_MACD_with_logic_99perc*** -> ***ZL_MACD_with_logic_99pc_solo*** -> Основана на ZL_MACD_solo, но более жесткие  условия фильтрации входа:
- ниже 0 линии 
- Ниже 99 перентиля линии MACD  (ниже чем 99% значений индикатора)

***RSI_gridsearch*** -> ***RSI_solo*** -> Стратегия по RSI, есть значение ниже которого спускаеться индикатор и на возврате когда поднимается выше, мы входим в лонг сделку. Из параметров период и значени этого корридора. 

# ! Эти скрипты, могут содержать ошибку! При нахождении прошу сообщить.  

===================================================================================================

Eng:

# Hello!

#### The scripts in this folder are a continuation of the solo_scripts folder, but already in the gridsearch format, where we go through thousands of parameter combinations,
#### to determine the best option.

#### Once again on the strategies that we test here.

## Scripts:

***imple_strategy_calculations*** -> ***simple_strategy*** -> The goal of the strategy is to simply find a price drop of X% and enter long at this drop by Y%.

***calculation_simple_MACD*** -> ***simple_MACD*** -> Simple strategy for MACD, entering a long deal at X%, when the MACD line crosses the signal line from the bottom up.

***calc_MACD_with_logic*** -> ***macd_solo_logic*** -> The same as simple_MACD, but only crossings below the 0 line are taken into account.

***ZL_MACD_gridsearch*** -> ***ZL_MACD_solo*** -> Same as simple_MACD, but from another author "https://ru.tradingview.com/script/kfFN7M7u/"
Full name "Zero Lag MACD Enhanced - Version 1.2"
Author: albert.callisto, "https://ru.tradingview.com/u/albert.callisto/"

***ZeroLag_MACD_with_logic_99perc*** -> ***ZL_MACD_with_logic_99pc_solo*** -> Based on ZL_MACD_solo, but more stringent entry filtering conditions:
- below 0 line
- Below 99 percentile of MACD line (below 99% of indicator values)

***RSI_gridsearch*** -> ***RSI_solo*** -> Strategy for RSI, there is a value below which the indicator goes down and when it goes back up, we enter a long deal. From the parameters, the period and value of this corridor.

# ! These scripts may contain an error! If found, please report it.