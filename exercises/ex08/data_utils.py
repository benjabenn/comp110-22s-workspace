"""Dictionary related utility functions."""

__author__ = "730518701"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(input_data_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Return a smaller sample of column based data with an inputted number of rows."""
    result: dict[str, list[str]] = {}

    for column_names in input_data_table:
        data_column: list[str] = []
        i: int = 0
        while i < num_rows and i < len(input_data_table[column_names]):
            data_column.append(input_data_table[column_names][i])
            i += 1
        result[column_names] = data_column

    return result


def select(input_data_table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Returns only the selected columns given by str in a list from a given table into another table."""
    result: dict[str, list[str]] = {}

    for column_names in input_data_table:
        if column_names in selected_columns:
            result[column_names] = input_data_table[column_names]

    return result


def concat(first_data_table: dict[str, list[str]], second_data_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column based tables into one without mutation."""
    result: dict[str, list[str]] = {}

    for first_columns in first_data_table:
        result[first_columns] = first_data_table[first_columns]

    for second_columns in second_data_table:
        if second_columns in result:
            for values in second_data_table[second_columns]:
                result[second_columns].append(values)
        else:
            result[second_columns] = second_data_table[second_columns]
    
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """This function takes a list of str and counts the occurrences of all items in a list, assigning each item as the key in a new dict and the count as its associated value."""
    result: dict[str, int] = {}

    for items in input_list:
        if items in result:
            result[items] += 1
        else:
            result[items] = 1

    return result


def average(input_data_table: dict[str, list[str]]) -> dict[str, float]:
    """This function returns the average of all the items in each column into a new dictionary with only one value for each key."""
    result: dict[str, float] = {}

    for items in input_data_table:
        average_value: float = 0.0
        for values in input_data_table[items]:
            average_value += float(values)
        average_value /= len(input_data_table[items])
        result[items] = average_value

    return result