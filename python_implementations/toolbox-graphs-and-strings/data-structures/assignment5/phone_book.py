# python3

# Phone book

# Task. In this task your goal is to implement a simple phone book 
# manager. It should be able to process the following types of 
# user’s queries:

# add number name. It means that the user adds a person with 
# name name and phone number number to the phone book. If there 
# exists a user with such number already, then your manager has 
# to overwrite the corresponding name.

# del number. It means that the manager should erase a person 
# with number number from the phone book. If there is no such 
# person, then it should just ignore the query.

# find number. It means that the user looks for a person with 
# phone number number. The manager should reply with the 
# appropriate name, or with string “not found" (without quotes) 
# if there is no such person in the book.

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = ['' for _ in range(10 ** 7)]
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':   
            contacts[cur_query.number] = ''

        else:
            response = contacts[cur_query.number]
            if contacts[cur_query.number] == '':
                    response = "not found"
            result.append(response)
    return result

def main():
    write_responses(process_queries(read_queries()))


if __name__ == '__main__':
    main()