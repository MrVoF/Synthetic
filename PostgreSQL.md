|                    Имя                    |      Псевдонимы      | Описание                                              |
|:-----------------------------------------:|:--------------------:|-------------------------------------------------------|
|                  boolean                  |         bool         | логическое значение (true/false)                      |
|             character [ (n) ]             |     char [ (n) ]     | символьная строка фиксированной длины                 |
|         character varying [ (n) ]         |   varchar [ (n) ]    | символьная строка переменной длины                    |
|                   date                    |                      | календарная дата (год, месяц, день)                   |
|             double precision              |        float8        | число двойной точности с плавающей точкой (8 байт)    |
|                  integer                  |      int, int4       | знаковое четырёхбайтное целое                         |
|            numeric [ (p, s) ]             |  decimal [ (p, s) ]  | вещественное число заданной точности                  |
|                   real                    |        float4        | число одинарной точности с плавающей точкой (4 байта) |
|                   text                    |                      | символьная строка переменной длины                    |
|    time [ (p) ] [ without time zone ]     |                      | время суток (без часового пояса)                      |
|        time [ (p) ] with time zone        |        timetz        | время суток с учётом часового пояса                   |
|  timestamp [ (p) ] [ without time zone ]  |                      | дата и время (без часового пояса)                     |
|     timestamp [ (p) ] with time zone      |     timestamptz      | дата и время с учётом часового пояса                  |
|                   uuid                    |                      | универсальный уникальный идентификатор                |