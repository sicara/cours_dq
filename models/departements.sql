{{
  config(
    materialized = "table",
  )
}}

SELECT * FROM {{ source('birth_data', 'departements') }}