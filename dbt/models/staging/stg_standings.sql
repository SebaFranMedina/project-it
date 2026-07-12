select
    id,
    pais,
    puntos,
    mundial,
    grupo
from {{ source('raw', 'standings') }}


