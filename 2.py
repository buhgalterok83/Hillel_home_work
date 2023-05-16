digraph {
  node [shape=class, fontname=Arial];
  edge [fontname=Arial];
  
  Course [label="{Course | -course_code: string \l -course_name: string \l -professor: Professor \l -students: list<Student> \l| +add_student(student: Student) \l +remove_student(student: Student)}"];
  
  Professor [label="{Professor | -name: string \l -courses_taught: list<Course> \l| +add_course(course: Course) \l +remove_course(course: Course)}"];
  
  Student [label="{Student | -name: string \l -courses_enrolled: list<Course> \l| +enroll_course(course: Course) \l +drop_course(course: Course)}"];
  
  Course -> Professor [label="professor"];
  Course -> Student [label="students"];
}
