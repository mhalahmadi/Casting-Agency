--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Actors" (
    id integer NOT NULL,
    name character varying(120),
    age character varying(120),
    gender character varying(120)
);


ALTER TABLE public."Actors" OWNER TO postgres;

--
-- Name: Actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Actors_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actors_id_seq" OWNER TO postgres;

--
-- Name: Actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Actors_id_seq" OWNED BY public."Actors".id;


--
-- Name: Movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Movies" (
    id integer NOT NULL,
    title character varying(120),
    relase_date timestamp without time zone
);


ALTER TABLE public."Movies" OWNER TO postgres;

--
-- Name: Movies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Movies_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movies_id_seq" OWNER TO postgres;

--
-- Name: Movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Movies_id_seq" OWNED BY public."Movies".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: Actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors" ALTER COLUMN id SET DEFAULT nextval('public."Actors_id_seq"'::regclass);


--
-- Name: Movies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movies" ALTER COLUMN id SET DEFAULT nextval('public."Movies_id_seq"'::regclass);


--
-- Data for Name: Actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Actors" (id, name, age, gender) FROM stdin;
2	Emma Roberts	29	Female
4	Will Smith	51	Male
5	Will Smith	51	Male
6	Jason Bateman	50	Male
7	Jennifer Aniston	51	Female
3	Will Smith	52	Male
9	tota	16	female
10	Emma Roberts	29	Female
11	tota	16	female
12	Emma Roberts	29	Female
\.


--
-- Data for Name: Movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Movies" (id, title, relase_date) FROM stdin;
1	Wild Child	2012-10-01 12:12:12
2	Life Of Crime	2012-10-01 12:12:12
4	New Wild Child	2012-10-01 12:12:12
5	Hancock	2012-10-01 12:12:12
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Name: Actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Actors_id_seq"', 12, true);


--
-- Name: Movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Movies_id_seq"', 5, true);


--
-- Name: Actors Actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors"
    ADD CONSTRAINT "Actors_pkey" PRIMARY KEY (id);


--
-- Name: Movies Movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movies"
    ADD CONSTRAINT "Movies_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- PostgreSQL database dump complete
--

