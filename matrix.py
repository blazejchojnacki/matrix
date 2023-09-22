ITERATION_START = 1


class Entries(list):
    """creates a free-form matrix based on given entries"""
    def __init__(self, entries):
        super().__init__()
        self.number_of_rows = len(entries)
        self.number_of_columns = len(entries[0])
        for row_number in range(self.number_of_rows):
            self.append(entries[row_number])
        self.determinant = self.get_determinant()
    # def input_from_console(self):
    # def input_from_file(self, filepath):

    def display(self):
        """returns the matrix after printing it, formatted"""
        matrix = display(self)
        return matrix

    def transpose(self):
        """ returns the matrix, transposed"""
        matrix = transpose(self)
        return matrix

    def get_submatrix(self, skipped_row, skipped_column):
        """ returns the submatrix of the matrix, given the skipped row and column """
        matrix = get_submatrix(self, skipped_row, skipped_column)
        return matrix

    def get_determinant(self):
        """ returns the determinant of the matrix"""
        self.determinant = get_determinant(self)
        return self.determinant

    def inverse(self):
        """ returns the inverse of the matrix """
        matrix = inverse(self)
        return matrix

    def scale(self, scalar):
        """ returns the matrix multiplied by a given scalar """
        matrix = scale(scalar, self)
        return matrix

    def add(self, matrix_added):
        """ returns the sum of the matrix and a given matrix """
        matrix_sum = add(self, matrix_added)
        return matrix_sum

    def multiply(self, matrix_multiplying):
        """ returns the product of the matrix and a given matrix """
        matrix_product = multiply(self, matrix_multiplying)
        return matrix_product


class Identity(Entries):
    """ creates a square identity matrix of given column or row length """
    def __init__(self, size):
        self.number_of_rows = int(size)
        self.number_of_columns = int(size)
        entries = []
        for row_number in range(self.number_of_rows):
            entries.append([])
            for column_number in range(self.number_of_columns):
                if row_number == column_number:
                    entries[row_number].append(1)
                else:
                    entries[row_number].append(0)
        super().__init__(entries)
        self.determinant = 1


def display(matrix):
    """ returns a given matrix after printing it to the console """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for row_number in range(number_of_rows):
        line = "|\t"
        for column_number in range(number_of_columns):
            line += f"{matrix[row_number][column_number]}\t"
        print(f"{line}|")
    print()
    return matrix


def transpose(matrix):
    """ returns the given matrix transposed """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    transposed = []
    for column_number in range(number_of_columns):
        transposed.append([])
        for row_number in range(number_of_rows):
            transposed[column_number].append(matrix[row_number][column_number])
    transposed_matrix = Entries(transposed)
    return transposed_matrix


def get_submatrix(matrix, skipped_row, skipped_column):
    """ returns the submatrix of a provided matrix, given the skipped row and column """
    number_of_rows = len(matrix) - 1
    number_of_columns = len(matrix[0]) - 1
    sub_entries = []
    skip_row = 0
    for row_number in range(number_of_rows):
        if row_number + ITERATION_START == skipped_row:
            skip_row = 1
        sub_entries.append([])
        skip_column = 0
        for column_number in range(number_of_columns):
            if column_number + ITERATION_START == skipped_column:
                skip_column = 1
            sub_entries[row_number].append(matrix[row_number + skip_row][column_number + skip_column])
    submatrix = Entries(sub_entries)
    return submatrix


def get_determinant(matrix):
    """ returns the determinant of a given matrix """
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    if number_of_rows == number_of_columns:
        if number_of_rows == 1:
            determinant = matrix[0][0]
        else:
            determinant = 0
            for column_number in range(number_of_columns):
                submatrix = get_submatrix(matrix, 0 + ITERATION_START, column_number + ITERATION_START)
                determinant += (-1) ** column_number * matrix[0][column_number] * get_determinant(submatrix)
        return determinant


def inverse(matrix):
    """ returns the inverse of a given matrix """
    determinant = get_determinant(matrix)
    if determinant != 0:
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])
        inverted = []
        for row_number in range(number_of_rows):
            inverted.append([])
            for column_number in range(number_of_columns):
                submatrix = get_submatrix(matrix, row_number + ITERATION_START, column_number + ITERATION_START)
                inverted[row_number].append(get_determinant(submatrix) / determinant)
                if inverted[row_number][column_number] % 1 == 0:
                    inverted[row_number][column_number] = int(inverted[row_number][column_number])
                inverted[row_number][column_number] *= (-1) ** (row_number + column_number)
        inverse_matrix = transpose(Entries(inverted))
        return inverse_matrix


def scale(scalar, matrix):
    """ returns the given matrix multiplied by a given scalar """
    number_of_rows = len(matrix)
    scaled = []
    for row_number in range(number_of_rows):
        row = matrix[row_number]
        scaled.append([term * scalar for term in row])
    scaled_matrix = Entries(scaled)
    return scaled_matrix


def add(matrix_a, matrix_b):
    """ returns the sum-matrix of two given matrices """
    number_of_rows_a = len(matrix_a)
    number_of_columns_a = len(matrix_a[0])
    number_of_rows_b = len(matrix_b)
    number_of_columns_b = len(matrix_b[0])
    if number_of_rows_a == number_of_rows_b and number_of_columns_a == number_of_columns_b:
        result = []
        for row_number in range(number_of_rows_a):
            result.append([])
            for column_number in range(number_of_columns_a):
                result[row_number].append(matrix_a[row_number][column_number] + matrix_b[row_number][column_number])
        sum_matrix = Entries(result)
        return sum_matrix


def multiply(matrix_a, matrix_b):
    """ returns the product-matrix of two given matrices """
    number_of_rows_a = len(matrix_a)
    number_of_columns_a = len(matrix_a[0])
    number_of_rows_b = len(matrix_b)
    number_of_columns_b = len(matrix_b[0])
    if number_of_columns_a == number_of_rows_b:
        product = []
        for row_number_a in range(number_of_rows_a):
            product.append([])
            for column_number_b in range(number_of_columns_b):
                product[row_number_a].append(0)
                for column_number_a in range(number_of_columns_a):
                    row_number_b = column_number_a
                    product[row_number_a][column_number_b] += (matrix_a[row_number_a][column_number_a]
                                                               * matrix_b[row_number_b][column_number_b])
        product_matrix = Entries(product)
        return product_matrix
