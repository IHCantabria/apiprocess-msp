class Result(object):
    RESULT_OK = "OK"
    RESULT_FAIL = "ERROR"

    def __init__(self, status, msg, value):

        self.status = status
        self.msg = msg
        self.value = value

    def to_json(self):
        return {"status": self.status, "msg": self.msg, "value": self.value}
