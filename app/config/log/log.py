from ornator import FlexibleDualDecorator


class Log(FlexibleDualDecorator):

    def __init__(self):
        super().__init__(locked_pre=self.pre_handler, persistent_pos=self.pos_handler, name_param_response="after_log")

    def pre_handler(self, after_validation: bool = True):
        if after_validation == False: self.persistent_pos = None
        

    def pos_handler(self, after_log):
        pass