import argparse
from pydate import activity
from pydate import food
#from pydate import dessert
#from pydate import pickupline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", choices=["activity", "food", "dessert", "pickupline"])

    parser.add_argument("--indoor", choices=["True", "False"])
    parser.add_argument("--time", type=str, default="evening")
    parser.add_argument("--cuisine", type=str, default="French")
    parser.add_argument("--price_range", type=str, default="medium")
    parser.add_argument("--type", type=str, default="dinner")

    args = parser.parse_args()

    if args.function == "activity":
        indoor = args.indoor == "True"
        result = activity(indoor=indoor, time=args.time)
    elif args.function == "food":
        result = food(cuisine=args.cuisine, price_range=args.price_range, type=args.type)
    
    print(result)

if __name__ == "__main__":
    main()