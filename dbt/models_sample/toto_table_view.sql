
{{ config(
	materialized="view"
)
}}

WITH _toto_table AS (
 SELECT
 	groupe,
 	sum(qte) as somme
 FROM {{ ref("toto_table_copy") }}
 GROUP BY groupe
)

SELECT * FROM _toto_table