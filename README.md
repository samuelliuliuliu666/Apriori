# Apriori Algorithm Implementation
This project aims to implement the Apriori algorithm for association rule mining on the NYPD Hate Crimes dataset. The implementation reads data from a CSV file, generates frequent itemsets and high-confidence association rules as output, and writes the results to a text file.

## Team members

- Ziyu Liu (zl3220)
- Zelin Wang (zw2852)

## Files submitted

1. `proj3.tar.gz`
2. `README.md`
3. `INTEGRATED-DATASET.csv`
4. `example-run.txt`

## How to run the program

1. Set up your Google Cloud VM following the provided instructions.
2. Download the zipped file proj3.tar.gz.
3. Unzip the file
4. Go to the directory where apriori.py is under, and run the folloing commands on your Google Cloud Platform.
   - python apriori.py <input_data> <min_sup> <min_conf>

```sh
python apriori.py INTEGRATED-DATASET.csv 0.1 0.7
```


## Integrated Dataset Description

### Data Sets Used
We used the following NYC Open Data data set to generate the `INTEGRATED-DATASET` file:
- [NYPD Hate Crimes](https://data.cityofnewyork.us/Public-Safety/NYPD-Hate-Crimes/bqiq-cu78)


### Data Mapping Procedure
1. We removed the Full Complaint ID from the original data as we believe they are all unique and would have a low support value. 
2. We also eliminated Month Number, Year Number, and Create Date, assuming that these events occur around the same time. 
3. Additionally, we discarded arrest date and arrest id, as they don't seem to contribute meaningfully to the association rules.

### Justification for Data Set Choices
We excluded the Full Complaint ID from the initial data, considering that each ID is unique and would result in a low support value. Month Number, Year Number, and Create Date were also removed, based on the assumption that these incidents happen in close temporal proximity. Furthermore, we disregarded arrest date and arrest id since they appear to have little relevance to the association rules.

## Internal Design
1. Generate the first large 1 item set using `get_large_1_items`
2. Implemented a method `generate_c` that could generate Candidate set of all large k items by taking the set of all large k-1 items as an input
3. Implemented the Apriori Algorithm in section 2.1.1 in the paper to generate the set of items in all sizes that could potentially give meaningful association rules by the specified thresholds: min support and min confidence using the `apriori` function
4. Generate all association rules in the potential set using the `generate_rules` function


## Compelling Sample Run
### Command line specification for a compelling sample run:
An output file named `output.txt` will be generated containing the frequent itemsets and high-confidence association rules. The format of the output includes the frequent itemsets sorted by support values and the high-confidence association rules sorted by confidence values.

[MISCELLANEOUS PENAL LAW] => [AGGRAVATED HARASSMENT 1] (Conf: 95.48%, Supp: 23.5801%)
This association rule implies that when a record has the attribute "MISCELLANEOUS PENAL LAW," there is a 95.48% confidence (probability) that the record will also have the attribute "AGGRAVATED HARASSMENT 1." The support value of 23.5801% indicates that this rule applies to approximately 23.58% of the total records in the dataset.

In other words, this rule suggests that there is a strong relationship between the presence of "MISCELLANEOUS PENAL LAW" and "AGGRAVATED HARASSMENT 1" attributes in the records. When the law code category is "MISCELLANEOUS PENAL LAW," it is highly likely (with 95.48% confidence) that the crime belongs to "AGGRAVATED HARASSMENT."

[Religion/Religious Practice] => [ANTI-JEWISH] (Conf: 88.37%, Supp: 43.9148%)
This association rule implies that when a record has the attribute "Religion/Religious Practice," there is an 88.37% confidence (probability) that the record will also have the attribute "ANTI-JEWISH." The support value of 43.9148% indicates that this rule applies to approximately 43.91% of the total records in the dataset.

In other words, this rule suggests that there is a strong relationship between the presence of "Religion/Religious Practice" and "ANTI-JEWISH" attributes in the records. Whenever there is an offense categorized as "Religion/Religious Practice", it is very likely that the Bias Motive is "ANTI-JEWISH".


