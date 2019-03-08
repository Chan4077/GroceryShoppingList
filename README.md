# Computing PT

## Running the code

To run the code, use the `computing_pt_v2.py` file with ideally Python v3.7.

Full code needed to execute the file (copy and paste the following code in your terminal and press enter):

```bash
pip3 install xlwt xlrd # Install needed libraries
python3 computing_pt_v2.py
```

The code above assumes that you're currently in the project's root folder.

## Libraries needed

- [`xlwt`](https://pypi.org/project/xlwt/) for writing Excel files (`.xls`)
- [`xlrd`](https://pypi.org/project/xlrd/) for reading Excel files (`.xls`)

To install the libraries, run the following command:

```bash
pip3 install xlwt xlrd
```

This assumes that you've installed [Python 3](https://python.org/download).

## Spreadsheet template

For an example of how the data should be imported, please see the below code for an example:

```csv
Name,Ability,Gender
Name #1,L/M/H,F/M
```

Column value | Description
---|---
Name | A column of names
Ability | A column of abilities (L: Low, M: Medium, H: High)
Gender | A column of genders (F: Female, M: Male)

Alternatively, see the [mock data CSV file](computing_pt_mock_data_v2.csv) for example.