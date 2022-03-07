from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
from pytest import approx
import pytest
def test_names():
        """Test the chemistry.get_name function."""
        assert get_name("Ac") == "Actinium"
        assert get_name("Ag") == "Silver"
        assert get_name("Al") == "Aluminum"
        assert get_name("Am") == "Americium"
        assert get_name("Ar") == "Argon"
        assert get_name("As") == "Arsenic"
        assert get_name("At") == "Astatine"
        assert get_name("Au") == "Gold"
        assert get_name("B") == "Boron"
        assert get_name("Ba") == "Barium"
        assert get_name("Be") == "Beryllium"
        assert get_name("Bh") == "Bohrium"
        assert get_name("Bi") == "Bismuth"
        assert get_name("Bk") == "Berkelium"
        assert get_name("Br") == "Bromine"
        assert get_name("C") == "Carbon"
        assert get_name("Ca") == "Calcium"
        assert get_name("Cd") == "Cadmium"
        assert get_name("Ce") == "Cerium"
        assert get_name("Cf") == "Californium"
        assert get_name("Cl") == "Chlorine"
        assert get_name("Cm") == "Curium"
        assert get_name("Cn") == "Copernicium"
        assert get_name("Co") == "Cobalt"
        assert get_name("Cr") == "Chromium"
        assert get_name("Cs") == "Cesium"
        assert get_name("Cu") == "Copper"
        assert get_name("Db") == "Dubnium"
        assert get_name("Ds") == "Darmstadtium"
        assert get_name("Dy") == "Dysprosium"
        assert get_name("Er") == "Erbium"
        assert get_name("Es") == "Einsteinium"
        assert get_name("Eu") == "Europium"
        assert get_name("F") == "Fluorine"
        assert get_name("Fe") == "Iron"
        assert get_name("Fl") == "Flerovium"
        assert get_name("Fm") == "Fermium"
def test_atomic_masses():
        """Test the chemistry.get_atomic_mass function."""
        assert get_atomic_mass("Ac") == 227
        assert get_atomic_mass("Ag") == 107.8682
        assert get_atomic_mass("Al") == 26.9815386
        assert get_atomic_mass("Am") == 243
        assert get_atomic_mass("Ar") == 39.948
        assert get_atomic_mass("As") == 74.9216
        assert get_atomic_mass("At") == 210
        assert get_atomic_mass("Au") == 196.966569
def test_parse():
    """Test the chemistry.parse_formula function."""
    assert parse_formula("O3") == ({"O":3})
    assert parse_formula("H2O") == ({"H":2, "O":1})
    assert parse_formula("C6H12O6") == ({"C":6, "H":12, "O":6})
    assert parse_formula("PO4H2(CH2)12CH3") == ({"P":1, "O":4, "H":29, "C":13})
def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    assert molar_mass({"H":2, "O":1}) == 18.01528
    assert molar_mass({"C":6, "H":6}) == approx(78.11184)
    assert molar_mass({"P":1, "O":4, "H":29, "C":13}) == approx(280.34072)
# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=no", "test_chemistry.py"])