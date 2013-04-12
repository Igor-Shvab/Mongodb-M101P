#ruby
connection = Mongo::Connection.new
db = connection.db("students")
grades=db.collection("grades").find("type" => "homework").sort({student_id:1, score:1})

student_id = -1
while grades.has_next? do
  grade = grades.next
  if student_id != grade["student_id"]
    student_id = grade["student_id"]
    puts grade
    db.collection("grades").remove(grade)
  end
end