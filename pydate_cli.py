import argparse
from pydate import activity
#from pydate import food
#from pydate import dessert
#from pydate import pickupline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", choices=["activity", "food", "dessert", "pickupline"])

    parser.add_argument("--indoor", choices=["True", "False"])
    parser.add_argument("--time", type=str, default="evening")

    args = parser.parse_args()

    if args.function == "activity":
        indoor = args.indoor == "True"
        result = activity(indoor=indoor, time=args.time)
    """elif args.function == "food":
    
    elif args.function == "dessert":
    
    elif args.function == "pickupline"""""


    print(result)

if __name__ == "__main__":
    main()

