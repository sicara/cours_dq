{% test value_in_range(model, column_name, min_value, max_value) %}

SELECT *
FROM {{ model }}
WHERE {{ column_name }} < {{ min_value }}
   OR {{ column_name }} > {{ max_value }}
{% endtest %}