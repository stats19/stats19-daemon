from typing import Dict, Any, Callable


def extract_dict_value(dict_: Dict[Any, Any], extract_function: Callable[[Dict[Any, Any]], Any],
                       default_value: Any = None) -> Any:
    try:
        field_value = extract_function(dict_)
    except (IndexError, KeyError, TypeError, AttributeError) as e:
        field_value = default_value
    return field_value if field_value is not None else default_value
