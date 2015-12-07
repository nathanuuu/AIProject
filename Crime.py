# This files deals with specifics of crimes. 

class Crime(object):

    # A method that returns between 0 and 1 how bad a crime is
    # CrimeClass is a list of (crime, vlaue) tuples
    @staticmethod
    def severeness(desc, crimeClass):
        for (c, v) in crimeClass:
            if (desc.lower().find(c.lower()) != -1):
                return v
        return 0.0
