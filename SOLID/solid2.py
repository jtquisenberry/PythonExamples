

# Liskov Substitution
# The Liskov Substitution Principle (LSP): functions that use pointers to base classes must be able to use objects of derived classes without knowing it.
# https://www.tomdalling.com/blog/software-design/solid-class-design-the-liskov-substitution-principle/


''' Ensure Penguin does not inherit flying from Bird
//Solution 3: Proper inheritance
class Bird {
public:
    virtual void draw() = 0;
    virtual void setLocation(double longitude, double latitude) = 0;
};

class FlightfulBird : public Bird {
public:
    virtual void setAltitude(double altitude) = 0;
};
'''


#SRP 	The Single Responsibility Principle 	A class should have one, and only one, reason to change.
#OCP 	The Open Closed Principle 	You should be able to extend a classes behavior, without modifying it.
#LSP 	The Liskov Substitution Principle 	Derived classes must be substitutable for their base classes.
#ISP 	The Interface Segregation Principle 	Make fine grained interfaces that are client specific.
#DIP 	The Dependency Inversion Principle 	Depend on abstractions, not on concretions.
# http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod


