from jina import DocumentArray, Executor, requests


class MyExecutor98(Executor):
    """"""
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        pass