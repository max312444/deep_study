from typing import Sequence

# Sequence -> Type hinting -> list, tuple, range
x_seq_int:Sequence[int] = [1, 2, 3]
x_seq_int = (1, 2, 3)
# x_seq_int = {1, 2, 3} # Error
# x_seq_int = {1:2, 3:4} # Error