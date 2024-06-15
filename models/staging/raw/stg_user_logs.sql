WITH user_logs AS(
  SELECT *
  FROM {{source('data_source','user_logs')}}
)

SELECT
  id,
  ref,
  action,
  status,
  state,
  created,
  service,
  request,
  response,
  month_created

FROM user_logs