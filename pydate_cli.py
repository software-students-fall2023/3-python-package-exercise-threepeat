import argparse
from pydate import activity
#from pydate import food
#from pydate import dessert
#from pydate import pickupline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", choices=["activity", "food", "dessert", "pickupline"])
    args = parser.parse_args()

    if args.function == "activity":
        parser.add_argument("--indoor", type=bool, default=True)
        parser.add_argument("--time", default="evening")
        activity_args = parser.parse_args()
        result = activity(indoor=activity_args.indoor, time=activity_args.time)
    """elif args.function == "food":
    
    elif args.function == "dessert":
    
    elif args.function == "pickupline"""""


    print(result)

if __name__ == "__main__":
    main()

