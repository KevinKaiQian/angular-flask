import sys
import six

class StockException(Exception):
    """Base Nova Exception

    To correctly use this class, inherit from it and define
    a 'msg_fmt' property. That msg_fmt will get printf'd
    with the keyword arguments provided to the constructor.

    """
    msg_fmt ="An unknown exception occurred."
    code = 500
    headers = {}
    safe = False

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass

        if not message:
            try:
                message = self.msg_fmt % kwargs

            except Exception:
                exc_info = sys.exc_info()
                # kwargs doesn't match a variable in the message
                # log the issue and the kwargs
                
                for name, value in six.iteritems(kwargs):
                    print "name :"+ str(name)+" value : " + str(value)
                    #LOG.error("%s: %s" % (name, value))  # noqa

                if True:
                    six.reraise(*exc_info)
                else:
                    # at least get the core message out if something happened
                    message = self.msg_fmt

        self.message = message
        super(StockException, self).__init__(message)

    def format_message(self):
        # NOTE(mrodden): use the first argument to the python Exception object
        # which should be our full NovaException message, (see __init__)
        return self.args[0]
    
class Invalid(StockException):
    msg_fmt = "Bad Request - Invalid Parameters"
    code = 400
    
    
    
class DataBaseException(StockException):
    msg_fmt = "Failed to handle database: %(reason)s"
    code = 400