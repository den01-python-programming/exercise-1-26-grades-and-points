import pytest
import src.exercise

def test_exercise():
    input_values = ["-1","25","55","65","79","80","95","105"]
    input_values_stored = ["-1","25","55","65","79","80","95","105"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    assert [output[0],output[1]] == ["Give points [0-100]:","Grade: impossible!"]
    assert [output[2],output[3]] == ["Give points [0-100]:","Grade: failed"]
    assert [output[4],output[5]] == ["Give points [0-100]:","Grade: 1"]
    assert [output[6],output[7]] == ["Give points [0-100]:","Grade: 2"]
    assert [output[8],output[9]] == ["Give points [0-100]:","Grade: 3"]
    assert [output[10],output[11]] == ["Give points [0-100]:","Grade: 4"]
    assert [output[12],output[13]] == ["Give points [0-100]:","Grade: 5"]
    assert [output[14],output[15]] == ["Give points [0-100]:","Grade: incredible!"]
