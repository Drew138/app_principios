class Controlador:
    jwt = ""
    refresh = ""

    @classmethod
    def setJWT(cls, jwt):
        cls.jwt = jwt

    @classmethod
    def getJWT(cls):
        return cls.jwt

    @classmethod
    def setRefresh(cls, refresh):
        cls.refresh = refresh

    @classmethod
    def getRefresh(cls):
        return cls.refresh
