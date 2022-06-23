import main as main
from unittest.mock import Mock
import pytest
import sys
from _pytest.capture import CaptureFixture

CANNOT_ENTER:str = "can not enter in this time\n"

def test_case_1(capfd:CaptureFixture):
    inputs = Mock(side_effect=['8','30','14','00'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == "cost 80\n"

def test_case_2(capfd:CaptureFixture):
    inputs = Mock(side_effect=['5'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == CANNOT_ENTER

def test_case_3(capfd:CaptureFixture):
    inputs = Mock(side_effect=['21'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == CANNOT_ENTER

def test_case_4(capfd:CaptureFixture):
    inputs = Mock(side_effect=['8','00'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == CANNOT_ENTER

def test_case_5(capfd:CaptureFixture):
    inputs = Mock(side_effect=['8','5','10','5'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == "cost 0\n"

def test_case_6(capfd:CaptureFixture):
    inputs = Mock(side_effect=['12','50','23','22'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == "cost 680\n"

def test_case_7(capfd:CaptureFixture):
    inputs = Mock(side_effect=['12','0','10','00'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == "cost 900\n"

def test_case_8(capfd:CaptureFixture):
    inputs = Mock(side_effect=['20','49','7','0'])
    setattr(main,'input',inputs)
    main.main()
    out,err = capfd.readouterr()
    assert out == "cost 680\n"