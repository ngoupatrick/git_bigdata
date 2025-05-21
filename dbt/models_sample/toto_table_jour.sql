{{ config(
	materialized="table"
)
}}

WITH _toto_table AS (
 SELECT
 	jour,
 	sum(qte) as somme
 FROM {{ ref("toto_table_copy") }}
 GROUP BY jour
)

SELECT * FROM _toto_table