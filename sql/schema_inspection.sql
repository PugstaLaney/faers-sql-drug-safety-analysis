-- ==========================================================
-- FAERS DATABASE SCHEMA INSPECTION
-- ==========================================================

-- List tables in the database
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;


-- Count rows in each table
SELECT COUNT(*) AS demo_rows FROM demo;

SELECT COUNT(*) AS drug_rows FROM drug;

SELECT COUNT(*) AS indi_rows FROM indi;

SELECT COUNT(*) AS outc_rows FROM outc;

SELECT COUNT(*) AS reac_rows FROM reac;

SELECT COUNT(*) AS rpsr_rows FROM rpsr;

SELECT COUNT(*) AS ther_rows FROM ther;


-- Count unique cases
SELECT COUNT(DISTINCT caseid) AS unique_cases
FROM demo;