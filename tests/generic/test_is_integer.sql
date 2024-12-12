{% test is_integer(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE TRY_CAST({{ column_name }} AS INT) IS NULL
  AND {{ column_name }} IS NOT NULL
{% endtest %}