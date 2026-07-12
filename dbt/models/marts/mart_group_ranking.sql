-- Mart: ranking de cada país dentro de su grupo, ordenado por puntos.
-- A diferencia de staging, acá SÍ calculamos algo nuevo (la posición),
-- que no existía como columna en los datos originales.
select
    grupo,
    pais,
    puntos,
    rank() over (partition by grupo order by puntos desc) as posicion_en_grupo
from {{ ref('stg_standings') }}
order by grupo, posicion_en_grupo