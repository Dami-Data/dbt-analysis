{% macro json_extract(json, paths) %}
  CASE
    {% for path in paths.split(',') %}
      WHEN JSON_EXTRACT_SCALAR({{ json }}, '$.{{ path }}') IS NOT NULL
        THEN JSON_EXTRACT_SCALAR({{ json }}, '$.{{ path }}')
    {% endfor %}
    ELSE NULL
  END
{% endmacro %}