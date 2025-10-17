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
This project uses DuckDB as the data warehouse and the connection configuration is stored in `config/profiles.yml`. The database file will be created automatically in the `database/` directory when you first run dbt.

## Usage

### Environment Configuration
Export the profiles directory configuration to avoid specifying it in every command:
```shell
export DBT_PROFILES_DIR=config
```

### Common dbt Commands

- **Run all models**: `uv run dbt run` - Executes all SQL models and creates/updates tables and views in the database
- **Test data quality**: `uv run dbt test` - Runs all defined tests to validate data quality and model assumptions
- **Compile models**: `uv run dbt compile` - Compiles SQL templates without executing them
- **Debug configuration**: `uv run dbt debug` - Validates your dbt configuration and database connection
- **Generate documentation**: `uv run dbt docs generate` - Creates project documentation
- **Serve documentation**: `uv run dbt docs serve` - Serves documentation on a local web server

### Alternative Usage (with explicit profiles directory)
If you prefer not to set the environment variable, you can specify the profiles directory in each command:
```shell
uv run dbt run --profiles-dir config
uv run dbt test --profiles-dir config
```


## Project Overview
This project analyzes French birth data from 2021, focusing on data quality practices and techniques taught in the Centrale Supélec data quality course.

## Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
