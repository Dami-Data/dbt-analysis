# dbt-analysis
This repository contain transformation of user analysis dbt models.

# Description
The files in this repository are dbt models for differenct purposes.

* Models - are SQL files that define transformations on your raw data. Each model represents a single transformation or analysis step, and dbt compiles these models into SQL queries that are executed against your database.

* Macros - Macros in dbt are reusable pieces of SQL code that can be called within other dbt models, macros, or operations. They are similar to functions in programming languages.

* Sources - Sources in dbt refer to the raw tables and views in your database that you do not control but depend on for your transformations. They provide a way to define and document these raw data assets within your dbt project.

* Marts - Marts, often referred to as data marts, are the final, business-facing tables and views in your data warehouse that are ready for consumption by end users or analytics tools. They typically aggregate and simplify data for specific business domains.

* Staging - Staging refers to the intermediate layer of models in your dbt project that transform raw source data into a format that is easier to work with for subsequent transformations. Staging models are typically used to clean, standardize, and pre-process data before it is further transformed into marts or other business-specific tables.

* Documentation(DOC) - Documentation in dbt is a feature that allows you to add descriptions, metadata, and notes to your models, sources, seeds, and other assets. 

# FILES

* macro files(format_month.sql and json_extract.sql) - they are used to avoid repetition and to encapsulate complex logic that can be reused across multiple models.

* models - core of dbt projects and are used to build derived tables or views from your raw data.

* doc(user_logs.md) - Descriptions and metadata for models, sources, and other dbt assets to provide context and improve understanding.

* marts(user_logs.sql) - End-result/ final business-facing tables/views for end users.

* staging(stg_user_logs.sql, stg_user.sql) - helps to organize your transformation logic into manageable, modular steps. They act as a bridge between raw data sources and final analytical tables (marts).

* seeds: Static data loaded from CSV files.

* update_seeds.py - a python script written to update the seed file and save in csv format.

* sources.yml - Raw data tables/views from external systems.

* dbt_project.yml file is the configuration file for your dbt project. It defines the settings, structure, and behavior of your project. 

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

## Contributors
* Damilola Akinsoju
Feel free to contribute by submitting pull requests or opening issues.
