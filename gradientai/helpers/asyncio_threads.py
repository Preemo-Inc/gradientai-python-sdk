"""Python 3.8 backward compatible - High-level support for working with threads in asyncio

Code attribution, PSF compatible license:
https://github.com/python/cpython/blob/956023826a393b5704d3414dcd01f1bcbeaeda15/Lib/asyncio/threads.py#L12
"""
__all__ = ["to_thread"]


try:
    # works for python 3.9+
    from asyncio import to_thread
except ImportError:
    # fix for python 3.8 and below:
    import functools
    import contextvars
    from asyncio import events
    async def to_thread(func, /, *args, **kwargs):
        loop = events.get_running_loop()
        ctx = contextvars.copy_context()
        func_call = functools.partial(ctx.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, func_call)