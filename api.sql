create schema oobabooga;
create table oobabooga.api (
  id bigserial primary key,
  prompt text not null,
  result text not null,
  model jsonb not null,
  params jsonb not null,
  response jsonb not null,
  created_at timestamp with time zone not null default now(),
  updated_at timestamp with time zone not null default now()
);

-- vim: set et ff=unix ft=sql nocp sts=2 sw=2 ts=2:
