import pytest
import exercise

@pytest.mark.parametrize(
  'num1, result',
  [
    (5, '7'),
  ]
)

def test_case(capsys, num1, result):
  
  input_values = [num1]
  
  def mock_input(s):
    return input_values.pop(0)
  exercise.input = mock_input
  
  exercise.main()
  out, err = capsys.readouterr()
  out = out.replace('\n', '')

  assert out == result, 'for an input of {}, the output should be {} instead of {}'.format(input_values, result, out)
  assert err == ''