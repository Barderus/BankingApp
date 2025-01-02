class Customer:
    """
        Customer class that represents a customer object
    """

    def __init__(self, name, acc_num, exp_date, cv, acc_type):
        """
            Constructor __init__ that accepts the following arguments:
                name : String --> Customer name
                acc_num : String --> Bank Account number
                exp_date : String --> Account expire date
                cv : String --> Security code
                acc_type : String --> Account type
        """
        self.__name = name
        self.__acc_num = acc_num
        self.__exp_date = exp_date
        self.__cv = cv
        self.__acc_type = acc_type

    # Setters and getters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def acc_num(self):
        return self.__acc_num

    @acc_num.setter
    def acc_num(self, acc_num):
        self.__acc_num = acc_num

    @property
    def exp_date(self):
        return self.__exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        self.__exp_date = exp_date

    @property
    def cv(self):
        return self.__cv

    @cv.setter
    def cv(self, cv):
        self.__cv = cv

    @property
    def type(self):
        return self.__acc_type

    @type.setter
    def type(self, acc_type):
        self.__acc_type = acc_type

    def __str__(self):
        display_str = (f"Account type: {self.__acc_type}\nAccount Number: {self.__acc_num}"
                       f"\nValid Thru: {self.__exp_date}\tSec code: {self.__cv}\n\t{self.__name}")
        return display_str