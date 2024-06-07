Перед запуском скрипта необходимо в терминале установить модули:
=
- pip install pip --upgrade
- pip install pyyaml
- pip install psycopg2
- pip install loguru
- pip install faker


Доступные типы для синтетических данных:
=
|     Имя            | Описание                                                    |
|:------------------:|-------------------------------------------------------------|
| uuid               | ID стрима, команды и т.д.                                   |
| text(100)          | синтетический текст определенной длины (минимум 5 символов) |
| int(0, 434)        | целое число (в скобках min и  max)                          |
| float(0, 4,4)      | десятичное число (в скобках min и  max)                     |
| boolean            | булевое значение (0 или 1)                                  |
| percent            | процентное значение                                         |
| date               | дата                                                        |
| datetime           | дата и время                                                |
| numeric            | число с плавающей запятой (decimal)                         |
| list('', '')       | список значений                                             |
| name               | ФИО                                                         |
| supersprint        | суперспринт                                                 |
| sprint             | спринт                                                      |
| teamid             | ID команды                                                  |
| team               | название команды                                            |
| strimid            | ID стрима                                                   |
| strim              | стрим                                                       |
| departmentid       | ID департамента                                             |
| department         | департамент                                                 |
| infsysid           | ID департамента                                             |
| infsys             | департамент                                                 |
| issuekey           | Issue key                                                   |


>Если в одной таблице присутствует тип синтетических данных teamid и team, strimid и strim или departmentid и department, просьба идентификаторы в yml файле указывать до названий команд, стримов или департаментов, тогда связка id - название будет работать корректно!


Типы данных в PostgreSQL:
=
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