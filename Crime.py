# This files deals with specifics of crimes. 

class Crime(object):

    # A method that returns between 0 and 1 how bad a crime is
    @staticmethod
    def severeness(desc):
        crimeClass = [("theft", 1.0)]
                     # [("burglary", 1.0), ("theft", 1.0), ("robbery", 1.0),
                     #  ("dui", 1.0), ("assault", 1.0), ("arson", 1.0), 
                     #  ("kidnapping", 1.0)]
        for (c, v) in crimeClass:
            if (desc.lower().find(c) != -1):
                return v
        return 0.0
