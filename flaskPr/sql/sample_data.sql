drop table test_table;

create table public.test_table(
id serial,
name varchar(128),
age int
);

insert into test_table(name,age)
select 'name'||rn,(random()*80)::int from pg_catalog.generate_series(1,100) as rn;
