# RetainIQ — Phase 5 Methodology

I use K-Means to discover customer segments from behavior, value, service adoption, and account
characteristics.

I exclude direct churn outcome fields from the clustering inputs.

Feature engineering includes service count, referral behavior, paperless billing, financial value,
tenure, satisfaction, service usage, contract, internet type, payment method, and offer.

I evaluate candidate k values from 2 through 8 using inertia, silhouette score, cluster-size balance,
and stability across random seeds.

After clustering, I bring churn and revenue back into the segment profiles.

I classify segments using median segment CLTV and median segment churn rate into:
- Protect High-Value
- Maintain Value
- Retention Priority
- Monitor

These labels describe observed segment characteristics and are not clustering inputs.

Customer assignments and segment profiles are published back to MySQL for later Power BI and
GenAI/RAG use.