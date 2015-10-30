"""This module illustrates how to write your docstring in OpenAlea
and other projects related to OpenAlea."""

__license__ = "Cecill-C"
__revision__ = " $Id: actor.py 1586 2009-01-30 15:56:25Z cokelaer $ "
__docformat__ = 'reStructuredText'

class User(object):
  """This class is represent a user with age and name
  :Example:

    >>> import testDocsPy
    >>> a = testDocsPy.User()
    >>> print a
    Name: Mark
    Age: 21

    >>> import testDocsPy
    >>> a = testDocsPy.User("Gogo", 12)
    >>> print a
    Name: Gogo
    Age: 12

  """
  def __init__(self, name = "Mark", age = 21):
    self.name = name
    self.age = age
  def __repr__(self):
    return ("Name: {}\nAge: {}").format(self.name, self.age)
    
  

class MainClass1(object):
    """This class docstring shows how to use sphinx and rst syntax

    The first line is brief explanation, which may be completed with 
    a longer one. For instance to discuss about its methods. The only
    method here is :func:`function1`'s. The main idea is to document
    the class and methods's arguments with 

    - **parameters**, **types**, **return** and **return types**::

          :param arg1: description
          :param arg2: description
          :type arg1: type description
          :type arg1: type description
          :return: return description
          :rtype: the return type description

    - and to provide sections such as **Example** using the double commas syntax::

          :Example:

          followed by a blank line !

      which appears as follow:

      :Example:

      followed by a blank line

    - Finally special sections such as **See Also**, **Warnings**, **Notes**
      use the sphinx syntax (*paragraph directives*)::

          .. seealso:: blabla
          .. warnings also:: blabla
          .. note:: blabla
          .. todo:: blabla

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: That (and when) a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.

    Here below is the results of the :func:`function1` docstring.

    """
    def funcTest(self, arg1, arg2):
      """returns arg1 + arg2

      :param arg1: the first value
      :param arg2: the second value
      :type arg1: int, float,...
      :type arg2: int, float,...
      :returns: arg1 + arg2
      :rtype: int, float

      :Example:

        >>> import testDocsPy
        >>> a = testDocsPy.MainClass1()
        >>> a.funcTest(1,1)
        2


        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arguments should be not string
        .. todo:: check that arg1 or arg2 is not strings
        """
      return arg1 + arg2

    def function1(self, arg1, arg2, arg3):
        """returns (arg1 / arg2) + arg3

        **Drawbacks**:
         - Just looking at the docstring, the parameter, type and  return
           sections do not appear nicely

        :param arg1: the first value
        :param arg2: the second value
        :param arg3: the third value
        :type arg1: int, float,...
        :type arg2: int, float,...
        :type arg3: int, float,...
        :returns: arg1/arg2 +arg3
        :rtype: int, float

        :Example:

        >>> import testDocsPy
        >>> a = testDocsPy.MainClass1()
        >>> a.function1(1,1,1)
        2


        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.
        """
        return arg1/arg2 + arg3

if __name__ == "__main__":
  import doctest
  doctest.testmod()
  a = User("Gogo", 12)
  print a