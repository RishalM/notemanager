import pymongo
client = pymongo.MongoClient("mongodb+srv://Rishal:xJDh5TGfDHbJzH4@rishal.68vjh.mongodb.net/?retryWrites=true&w=majority")
database = client["MyDatabase"]
# collection = database["MyCollection"]
# record = {"name":"John","age":40,"country":"US"}
# collection.insert_one(record)
# record2 = {"name":"Duncan","age":25,"country":"Sweden"}
# collection.insert_one(record2)
# record3 = {"name":"Oscar","age":14,"country":"Germany"}
# record4 = {"name":"Vivaan","age":19,"country":"Afghanistan"}
# record5 = {"name":"Riyana","age":27,"country":"Singapore"}
# records = [record3,record4,record5]
# collection.insert_many(records)
# collection.update_one({"name":"John"},{"$set":{"country":"UK"}})
# collection.update_one({"country":"Afghanistan"},{"$set":{"age":27}})
# record6 = {"name":"Timothy","age":65,"country":"US"}
# record7 = {"name":"Arjun","age":52,"country":"US"}
# record8 = {"name":"Peter","age":8,"country":"US"}
# recordsSixthroughEight = [record6,record7,record8]
# collection.insert_many(recordsSixthroughEight)
# collection.update_many({"country":"US"},{"$set":{"city":"Los Angeles"}})
# collection.update_one({"country":"US"},{"$set":{"state":"California"}})
# collection.update_one({"country":"Japan"},{"$set":{"city":"Tokyo"}})
# collection.delete_one({"country":"Germany"})
# collection.delete_many({"country":"US"})
# personfromuk = collection.find_one({"country":"UK"})
# print(personfromuk)
# allfromus = collection.find({"country":"US"})
# for each in allfromus:
#     print(each)
collection = database["Students"]
record1 = {"name":"Eliot","age":9,"city":"SF","state":"California","country":"US"}
record2 = {"name":"Marcus","age":17,"city":"Chicago","state":"Illinois","country":"US"}
record3 = {"name":"Wyatt","age":12,"city":"Albany","state":"NY","country":"US"}
record4 = {"name":"Tim","age":6,"city":"Seattle","state":"Washington","country":"US"}
students = [record2,record3,record4]
# collection.insert_one(record1)
# collection.insert_many(students)
# collection.update_one({"city":"SF"},{"$set":{"age":10}})
# collection.update_many({"country":"US"},{"$set":{"zipCode":"14869"}})
# collection.delete_one({"city":"Albany"})
# collection.delete_many({"city":"Miami"})
# studentagedseventeen = collection.find_one({"age":17})
# print(studentagedseventeen)
# allfromUS = collection.find({"country":"US"})
# for each in allfromUS:
    # print(each)
# allfromGermany = collection.find({"country":"Germany"})
# for each in allfromGermany:
#     print(each)



