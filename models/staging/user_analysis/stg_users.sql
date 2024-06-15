WITH user_logs AS(
  SELECT 
    id,
    ref,
    status,
    request,
    response,
    state,
    service,
    created,
    month_created
  FROM {{ ref('stg_user_logs')}}
),

users AS (
  SELECT 
    DISTINCT id,
    ref, 
    "abuja" AS city,
    status,
    COALESCE({{json_extract('u.response', 
      'error, statusCode, message')}},u.response) AS response_error,
    IF (LOWER(service)='9mobile', 'ETISALAT', UPPER(service)) AS type,
    "VTU" AS service,
    DATETIME(created, "Africa/Lagos") AS date, 
    {{json_extract('u.response', 'data.confirmCode')}} AS ext_reference,
    "" AS token,
    COALESCE({{json_extract('u.request', 'recipient')}},
      {{json_extract('u.response', 'data.recipient')}}) AS user_phone,
    COALESCE({{json_extract('u.request', 'amount')}}, 
      {{json_extract('u.response', 'data.amount')}}) AS amount
  FROM user_logs u
  WHERE LOWER(state) IN  ("abuja", "fct") 
    AND LOWER(service) IN ("mtn", "9mobile","glo","airtel") 
    AND {{format_months ('month_created')}} IS NOT NULL
)

SELECT
  id,
  ref,
  city,
  date,
  status,
  type,
  user_phone,
  amount
FROM user_logs