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

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    rules = define_rules(lines)
    
    counter = 0
    colors = [BAG_COLOR]
    verified_colors = [BAG_COLOR]
    while True:
        next_colors = []
        for bag in rules:
            for bag_color in rules[bag].bags:
                if (bag_color in colors) and (rules[bag].color not in verified_colors):
                    counter += 1
                    next_colors.append(rules[bag].color)
                    verified_colors.append(rules[bag].color)

        if next_colors:
            colors = next_colors[:]
        else:
            break
    
    print(counter)