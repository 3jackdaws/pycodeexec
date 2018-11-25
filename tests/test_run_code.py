import pytest
from pycodeexec import Runner
import time
from pycodeexec.util import time_this


def test_run_python_code():
    python = None
    with time_this("Startup"):
        python = Runner("python")

    with time_this("Exec"):
        output = python.get_output("print('hello')")


@pytest.mark.asyncio
async def test_run_async_code():
    from pycodeexec.asyncio import Runner
    python = None
    with time_this("Startup"):
        python = Runner("python")

    with time_this("Exec"):
        output = await python.get_output("print('hello')")