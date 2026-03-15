CREATE TABLE faers_severity_dataset AS

WITH drug_base AS (
    SELECT
        primaryid,
        drugname,
        role_cod
    FROM drug
),

reaction_counts AS (
    SELECT
        primaryid,
        COUNT(*) AS n_reactions
    FROM reac
    GROUP BY primaryid
),

drug_counts AS (
    SELECT
        primaryid,
        COUNT(*) AS n_drugs
    FROM drug
    GROUP BY primaryid
),

outcome_flags AS (
    SELECT
        primaryid,

        MAX(CASE WHEN outc_cod = 'DE' THEN 1 ELSE 0 END) AS death_flag,
        MAX(CASE WHEN outc_cod = 'HO' THEN 1 ELSE 0 END) AS hosp_flag,
        MAX(CASE WHEN outc_cod = 'LT' THEN 1 ELSE 0 END) AS life_threat_flag,

        MAX(
            CASE
                WHEN outc_cod IN ('DE','HO','LT','DS')
                THEN 1
                ELSE 0
            END
        ) AS serious_flag

    FROM outc
    GROUP BY primaryid
),

final_dataset AS (

    SELECT
        d.primaryid,
        d.drugname,
        d.role_cod,

        dc.n_drugs,
        rc.n_reactions,

        of.death_flag,
        of.hosp_flag,
        of.life_threat_flag,
        of.serious_flag

    FROM drug_base d

    LEFT JOIN drug_counts dc
        ON d.primaryid = dc.primaryid

    LEFT JOIN reaction_counts rc
        ON d.primaryid = rc.primaryid

    LEFT JOIN outcome_flags of
        ON d.primaryid = of.primaryid
)

SELECT *
FROM final_dataset;