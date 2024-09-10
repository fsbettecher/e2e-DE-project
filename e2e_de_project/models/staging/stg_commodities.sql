-- import

WITH source AS (
    SELECT
        "Date",
        "Close",
        "symbol"
    FROM
        {{ source ('e2e_de_project', 'commodities')  }}
),

-- renamed

renamed AS (
    SELECT
        cast("Date" as date) as "data",
        "Close" as "Closure_value",
        symbol
    FROM
        source
)

-- select * from

SELECT * FROM renamed