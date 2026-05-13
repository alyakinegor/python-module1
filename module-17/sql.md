# база данных
`create`

создает таблицу

```
create table employees (id serial primary key, 
name text not null,
salary numeric)
```

`table`

указывает что создается\изменяется таблицу

```
create table departments (id serial primary key, 
name text)
```

`alter`

изменяет сущуствующий обьект

```
create table departments (id serial primary key, 
name text)
```

`add`

добавляет колонку, ограничения

```
alter table employees
add column phone text
```

`drop`

удаляет обьект

```
drop table projects
```

`if exists`

проверяет наличие
```
drop table if exists old_projects
```

`rename`

переименовывает обьект

```
alter table employees
rename column name to full_name
```

`TRUNCATE`

изменяет сущуствующий обьект

```
truncate table employees
```

## 2.Работа с данными
`select`

выбирает данные 

```
select name, salary from employees
```

`from`

указывает источник данных

```
select * from employees
```

`insert`

добавляет строки

```

INSERT INTO departmnets(name)
values ('it'), ('hr)
```