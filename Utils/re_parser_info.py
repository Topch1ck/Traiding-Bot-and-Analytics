# utils/re_parser_info.py

import re

def extract_symbol_timeframe(path: str):
    """
    Извлекает символ и таймфрейм из имени файла, формата SYMBOL_TIMEFRAME_from_....
    Пример: 'SOLUSDT_4h_from_1_Aug_2020.csv' → ('SOLUSDT', '4h')
    """
    match = re.search(r"([A-Z]+)_(\d+[a-zA-Z])_from", path)
    if match:
        symbol = match.group(1)
        timeframe = match.group(2)
        return symbol, timeframe
    raise ValueError(f"Невозможно извлечь symbol и timeframe из пути: {path}")
