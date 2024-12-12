{{
  config(
    materialized = "table",
  )
}}

SELECT * FROM {{ source('birth_data', 'birth_data_2021') }}