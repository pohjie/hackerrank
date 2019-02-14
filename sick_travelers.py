#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the traceDisease function below.
# initialStates is an array of strings, each string a line of input. 
# Your return value should also be a list of strings (see the prompt for the expected output format)
# Content sent to stdout (i.e. any print statements) will be sent to a separate output that is ignored by the test checker.

# constants
HEALTHY = "HEALTHY"
SICK = "SICK"
RECOVERING = "RECOVERING"

# data structures
person_health = {}
person2idx = {}
idx2person = {}
city2idx = {}

def preProcess(initialStates):
    person_counter = 0
    city_counter = 0

    num_people = len(initialStates)
    num_cities = 0
    city_schedule = []

    for i in range(num_people):
        person_info = initialStates[i].split()
        person = person_info[0]

        person_health[person] = person_info[1] # read in
        person2idx[person] = person_counter
        idx2person[person_counter] = person

        person_counter = person_counter + 1

        this_person_schedule = []
        for j in range(2, len(person_info)):
            city = person_info[j]
            this_person_schedule.append(city)
            if city not in city2idx:
                num_cities = num_cities + 1
                city2idx[city] = city_counter

                city_counter = city_counter + 1

        city_schedule.append(this_person_schedule)

    return num_people, num_cities, city_schedule, person2idx, idx2person, city2idx

def get_curr_city_idx(person, step_idx, city_schedule):
    person_idx = person2idx[person]
    max_travels = len(city_schedule[person_idx])
    curr_loc_idx = step_idx % max_travels

    curr_city_idx = city2idx[city_schedule[person_idx][curr_loc_idx]]

    return curr_city_idx

def traceDisease(initialStates):
    num_people, num_cities, city_schedule, person2idx, idx2person, city2idx = preProcess(initialStates)
    output = ""
    output_list = []
    for i in range(num_people):
        output = output + idx2person[i] + " "

    output = output.rstrip()
    output_list.append(output)

    # processing step
    for i in range(365): # max number of turns allowed
        output = ""
        cities_status = [0] * num_cities
        people_status = [None] * num_people
        healthy_people = set()

        for person in person_health:
            people_status[person2idx[person]] = person_health[person]
            if person_health[person] == HEALTHY:
                healthy_people.add(person)
            else: # SICK or RECOVERING
                if person_health[person] == SICK:
                    person_health[person] = RECOVERING
                elif person_health[person] == RECOVERING:
                    person_health[person] = HEALTHY
      
                curr_city_idx = get_curr_city_idx(person, i, city_schedule)
                cities_status[curr_city_idx] = 1 # infested!

        for person in healthy_people:
            curr_city_idx = get_curr_city_idx(person, i, city_schedule)
            if cities_status[curr_city_idx] == 1:
                person_health[person] = SICK

        for j in range(num_people):
            output = output + people_status[j] + " "

        output = output.rstrip()
        output_list.append(output)

        # check if everyone is healthy
        all_healthy = True
        for j in range(num_people):
            if people_status[j] != HEALTHY:
                all_healthy = False
                break

        if all_healthy:
            output_list.append(str(i + 1))
            return output_list

    output_list.append(str(365))
    return output_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    initialStates_count = int(input())

    initialStates = []

    for _ in range(initialStates_count):
        initialStates_item = input()
        initialStates.append(initialStates_item)

    res = traceDisease(initialStates)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()
