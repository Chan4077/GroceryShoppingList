# Computing PT

## Running the code

To run the code, use the `computing_pt_v2.py` file.

Alternatively, use the GitHub version on https://github.com/Chan4077/computing-pt.

## Libraries needed

- [`xlwt`](https://pypi.org/project/xlwt/) for writing Excel files (`.xls`)
- [`xlrd`](https://pypi.org/project/xlrd/) for reading Excel files (`.xls`)

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