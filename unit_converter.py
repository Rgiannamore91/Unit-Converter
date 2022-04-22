# Programmer: Ryan Giannamore
# A prototype for a peice of fuctionality for an app that I am developing.
# Produces Unit conversions relevant to Part Library builds.

def main():
    """Gives options that point to the unit converters of each respective category."""
    display_menue()
    main_prompt = ""
    while main_prompt != 4:
        main_prompt = int(input("Enter choice here: "))
        if main_prompt == 1:
            cap()
            display_menue()
        elif main_prompt == 2:
            res()
            display_menue()
        elif main_prompt == 3:
            inch_to_mm()
            display_menue()
        elif main_prompt == 4:
            print("Than you, come again.")


def display_menue():
    """Displays a menue of options in the main function."""
    print("\nOptions:")
    print("\n1.) Capacitance Unit Conversions")
    print("2.) Resistance Unit Conversions")
    print("3.) Inch to MM Unit Conversions")
    print("4.) End")

def cap():
    """Provides Capacitance Conversions."""
    def cap_main():
        display_menue()
        main_prompt = ""
        while main_prompt != 5:
            main_prompt = int(input("Enter choice here: "))
            if main_prompt == 1:
                pf_to_uf()
                display_menue()
            elif main_prompt == 2:
                nf_to_uf()
                display_menue()
            elif main_prompt == 3:
                mf_to_uf()
                display_menue()
            elif main_prompt == 4:
                f_to_uf()
                display_menue()
            elif main_prompt == 5:
                print("Thank you come again.")
        
    def display_menue():
        print("\nOptions:")
        print("\n1.) pF to uF")
        print("2.) nF to uF")
        print("3.) mF to uF")
        print("4.) F to uF")
        print("5.) End")

    def pf_to_uf():
        pf_value = float(input("Enter pF value here: "))
        uf_value = float(pf_value/1000000)
        print(f"{float(uf_value)}uF")

    def nf_to_uf():
        nf_value = float(input("Enter nF value here: "))
        uf_value = float(nf_value/1000)
        print(f"{float(uf_value)}uF")

    def mf_to_uf():
        mf_value = float(input("Enter nF value here: "))
        uf_value = float(mf_value*1000)
        print(f"{float(uf_value)}uF")

    def f_to_uf():
        f_value = float(input("Enter F value here: "))
        uf_value = float(f_value*1000000)
        print(f"{float(uf_value)}uF")
    
    return cap_main()

def res():
    """Provides Resistance Conversions."""
    def res_main():
        display_menue()
        main_prompt = ""
        while main_prompt != 4:
            main_prompt = int(input("Enter choice here: "))
            if main_prompt == 1:
                mil_to_ohms()
                display_menue()
            elif main_prompt == 2:
                kil_to_ohms()
                display_menue()
            elif main_prompt == 3:
                meg_to_ohms()
                display_menue()
            elif main_prompt == 4:
                print("Thank you, come again.")
                
          

    def display_menue():
        print("\nOptions:")
        print("\n1.) mOhms to Ohms")
        print("2.) KOhms to Ohms")
        print("3.) MOhms to Ohms")
        print("4.) End")

    def mil_to_ohms():
        mil_value = float(input("Enter mOhms value here: "))
        ohms_value = float(mil_value/1000)
        print(f"{float(ohms_value)}Ohms")
    
    def kil_to_ohms():
        kil_value = float(input("Enter KOhms value here: "))
        ohms_value = float(kil_value*1000)
        print(f"{float(ohms_value)}Ohms")

    def meg_to_ohms():
        meg_value = float(input("Enter MOhms value here: "))
        ohms_value = float(meg_value*1000000)
        print(f"{float(ohms_value)}Ohms")

    return res_main()

def inch_to_mm():
    """provides Inch to MM Conversions."""
    inch_value = float(input("Enter inch value here: "))
    mm_value = float(inch_value*25.4) 
    print(f"{float(mm_value)}mm")

if __name__=='__main__':
    main()
