class MyCalendar(object):

    def __init__(self):
        self.list_helper = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if (l < end and r > start for l, r in self.list_helper):
            return False
        self.list_helper.append([start, end])
        return True