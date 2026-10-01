# План изучения SQL для аналитики данных

Углубление знаний · 1 час в день · ~14 недель
Уровень на старте: средний (JOIN, GROUP BY) → цель: уверенный SQL для data analyst

---

## Фаза 1 · Продвинутые запросы (недели 1–3)

Оконные функции и рекурсивные CTE — база для любой аналитики.

**Темы:**
- [ ] Оконные функции: ROW_NUMBER, RANK, DENSE_RANK
- [ ] LAG / LEAD, NTILE, скользящие агрегаты (running total, moving average)
- [ ] PARTITION BY в связке с ORDER BY — типовые аналитические паттерны
- [ ] CTE (WITH), в том числе рекурсивные CTE
- [ ] Практика: 10+ задач на StrataScratch или LeetCode (раздел Database)

**Материалы:**
- [Mode SQL Tutorial (аналитические кейсы)](https://mode.com/sql-tutorial/)
- [LearnSQL — курс Window Functions](https://learnsql.com/course/window-functions/)
- [Window Functions Cheat Sheet](https://learnsql.com/blog/window-functions-cheat-sheet/)

---

## Фаза 2 · Оптимизация запросов (недели 4–6)

Понимание того, как СУБД выполняет запрос, и как его ускорить.

**Темы:**
- [ ] Индексы: типы (B-tree, hash), когда индекс не используется
- [ ] EXPLAIN / EXPLAIN ANALYZE — чтение планов выполнения
- [ ] Оптимизация JOIN'ов, порядок соединений, антипаттерны
- [ ] Партиционирование таблиц, материализованные представления
- [ ] Практика: найти и ускорить 3–5 медленных запросов (свои или учебные)

**Материалы:**
- [PostgreSQL docs — EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html)
- [Use The Index, Luke (индексы простыми словами)](https://use-the-index-luke.com/)
- [EnterpriseDB — разбор EXPLAIN ANALYZE на примере](https://www.enterprisedb.com/blog/postgresql-query-optimization-performance-tuning-with-explain-analyze)

---

## Фаза 3 · Моделирование данных (недели 7–9)

От OLTP-мышления к схемам, заточенным под аналитику.

**Темы:**
- [ ] Нормализация vs денормализация — когда что уместно
- [ ] Star schema и Snowflake schema, факты и измерения
- [ ] Основы ETL/ELT: где и как трансформировать данные
- [ ] Работа с датами и временными зонами в аналитических запросах
- [ ] Практика: спроектировать схему для учебного датасета (например, продажи)

**Материалы:**
- [Kimball Group — основы star schema](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)
- [dbt — ETL vs ELT](https://www.getdbt.com/blog/etl-vs-elt)
- [SQLBolt — практика по схемам и JOIN](https://sqlbolt.com/)

---

## Фаза 4 · Продвинутая агрегация и инструменты (недели 10–12)

Сложная агрегация плюс связка SQL с Python/BI-инструментами.

**Темы:**
- [ ] PIVOT / условная агрегация (CASE WHEN внутри SUM/COUNT)
- [ ] Статистические функции: percentile_cont, stddev, corr
- [ ] Связка SQL + Python (pandas.read_sql) для дальнейшего анализа
- [ ] Основы работы с BI-инструментом (Power BI, Metabase или Tableau) поверх SQL
- [ ] Практика: мини-проект — от сырых данных до дашборда

**Материалы:**
- [Pandas docs — read_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
- [Microsoft Learn — Power BI (бесплатные модули)](https://learn.microsoft.com/ru-ru/training/powerplatform/power-bi)
- [Kaggle — открытые датасеты для практики](https://www.kaggle.com/datasets)

---

## Фаза 5 · Портфолио и собеседования (недели 13+)

Упаковка навыков в проекты и подготовка к техническим интервью.

**Темы:**
- [ ] 1–2 полноценных pet-проекта на реальных открытых датасетах
- [ ] Оформить проекты на GitHub с описанием и SQL-скриптами
- [ ] Решить 30+ задач по SQL-собеседованиям (StrataScratch, LeetCode, DataLemur)
- [ ] Разобрать типовые вопросы: window functions, JOIN-логика, оптимизация
- [ ] Провести 1–2 мок-собеседования (с другом или на профильной платформе)

**Материалы:**
- [StrataScratch — задачи под реальные интервью](https://www.stratascratch.com/)
- [LeetCode — раздел Database](https://leetcode.com/studyplan/sql/)
- [DataLemur — SQL-вопросы с разбором по компаниям](https://datalemur.com/)
