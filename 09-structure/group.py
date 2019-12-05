#def average_age():
#    """Compute the average age of the group's members."""
#    all_ages = [person["age"] for person in group.values()]
#    return sum(all_ages) / len(group)

def average_age(group):
    all_ages = [person["age"] for person in group.values()]
    return sum(all_ages) / len(group)


def forget(group, person1, person2):
    """Remove the connection between two people."""
    group[person1]["relations"].pop(person2, None)
    group[person2]["relations"].pop(person1, None)


def add_person(group, name, age, job, relations):
    """Add a new person with the given characteristics to the group."""
    new_person = {
        "age": age,
        "job": job,
        "relations": relations
    }
    group[name] = new_person


if __name__ == "__main__":

	group = {
		"Jill": {
		    "age": 26,
		    "job": "biologist",
		    "relations": {
		        "Zalika": "friend",
		        "John": "partner"
		    }
		},
		"Zalika": {
		    "age": 28,
		    "job": "artist",
		    "relations": {
		        "Jill": "friend"
		    }
		},
		"John": {
		    "age": 27,
		    "job": "writer",
		    "relations": {
		        "Jill": "partner"
		    }
		},
		"Nash": {
		    "age": 34,
		    "job": "chef",
		    "relations": {
		        "John": "cousin",
		        "Zalika": "landlord"
		    }
		}
	}

	print("The group has {} members with an average age of {}".format(
        len(group),
        average_age(group)
	))
