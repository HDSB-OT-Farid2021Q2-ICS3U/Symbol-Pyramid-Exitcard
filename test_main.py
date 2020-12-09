import pytest
import exercise

@pytest.mark.parametrize(
  'num1, result',
  [
    (1, '$\n'),
    (5, '$\n$$\n$$$\n$$$$\n$$$$$\n$$$$\n$$$\n$$\n$\n'),
    (9, '$\n$$\n$$$\n$$$$\n$$$$$\n$$$$$$\n$$$$$$$\n$$$$$$$$\n$$$$$$$$$\n$$$$$$$$\n$$$$$$$\n$$$$$$\n$$$$$\n$$$$\n$$$\n$$\n$\n')
  ]
)

def test_case(capsys, num1, result):
  
  input_values = [num1]
  
  def mock_input(s):
    return input_values.pop(0)
  exercise.input = mock_input
  
  exercise.main()
  out, err = capsys.readouterr()

  assert out == result, 'for an input of {}, the output should be {} instead of {}'.format(input_values, result, out)
  assert err == ''