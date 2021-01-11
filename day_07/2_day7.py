import re

BAG_COLOR = 'shiny gold'

class Bag:
    def __init__(self, color):
        self.color = color
        self.bags = dict()
    
    def register_inside_bags(self, bag_color, bag_number):
        self.bags[bag_color] = bag_number


def define_rules(lines):
    rules = {}
    for rule in lines:
        rule = rule.split('bags contain')
        bag_color = rule[0].strip()

        if bag_color not in rules:
            rules[bag_color] = Bag(bag_color)

            if 'no other bags' in rule[1]:
                continue

            bags = rule[1].split(', ')
            for bag in bags:
                regex = re.compile(r"\d")
                bag_number = regex.match(bag.strip()).group()
                color = bag.replace(bag_number, '').replace('bags.', '').replace('bags', '').replace('bag.', '').replace('bag', '').strip()
                rules[bag_color].register_inside_bags(color, int(bag_number))

    return rules


def count_bags(bag, know_bags, rules):
    if not bag.bags:
        return 0
    
    if bag.color in know_bags:
        return know_bags[bag.color]

    count = 0
    for inside_bag in bag.bags:
        count += bag.bags[inside_bag] + bag.bags[inside_bag] * count_bags(rules[inside_bag], know_bags, rules)

    know_bags[bag.color] = count

    return know_bags[bag.color]

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    rules = define_rules(lines)

    my_bag = rules[BAG_COLOR]
    bags = {}
    
    bags = count_bags(my_bag, bags, rules)
    
    print(bags)