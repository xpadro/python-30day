from algorithms.other.excel_column_number import ExcelColumn

def test_resolve_column():
    excel = ExcelColumn()

    assert excel.resolve("A") == 1
    assert excel.resolve("B") == 2
    assert excel.resolve("Z") == 26
    assert excel.resolve("AA") == 27
    assert excel.resolve("AB") == 28
    assert excel.resolve("AZ") == 52
    assert excel.resolve("BA") == 53
    assert excel.resolve("ZY") == 701
    assert excel.resolve("AAA") == 703
