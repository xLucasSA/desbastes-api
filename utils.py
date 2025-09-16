from typing import List, Dict
from math import floor
from structures import DataSitio

async def process_desbaste_for_sitio(dataSitio: List[DataSitio], percent: float) -> Dict:
    """
    Process desbaste calculation for a single sitio
    """
    sum_items = 0
    checkeds = {}

    # Create a dictionary for listed values, ignoring null values
    for item in dataSitio:
        diameter = item.get("diameter")
        freq = item.get("freq")

        if diameter and freq:
            if diameter not in checkeds:
                checkeds[diameter] = 0
            checkeds[diameter] += freq
            sum_items += freq

    # Convert dictionary to a list of tuples and sort by diameter
    new_data = sorted(list(checkeds.items()), key=lambda x: x[0])

    quant_remove = floor(sum_items * (percent / 100))
    sum_items_final = sum_items - quant_remove

    results = []
    
    # Generate final result
    for diameter, freq in new_data:
        result = {
            'diameter': diameter,
            'ft': freq
        }

        if quant_remove < result['ft']:
            result['fd'] = -quant_remove
            quant_remove = 0
        else:
            result['fd'] = -result['ft']
            quant_remove -= result['ft']

        result['fr'] = result['ft'] + result['fd']
        results.append(result)

    sitio_result = {
        'results': results,
        'final_items': sum_items_final,
        'quant_remove': floor(sum_items * (percent / 100))
    }
    
    return sitio_result