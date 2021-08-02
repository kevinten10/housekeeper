class ChefScheduler(object):

    def is_done(self):
        return False

    def do_work(self):
        pass


class Chef(object):
    """
    My Chef
    """

    # --- employed

    # chef has a name
    name: str
    # chef working for
    responsibility: str
    # chef pay money to make food
    expenditure: int

    # --- working

    # current working scheduler
    current_scheduler: ChefScheduler

    # the chef birth
    def __init__(self):
        # bring 0 money
        self.expenditure = 0

    # employ the chef
    def employed(self, name: str, responsibility: str):
        self.name = name
        self.responsibility = responsibility

    # give money to chef
    def given_money(self, money: int):
        assert money >= 0
        self.expenditure += money

    # give scheduler to chef
    def given_scheduler(self, scheduler: ChefScheduler):
        self.current_scheduler = scheduler

    def keep_working(self, ):
        # todo chef thread
        while self.current_scheduler.is_done() is False:
            self.current_scheduler.do_work()
