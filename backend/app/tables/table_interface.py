from abc import abstractmethod


class InterfaceTable:
    @abstractmethod
    async def pull(self):
        pass
    