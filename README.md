# Data Quality Course - dbt Project

This Git repository contains the dbt code for the data quality course at Centrale Supélec.

## Git repository structure

```
├── analyses/           # Analytical SQL files
├── config/
│   └── profiles.yml   # dbt profiles configuration
├── data/              # Raw data files
│   ├── departements.csv
│   ├── dictionnaire_donnees_naissances.csv
│   └── donnees_naissances_2021.csv
├── database/          # DuckDB database files (created at runtime)
├── macros/            # SQL macros for reusable code
├── models/            # dbt models
│   ├── departements.sql
│   ├── donnees_naissances_2021.sql
│   └── schema.yml
├── sample_data/       # Sample/test data
├── seeds/             # CSV files to be loaded as tables
├── snapshots/         # Snapshot models for SCD
├── tests/             # Custom data tests
├── dbt_project.yml    # dbt project configuration
├── packages.yml       # dbt package dependencies
└── pyproject.toml     # Python dependencies managed by uv
```

## Installation and Setup

### Prerequisites
This project uses [uv](https://docs.astral.sh/uv/) for Python dependency management and virtual environment handling.

### Setup Instructions

1. **Install uv** (if not already installed):
   Follow the instructions in the [official documentation](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)

2. **Clone the repository and navigate to the project directory**:
   ```shell
   git clone <repository-url>
   cd cours_dq
   ```

3. **Install Python dependencies**:
   ```shell
   uv sync
   ```

4. **Install dbt packages**:
   ```shell
   uv run dbt deps
   ```

### Database Configuration
Create the database directory and output directory (CSV exports of created tables) with: 
```shell
mkdir database
mkdir output_exports
```

This project uses DuckDB as the data warehouse and the connection configuration is stored in `config/profiles.yml`. The database file will be created automatically in the `database/` directory when you first run dbt. The output created when running a DBT model will be exported as a CSV file in `output_exports`.

## Usage

### Environment Configuration
Export the profiles directory configuration to avoid specifying it in every command:
```shell
export DBT_PROFILES_DIR=config
```

#### Alternative Usage (with explicit profiles directory)
If you prefer not to set the environment variable, you can specify the profiles directory in each command:
```shell
uv run dbt run --profiles-dir config
uv run dbt test --profiles-dir config
```

### Common dbt Commands

- **Debug configuration**: `uv run dbt debug` - Validates your dbt configuration and database connection
- **Compile models**: `uv run dbt compile` - Compiles SQL templates without executing them
- **Run all models**: `uv run dbt run` - Executes all SQL models and creates/updates tables and views in the database
- **Test data quality**: `uv run dbt test` - Runs all defined tests to validate data quality and model assumptions
- **Generate documentation**: `uv run dbt docs generate` - Creates project documentation
- **Serve documentation**: `uv run dbt docs serve` - Serves documentation on a local web server


## Project Overview
This project analyzes French birth data from 2021, focusing on data quality practices and techniques taught in the CentraleSupélec data quality course.

You can explore the data by :
- looking at the data sample : `sample_data/extrait_donnees_naissances_2021.csv`
- adapting the Python script querying the database : `uv run python analyses/explore_database.py`

## Exercises

### Exercise 1 - Add uniqueness and nullable tests

**Task:** Add data quality tests to ensure data integrity
- Add a `unique` test for the `ID` column in the `birth_data_2021` source to ensure each record has a unique identifier
- Add `not_null` tests for critical columns that should never be empty (e.g., `ID`, `SEXE`, `MNAIS`)

**Implementation:** Add these tests to the `models/schema.yml` file under the appropriate column definitions.

### Exercise 2 - Add value range tests

**Task:** Add range validation tests for age columns using the `dbt_utils.accepted_range` test. See data dictionnary for accepted values.

**Implementation:** Use the `dbt_utils.accepted_range` test with `min_value: <MIN>` and `max_value: <MAX>` for each age column.

### Exercise 3 - Add data type tests

**Task:** Add tests to validate year columns (e.g., `ANAIS`, `AMAR`, `ARECC`, `ARECM`, `ARECP`) data type

**Implementation:** Use the appropriate data type test for a year column

**Bonus:** Validate year values using `dbt_utils.accepted_range` with appropriate min/max for year columns

### Exercise 4 - Add relationship test

**Task:** Verify referential integrity between birth data and department reference table

**Implementation:** Use the `relationships` test to ensure foreign key constraints are maintained between the birth data and department reference data.

### Bonus
Based on the results of the tests, create a new model `donnees_naissances_2021_corrected.sql` containing only correct data and run the same tests against it (they should all pass)

## Correction

In this correction, a data exploration script is available: `uv run python analyses/explore_database.py`

Here is the list of tests performed:
- Verification of the uniqueness of the `ID` field
- Verification that the `ANAIS` and `ID` fields are not null
- Verification that the `AMAR` field is indeed an integer
- Verification of the validity of the values taken by `AGEMERE`, `AGEPERE`, `AGEXACTM`, `AGEXACTP`
- Verification of the validity of the `DEPDOM` foreign key

## Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
