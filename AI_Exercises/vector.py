class Vector:
    """ A class to represent a Euclidean vector with magnitude and direction"""

    def_init_(self,*numbers) 
         print(numbers)
         for number in numbers:
             if not isinstance(number,(float,int)):
                 raise TypeError(f"{number} must be a float or int not{type(number)}")

         if len(numbers)  <=0:
             raise ValueError("vectors can't be empty")   

         #self._numbers=(float(number) for number in numbers)     
         #self.numbers=number for number in numbers)  

         self.numbers=tuple(number for number in numbers)  


      @property
      def numbers(self)    
      return self._numbers

# v1=(1,1), v2=(1,1,14,5,252,56,2,7)        