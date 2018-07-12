import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
def main():
    f = open("zips.csv")
    reader = csv.reader(f)
    next(reader)
# reading and inserting values to database
    for row in reader:

        db.execute("INSERT INTO data (zipcode, city, state, lat, long, population) VALUES (:a, :b, :c, :d, :e, :f)",
                    {"a": row[0], "b": row[1], "c": row[2], "d":row[3], "e":row[4],"f":row[5]})
        # print(f"Added data to table {row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")

    db.commit()

if __name__ == "__main__":
    main()
