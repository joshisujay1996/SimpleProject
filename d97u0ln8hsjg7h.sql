-- Adminer 4.6.3-dev PostgreSQL dump

DROP TABLE IF EXISTS "account";
DROP SEQUENCE IF EXISTS account_id_seq;
CREATE SEQUENCE account_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."account" (
    "id" integer DEFAULT nextval('account_id_seq') NOT NULL,
    "name" character varying NOT NULL,
    "password" character varying,
    CONSTRAINT "account_password_key" UNIQUE ("password"),
    CONSTRAINT "account_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "data";
DROP SEQUENCE IF EXISTS data_id_seq;
CREATE SEQUENCE data_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."data" (
    "id" integer DEFAULT nextval('data_id_seq') NOT NULL,
    "zipcode" integer NOT NULL,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "lat" numeric NOT NULL,
    "long" numeric NOT NULL,
    "population" character varying NOT NULL,
    CONSTRAINT "data_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


-- 2018-07-12 15:40:58.929747+00
