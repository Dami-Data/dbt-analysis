{{
    config(
        materialized ='incremental',
        on_schema_change='fail',
        partition_by ={
            'field': 'created',
            'data_type': 'timestamp',
            'granularity': 'day'
        },
        cluster_by=['type']
    )
}}

WITH users AS(
  SELECT *
  FROM {{ ref('stg_users')}}
)
SELECT 
 date,
 amount,
 state,
 type,
 id,
 user_phone,
 ref
FROM users

{% if is_incremental() %}
WHERE
    date > (SELECT MAX(date) FROM {{ this }})
{% endif %}