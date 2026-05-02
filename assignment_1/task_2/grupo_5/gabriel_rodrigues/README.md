# Task 2 — Pipeline de Dados (Glue ETL)

## O que foi criado
- Script do Glue ETL (PySpark): `glue_etl_star_schema.py`
- Infra via Terraform (na pasta da Task 1 / `terraform`):
  - Bucket S3 para script e saídas Parquet
  - IAM Role/Policy do Glue
  - Glue Connection (JDBC + VPC)
  - Glue Job
  - Regra de rede no RDS permitindo MySQL **somente** do SG do Glue e do seu `allowed_cidr_blocks` (ex.: seu IP/32)

## Como executar
1) Configure `terraform.tfvars` (copie do `terraform.tfvars.example` e ajuste):
- `db_password`
- `allowed_cidr_blocks = ["SEU_IP_PUBLICO/32"]`

2) Aplique o Terraform na pasta:
- `assignment_1/task_1/grupo_5/gabriel_rodrigues/terraform`

3) No console da AWS Glue, execute o Job (output `glue_job_name`) e aguarde `SUCCEEDED`.

## Como validar (critérios mínimos do enunciado)
- Job com status `SUCCEEDED`
- No bucket S3 (output `task2_s3_bucket`) existem pastas Parquet:
  - `curated/dim_customers/`
  - `curated/dim_products/`
  - `curated/dim_dates/`
  - `curated/dim_countries/`
  - `curated/fact_orders/`
- `fact_orders` contém registros
- O job falha se encontrar qualquer inconsistência de `sales_amount != quantity_ordered * price_each`

