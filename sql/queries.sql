-- Query 1: Top 5 Fund Houses by Total AUM
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;
-- Query 2: Average NAV by Fund
SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;
-- Query 3: Monthly Average NAV
SELECT
    substr(date,1,7) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
-- Query 4: Total Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;
-- Query 5: Funds with Expense Ratio Less Than 1%
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
-- Query 6: Average SIP Amount
SELECT
    ROUND(AVG(amount_inr),2) AS average_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP';
-- Query 7: Transaction Type Distribution
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;
-- Query 8: Top 10 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;
-- Query 9: Investors by KYC Status
SELECT
    kyc_status,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status;
-- Query 10: Portfolio Allocation by Sector
SELECT
    sector,
    SUM(weight_pct) AS total_weight
FROM fact_holdings
GROUP BY sector
ORDER BY total_weight DESC;